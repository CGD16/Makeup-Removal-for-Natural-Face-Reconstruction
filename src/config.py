"""Zentrale Konfiguration - HIER werden Experimente gesteuert."""
from pathlib import Path

# --- Pfade (relativ zum Projektordner, unabhaengig davon, wo man startet) ---
ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "Dataset"
MODELS_DIR = ROOT / "Models"
RESULTS_DIR = ROOT / "Results"



# später - nach EDA merge Dataset?? - tbd
# Huggingface
DATA_DIR_cyberagent_H1_all = DATA_DIR / "cyberagent_H1/FFHQ-Makeup/FFHQ-Makeup"
DATA_DIR_cyberagent_H1_test = DATA_DIR / "cyberagent_H1/FFHQ-Makeup/images"


# Kaggle - 26 Datenpunkte -> daher nur zum Validieren oder zum Testen nutzen!!!
DATA_DIR_tapakah68_K1 = DATA_DIR / "tapakah68_K1"

