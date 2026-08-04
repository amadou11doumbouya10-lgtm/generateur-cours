import os
import re
import time
import requests
import joblib
from urllib.parse import quote

HEADERS = {
    "User-Agent": "GenerateurCoursBot/1.0 (https://github.com/; contact@example.com)"
}

DELAI_ENTRE_REQUETES = 0.5  # secondes, pour éviter le rate-limiting de Wikipedia

# Tournures descriptives courantes dans les titres de modules générés par IA
# ("Introduction aux fondamentaux de l'IA", "Principes de base du Machine Learning").
# Utilisées uniquement en repli si la recherche du sujet tel quel ne trouve rien.
_PREFIXES_DESCRIPTIFS = [
    r"^introduction\s+(?:aux|au|à)\s+",
    r"^principes?\s+(?:de\s+base\s+)?(?:de|du|des|d')\s+",
    r"^notions?\s+(?:fondamentales?\s+)?(?:de|du|des|d')\s+",
    r"^(?:les\s+)?bases?\s+(?:de|du|des|d')\s+",
    r"^fondamentaux\s+(?:de|du|des|d')\s+",
    r"^compr[ée]hension\s+(?:de|du|des|d')\s+",
    r"^d[ée]couverte\s+(?:de|du|des|d')\s+",
    r"^mise\s+en\s+[œoe]uvre\s+(?:de|du|des|d')\s+",
]

_SUFFIXES_DESCRIPTIFS = [
    r"\s+(?:avec|en)\s+python$",
]


def _nettoyer_sujet(sujet):
    """Retire les tournures descriptives courantes pour isoler le sujet recherchable."""
    resultat = sujet
    for _ in range(3):  # jusqu'à 3 préfixes empilés ("Introduction aux fondamentaux de...")
        avant = resultat
        for motif in _PREFIXES_DESCRIPTIFS:
            resultat = re.sub(motif, "", resultat, flags=re.IGNORECASE).strip()
        if resultat == avant:
            break
    for motif in _SUFFIXES_DESCRIPTIFS:
        resultat = re.sub(motif, "", resultat, flags=re.IGNORECASE).strip()
    # Retire un article isolé qui traîne après nettoyage ("l'IA" -> "IA") : laissé tel quel,
    # ce genre de fragment fait dériver la recherche sur des titres sans rapport (ex: "L'incoronazione di Poppea").
    resultat = re.sub(r"^(?:l['’]|les?\s+|la\s+)", "", resultat, flags=re.IGNORECASE).strip()
    return resultat

CHEMIN_MODELE_PERTINENCE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "entrainement", "modele_pertinence.pkl"
)

try:
    _pipeline_pertinence = joblib.load(CHEMIN_MODELE_PERTINENCE)
except FileNotFoundError:
    _pipeline_pertinence = None


def extrait_est_pertinent(sujet, extrait):
    """Utilise le classifieur entraîné (entrainement/) pour juger si un extrait est exploitable.

    Si le modèle n'a pas encore été entraîné, on ne filtre rien (tout extrait non-vide passe).
    """
    if not extrait:
        return False
    if _pipeline_pertinence is None:
        return True
    return _pipeline_pertinence.predict([sujet + " " + extrait])[0] == "UTILE"


def _requete_opensearch(sujet, domaine):
    """Une seule requête à l'API opensearch de Wikipedia. Retourne le titre trouvé ou None."""
    url = f"https://{domaine}/w/api.php"
    params = {
        "action": "opensearch",
        "search": sujet,
        "limit": 1,
        "namespace": 0,
        "format": "json",
    }
    try:
        reponse = requests.get(url, headers=HEADERS, params=params, timeout=10)
        if reponse.status_code == 200:
            data = reponse.json()
            # data[1] est la liste des titres trouvés, dans l'ordre de pertinence
            titres = data[1] if len(data) > 1 else []
            return titres[0] if titres else None
        else:
            print(f"   [!] {domaine} (recherche) a répondu {reponse.status_code} pour '{sujet}'")
            return None
    except requests.exceptions.Timeout:
        print(f"   [!] Timeout recherche sur {domaine} pour '{sujet}'")
        return None
    except requests.exceptions.RequestException as e:
        print(f"   [!] Erreur réseau recherche sur {domaine} pour '{sujet}': {e}")
        return None
    except ValueError as e:
        print(f"   [!] Réponse JSON invalide (recherche) de {domaine} pour '{sujet}': {e}")
        return None
    finally:
        time.sleep(DELAI_ENTRE_REQUETES)


