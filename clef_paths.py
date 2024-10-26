import os 
from clef_extractors import *

if not os.environ["CLEF_HOME"] or not os.path.exists(os.environ["CLEF_HOME"]):
  raise RuntimeError("Environment variable CLEF_HOME is not set.")

CLEF_BASE_DIR = os.environ["CLEF_HOME"]
CLEF_LOWRES_DIR = ""

if not CLEF_BASE_DIR:
  raise FileNotFoundError(f"Download CLEF and set CLEF_BASE_DIR in {__file__}")

#
# CLEF paths
#
PATH_BASE_QUERIES = CLEF_BASE_DIR + "Topics/"
PATH_BASE_DOCUMENTS = CLEF_BASE_DIR + "DocumentData/"
PATH_BASE_EVAL = CLEF_BASE_DIR + "RelAssess/"

# Prepare dutch CLEF data paths
nl_all = (PATH_BASE_DOCUMENTS + "dutch/all/", extract_dutch)
dutch = {"2001": [nl_all], "2002": [nl_all], "2003": [nl_all]}

# Prepare italian CLEF data paths
it_lastampa = (PATH_BASE_DOCUMENTS + "italian/la_stampa/", extract_italian_lastampa)
it_sda94 = (PATH_BASE_DOCUMENTS + "italian/sda_italian/", extract_italian_sda9495)
it_sda95 = (PATH_BASE_DOCUMENTS + "italian/agz95/", extract_italian_sda9495)
italian = {"2001": [it_lastampa, it_sda94],
           "2002": [it_lastampa, it_sda94],
           "2003": [it_lastampa, it_sda94, it_sda95]}

# Prepare finnish CLEF data paths
aamu9495 = PATH_BASE_DOCUMENTS + "finnish/aamu/"
fi_ammulethi9495 = (aamu9495, extract_finish_aamuleth9495)
finnish = {
  "2001": None,
  "2002": [fi_ammulethi9495],
  "2003": [fi_ammulethi9495]
}

# Prepare english CLEF data paths
gh95 = (PATH_BASE_DOCUMENTS + "english/GH95/", extract_english_gh)
latimes = (PATH_BASE_DOCUMENTS + "english/latimes/", extract_english_latimes)
english = {
  "2001": [gh95, latimes],
  "2002": [gh95, latimes],
  "2003": [gh95, latimes]
}

# Prepare german CLEF data paths
der_spiegel = (PATH_BASE_DOCUMENTS + "german/der_spiegel/", extract_german_derspiegel)
fr_rundschau = (PATH_BASE_DOCUMENTS + "german/fr_rundschau/", extract_german_frrundschau)
de_sda94 = (PATH_BASE_DOCUMENTS + "german/sda94/", extract_german_sda)
de_sda95 = (PATH_BASE_DOCUMENTS + "german/sda95/", extract_german_sda)
german = {
  "2003": [der_spiegel, fr_rundschau, de_sda94, de_sda95],
  "2002": [der_spiegel, fr_rundschau, de_sda94, de_sda95]
}

# Prepare russian CLEF data paths
xml = (PATH_BASE_DOCUMENTS + "russian/xml/", extract_russian)
russian = {"2003": [xml]}
all_paths = {"nl": dutch, "it": italian, "fi": finnish, "en": english, "de": german, "ru": russian}

# Utility function
languages = [("de", "german"), ("en", "english"), ("ru", "russian"), ("fi", "finnish"), ("it", "italian"),
             ("fr", "french"), ("tr", "turkish"), ("es", "spanish"), ("nl", "dutch"), ("sv", "sv")]
short2pair = {elem[0]: elem for elem in languages}
long2pair = {elem[1]: elem for elem in languages}
def get_lang2pair(language):
  return long2pair[language] if len(language) != 2 else short2pair[language]
