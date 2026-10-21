"""Zentrale Konfiguration - HIER werden Experimente gesteuert."""
from pathlib import Path

# --- Pfade (relativ zum Projektordner, unabhaengig davon, wo man startet) ---
ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "Dataset"
MODELS_DIR = ROOT / "Models"
RESULTS_DIR = ROOT / "Results"

# später - nach EDA merge Dataset?? - tbd
# Huggingface
CYBER_DIR = DATA_DIR / "cyberagent_H1"
CYBER_REPO_DIR = CYBER_DIR / "FFHQ-Makeup"
CYBER_PERSONS_DIR = CYBER_REPO_DIR / "FFHQ-Makeup"   # hier liegen die Personenordner
CYBER_IMAGES_DIR = CYBER_REPO_DIR / "images"         # separater Ordner, NICHT Teil der Personen
CYBER_README = CYBER_REPO_DIR / "README.md"
CYBER_BARE_STEM = "bare"
CYBER_MAKEUP_STEMS = [f"makeup_{i:02d}" for i in range(1, 6)]   # makeup_01 ... makeup_05
CYBER_EXPECTED_STEMS = {CYBER_BARE_STEM, *CYBER_MAKEUP_STEMS}
CYBER_EXPECTED_PER_PERSON = len(CYBER_EXPECTED_STEMS)           # 6
 
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png"}





# Kaggle - 26 Datenpunkte -> daher nur zum Validieren oder zum Testen nutzen!!!
DATA_DIR_tapakah68_K1 = DATA_DIR / "tapakah68_K1"

"""
if __name__ == "__main__":
    print("Projektordner:", ROOT)
    for name, p in [("Personenordner", CYBER_PERSONS_DIR), ("images", CYBER_IMAGES_DIR), ("README", CYBER_README)]:
        print(f"{name:15s} {'OK     ' if p.exists() else 'FEHLT  '} {p}")
"""