def _trouver_titre_reel(sujet, domaine):
    """
    Utilise l'API de recherche Wikipedia (opensearch) pour trouver le titre
    d'article le plus proche du sujet donné. Indispensable pour les titres
    de modules générés par l'IA ("Introduction aux fondamentaux de l'IA"),
    qui ne correspondent presque jamais exactement à un titre d'article.

    Si la recherche du sujet tel quel ne trouve rien, réessaie avec les
    tournures descriptives courantes retirées ("Introduction à...", "... avec Python").
    """
    titre = _requete_opensearch(sujet, domaine)
    if titre:
        return titre

    sujet_nettoye = _nettoyer_sujet(sujet)
    if sujet_nettoye and sujet_nettoye.lower() != sujet.lower():
        print(f"   [i] {domaine} : nouvelle recherche avec sujet simplifié : '{sujet_nettoye}'")
        titre = _requete_opensearch(sujet_nettoye, domaine)

    return titre


def _chercher_wikipedia_generique(sujet, domaine):
    """
    Fonction interne partagée par les deux langues.
    Étape 1 : trouve le titre d'article réel le plus proche du sujet (opensearch).
    Étape 2 : récupère le résumé de cette page précise (page/summary).
    """
    titre_reel = _trouver_titre_reel(sujet, domaine)
    if not titre_reel:
        print(f"   [!] {domaine} : aucun article trouvé pour '{sujet}'")
        return ""

    if titre_reel.lower() != sujet.lower():
        print(f"   [i] {domaine} : '{sujet}' -> page trouvée : '{titre_reel}'")

    url = f"https://{domaine}/api/rest_v1/page/summary/" + quote(titre_reel.replace(" ", "_"), safe="")
    try:
        reponse = requests.get(url, headers=HEADERS, timeout=10)
        if reponse.status_code == 200:
            data = reponse.json()
            return data.get("extract", "")
        else:
            print(f"   [!] {domaine} a répondu {reponse.status_code} pour '{titre_reel}'")
            return ""
    except requests.exceptions.Timeout:
        print(f"   [!] Timeout sur {domaine} pour '{titre_reel}'")
        return ""
    except requests.exceptions.RequestException as e:
        print(f"   [!] Erreur réseau sur {domaine} pour '{titre_reel}': {e}")
        return ""
    except ValueError as e:
        print(f"   [!] Réponse JSON invalide de {domaine} pour '{titre_reel}': {e}")
        return ""
    finally:
        time.sleep(DELAI_ENTRE_REQUETES)


def chercher_wikipedia(sujet):
    """Cherche un résumé sur Wikipedia en français."""
    return _chercher_wikipedia_generique(sujet, "fr.wikipedia.org")


def chercher_wikipedia_en(sujet):
    """Cherche un résumé sur Wikipedia en anglais (plus de contenu technique)."""
    return _chercher_wikipedia_generique(sujet, "en.wikipedia.org")


def collecter_infos(sujet):
    """Collecte toutes les infos disponibles sur le sujet."""
    print(f"\n Recherche d'informations sur : {sujet}")
    print(" Interrogation Wikipedia français...")
    info_fr = chercher_wikipedia(sujet)
    if info_fr and not extrait_est_pertinent(sujet, info_fr):
        print(" [ML] Extrait français jugé peu pertinent (homonymie/hors-sujet), ignoré.")
        info_fr = ""

    print(" Interrogation Wikipedia anglais...")
    info_en = chercher_wikipedia_en(sujet)
    if info_en and not extrait_est_pertinent(sujet, info_en):
        print(" [ML] Extrait anglais jugé peu pertinent (homonymie/hors-sujet), ignoré.")
        info_en = ""

    infos = {
        "sujet": sujet,
        "wikipedia_fr": info_fr,
        "wikipedia_en": info_en,
    }

    total = len(info_fr) + len(info_en)
    print(f" {total} caractères d'informations collectés.")
    return infos
