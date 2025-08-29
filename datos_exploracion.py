import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import re, unicodedata
# Leer los datos
DATA_PATH = Path("/content/datos/JEFAB_2024_clean.xlsx")  # evita rutas de Colab
FIG_DIR = Path("figuras"); FIG_DIR.mkdir(exist_ok=True, parents=True)
TAB_DIR = Path("tablas");  TAB_DIR.mkdir(exist_ok=True, parents=True)
# Explorar estructura básica
def _norm(s):
    s = str(s) if s is not None else ""
    s = unicodedata.normalize("NFKD", s).encode("ascii","ignore").decode("ascii")
    return re.sub(r"\s+"," ", s).strip().upper()
 
