# ==========================
# 1) Análisis de datos faltantes
# ==========================
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import re, unicodedata
# Leer los datos
DATA_PATH = Path("/content/JEFAB_2024.xlsx")  # evita rutas de Colab
FIG_DIR = Path("figuras"); FIG_DIR.mkdir(exist_ok=True, parents=True)
TAB_DIR = Path("tablas");  TAB_DIR.mkdir(exist_ok=True, parents=True)
print("=== ANÁLISIS DE DATOS FALTANTES ===")
missing_data = df.isnull().sum()
missing_percent = (missing_data / len(df)) * 100

missing_info = pd.DataFrame({
    "Columna": missing_data.index,
    "Datos_Faltantes": missing_data.values,
    "Porcentaje": missing_percent.round(2).values
}).sort_values("Datos_Faltantes", ascending=False)

print("Top 10 columnas con más datos faltantes:")
print(missing_info.head(10))
missing_info.to_csv(TAB_DIR/"C_datos_faltantes.csv", index=False, encoding="utf-8")

# ==========================
# 2) Análisis de duplicados
# ==========================
print("\n=== ANÁLISIS DE DUPLICADOS ===")
duplicados = df.duplicated().sum()
print(f"Registros duplicados: {duplicados}")

# ==========================
# 3) Tipos de datos
# ==========================
print("\n=== TIPOS DE DATOS ===")
dtype_counts = df.dtypes.value_counts()
print(dtype_counts)
dtype_counts.to_csv(TAB_DIR/"C_tipos_datos.csv")

# ==========================
# 4) Columnas con caracteres problemáticos
# ==========================
print("\n=== COLUMNAS CON CARACTERES ESPECIALES ===")
problematic_columns = [col for col in df.columns if "Ã" in col or "â" in col or "�" in col]
print(f"Columnas con encoding problemático: {len(problematic_columns)}")
for col in problematic_columns[:10]:
    print(f" - {col}")

# ==========================
# Resumen automático (para el reporte .md)
# ==========================
# Create the reportes directory if it doesn't exist
Path("reportes").mkdir(exist_ok=True)

with open("reportes/calidad_datos.md", "w", encoding="utf-8") as f:
    f.write("# Reporte Estudiante C - Calidad de Datos\n\n")
    f.write("## 1. Columnas con más datos faltantes\n")
    f.write(missing_info.head(5).to_markdown(index=False))
    f.write("\n\n## 2. Registros duplicados\n")
    f.write(f"Se detectaron **{duplicados} registros duplicados** en la base de datos.\n")
    f.write("\n\n## 3. Problemas de encoding\n")
    if problematic_columns:
        f.write("Se detectaron problemas de caracteres extraños en las siguientes columnas:\n")
        for col in problematic_columns[:5]:
            f.write(f"- {col}\n")
    else:
        f.write("No se detectaron columnas con problemas de encoding.\n")

print("\n=== FIN DEL ANÁLISIS (Estudiante C) ===")
print("Resultados guardados en:")
print(f"- {TAB_DIR}/C_datos_faltantes.csv")
print(f"- {TAB_DIR}/C_tipos_datos.csv")
print("- reportes/calidad_datos.md")
# limpieza_datos.py (Estudiante C)
import pandas as pd
from pathlib import Path

# ==========================
# Configuración de rutas
# ==========================
DATA_PATH = Path("/content/JEFAB_2024.xlsx")      # archivo original
OUTPUT_PATH = Path("datos/JEFAB_2024_clean.xlsx")  # archivo limpio

# ==========================
# Cargar datos
# ==========================
if not DATA_PATH.exists():
    raise SystemExit(f"No se encontró el archivo {DATA_PATH}")
df = pd.read_excel(DATA_PATH)
df_clean = df.copy()

# ==========================
# 1. Eliminar duplicados
# ==========================
n_dup = df_clean.duplicated().sum()
if n_dup > 0:
    df_clean = df_clean.drop_duplicates()
print(f"Duplicados eliminados: {n_dup}")

# ==========================
# 2. Eliminar columnas con >50% faltantes
# ==========================
missing_ratio = df_clean.isnull().mean()
cols_drop = missing_ratio[missing_ratio > 0.5].index.tolist()
df_clean = df_clean.drop(columns=cols_drop)
print(f"Columnas eliminadas por >50% vacíos: {cols_drop}")

# ==========================
# 3. Imputación condicional
# ==========================
# --- HIJOS ---
if "HIJOS" in df_clean.columns and "ESTADO_CIVIL" in df_clean.columns:
    def imputar_hijos(row):
        if pd.isna(row["HIJOS"]):
            estado = str(row["ESTADO_CIVIL"]).upper()
            if "CASADO" in estado:
                return "SI"
            elif "SOLTERO" in estado:
                return "NO"
            else:
                return df_clean["HIJOS"].mode()[0]
        return row["HIJOS"]
    df_clean["HIJOS"] = df_clean.apply(imputar_hijos, axis=1)

# --- HIJOS_EN_HOGAR ---
if "HIJOS_EN_HOGAR" in df_clean.columns and "HIJOS" in df_clean.columns:
    def imputar_hijos_hogar(row):
        if pd.isna(row["HIJOS_EN_HOGAR"]):
            if str(row["HIJOS"]).upper() == "SI":
                return 1  # vive con hijos
            else:
                return 0  # no vive con hijos
        return row["HIJOS_EN_HOGAR"]
    df_clean["HIJOS_EN_HOGAR"] = df_clean.apply(imputar_hijos_hogar, axis=1)

# ==========================
# 4. Imputación simple
# ==========================
# Numéricas -> mediana
for col in df_clean.select_dtypes(include=["float64","int64"]).columns:
    if df_clean[col].isnull().any():
        df_clean[col] = df_clean[col].fillna(df_clean[col].median())

# Categóricas -> moda
for col in df_clean.select_dtypes(include=["object"]).columns:
    if df_clean[col].isnull().any():
        df_clean[col] = df_clean[col].fillna(df_clean[col].mode()[0])

# ==========================
# Guardar dataset limpio
# ==========================
# Create the output directory if it doesn't exist
OUTPUT_PATH.parent.mkdir(exist_ok=True, parents=True)
df_clean.to_excel(OUTPUT_PATH, index=False)
print(f"\nDataset limpio guardado en {OUTPUT_PATH}")
# demografia_basica.py
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import re, unicodedata
# Leer los datos
DATA_PATH = Path("/content/datos/JEFAB_2024_clean.xlsx")  # evita rutas de Colab
FIG_DIR = Path("figuras"); FIG_DIR.mkdir(exist_ok=True, parents=True)
TAB_DIR = Path("tablas");  TAB_DIR.mkdir(exist_ok=True, parents=True)

# --- Carga de datos (NUEVO) ---
if not DATA_PATH.exists():
    raise SystemExit(f"No se encontró el archivo: {DATA_PATH}. Colócalo en 'datos/'.")
df = pd.read_excel(DATA_PATH).dropna(axis=1, how="all")

# Si la limpiaste y guardaste en CSV
# df = pd.read_csv("JEFAB_2024_limpio.csv")

print("Base de datos limpia cargada. Registros:", len(df))

# Explorar estructura básica
def _norm(s):
    s = str(s) if s is not None else ""
    s = unicodedata.normalize("NFKD", s).encode("ascii","ignore").decode("ascii")
    return re.sub(r"\s+"," ", s).strip().upper()

def find_col(df, candidates):
    # Detecta columnas equivalentes (e.g., GENERO/SEXO, EDAD/EDAD2, GRADO/GRADO_MILITAR)
    cand = [_norm(c) for c in candidates]
    norm_map = {c: _norm(c) for c in df.columns}
    # match exacto normalizado
    for orig, normd in norm_map.items():
        if normd in cand:
            return orig
    # match parcial por tokens
    for orig, normd in norm_map.items():
        if any(tok in normd for tok in cand):
            return orig
    return None


# --- Explorar estructura básica (igual que tu idea) ---
print("=== INFORMACIÓN GENERAL ===")
print(f"Total de registros: {len(df)}")
print(f"Total de columnas: {len(df.columns)}")

# --- Detectar columnas clave con flexibilidad (NUEVO) ---
col_edad   = find_col(df, ["EDAD2","EDAD"])
col_genero = find_col(df, ["GENERO","SEXO"])
col_grado  = find_col(df, ["GRADO","GRADO_MILITAR"])

# ==========================
# 1) ANÁLISIS DE EDAD
# ==========================
print("\n=== ANÁLISIS DE EDAD ===")
if col_edad is None:
    print("No se encontró columna de edad (esperado: EDAD2/EDAD).")
else:
    s_edad = pd.to_numeric(df[col_edad], errors="coerce").dropna()
    if s_edad.empty:
        print("No hay datos numéricos de edad.")
    else:
        print(f"Edad promedio: {s_edad.mean():.1f} años")
        print(f"Edad mínima: {s_edad.min()} años")
        print(f"Edad máxima: {s_edad.max()} años")

        # Rango de edad más común (bins de 5 años)  -> Responde Pregunta 1
        bins = range(int(s_edad.min()) - (int(s_edad.min()) % 5),
                     int(s_edad.max()) + 5, 5)
        cat = pd.cut(s_edad, bins=bins, right=False)  # [a, b)
        moda_rango = cat.value_counts().idxmax() if not cat.empty else None
        print(f"Rango de edad más común: {moda_rango}")

        # Histograma + guardado
        plt.figure(figsize=(10,6))
        plt.hist(s_edad, bins=20, edgecolor='black')
        plt.title('Distribución de Edades del Personal FAC')
        plt.xlabel('Edad'); plt.ylabel('Cantidad de Personal')
        plt.tight_layout()
        plt.savefig(FIG_DIR / "A_demografia_edades_hist.png", dpi=130)
        plt.show(); plt.close()

# ==========================
# 2) ANÁLISIS DE GÉNERO
# ==========================
print("\n=== ANÁLISIS DE GÉNERO ===")
if col_genero is None:
    print("No se encontró columna de género (esperado: GENERO/SEXO).")
else:
    conteo_genero = df[col_genero].value_counts(dropna=False)
    print(conteo_genero)

    # Diferencias en la distribución por género -> Responde Pregunta 2
    porc_genero = (conteo_genero / conteo_genero.sum() * 100).round(2)
    print("\nParticipación por género (%):")
    print(porc_genero)

    # Barra y guardado
    plt.figure(figsize=(7,5))
    conteo_genero.plot(kind='bar', edgecolor='black')
    plt.title('Distribución por Género')
    plt.xlabel('Género'); plt.ylabel('Cantidad')
    plt.tight_layout()
    plt.savefig(FIG_DIR / "A_demografia_genero_bar.png", dpi=130)
    plt.show(); plt.close()

# ==========================
# 3) GRADO MILITAR (NUEVO)
# ==========================
print("\n=== GRADO MILITAR ===")
if col_grado is None:
    print("No se encontró columna de grado (esperado: GRADO/GRADO_MILITAR).")
else:
    conteo_grado = df[col_grado].value_counts(dropna=False)
    grado_top = conteo_grado.idxmax() if not conteo_grado.empty else None
    print("Top grados (head 10):")
    print(conteo_grado.head(10))
    print(f"\nGrado militar más frecuente: {grado_top}")  # -> Responde Pregunta 3

    # Guardar tabla top grados para tu reporte A
    conteo_grado.head(20).to_csv(TAB_DIR / "A_grado_militar_top.csv", encoding="utf-8")

print("\n=== FIN DEL ANÁLISIS (Estudiante A) ===")
print("Archivos generados:")
print(f"- Figuras: {FIG_DIR}/A_demografia_edades_hist.png, {FIG_DIR}/A_demografia_genero_bar.png")
print(f"- Tabla grado (top): {TAB_DIR}/A_grado_militar_top.csv")
# ==========================
# ANÁLISIS FAMILIAR
# ==========================
# --- Detectar columnas clave ---
col_estado   = find_col(df, ["ESTADO_CIVIL"])
col_hijos    = find_col(df, ["HIJOS"])
col_numhijos = find_col(df, ["NUMERO_HIJOS"])
col_conv     = find_col(df, ["HABITA_VIVIENDA_FAMILIAR","CONVIVE_CON_FAMILIA"])
col_edad     = find_col(df, ["EDAD2","EDAD"])
col_genero   = find_col(df, ["GENERO","SEXO"])
col_edu      = find_col(df, ["NIVEL_EDUCATIVO"])
col_estrato  = find_col(df, ["ESTRATO"])
col_vivienda = find_col(df, ["VIVIENDA_PROPIA"])

print("=== ANÁLISIS FAMILIAR (Estudiante B) ===")

# ==========================
# 1) Estado civil
# ==========================
print("\n=== ESTADO CIVIL ===")
if col_estado:
    conteo_ec = df[col_estado].value_counts(dropna=False)
    print(conteo_ec)
    porc_casados = (conteo_ec.get("CASADO",0)/len(df)*100) if len(df)>0 else 0
    print(f"% de casados: {porc_casados:.2f}%")

    plt.figure(figsize=(8,5))
    conteo_ec.plot(kind="bar", edgecolor="black")
    plt.title("Distribución Estado Civil")
    plt.xlabel("Estado Civil"); plt.ylabel("Cantidad")
    plt.tight_layout()
    plt.savefig(FIG_DIR / "B_estado_civil_bar.png", dpi=130)
    plt.show(); plt.close()
else:
    print("No se encontró columna de estado civil.")
    # ==========================
# 2) Hijos
# ==========================
print("\n=== HIJOS ===")
if col_hijos:
    conteo_h = df[col_hijos].value_counts(dropna=False)
    print(conteo_h)

    plt.figure(figsize=(6,4))
    conteo_h.plot(kind="bar", edgecolor="black", color="lightgreen")
    plt.title("Distribución: ¿Tiene hijos?")
    plt.xlabel("Respuesta"); plt.ylabel("Cantidad")
    plt.tight_layout()
    plt.savefig(FIG_DIR / "B_hijos_bar.png", dpi=130)
    plt.show(); plt.close()

if col_numhijos:
    serie_h = pd.to_numeric(df[col_numhijos], errors="coerce").dropna()
    print("\nNúmero de hijos - estadísticos:")
    print(serie_h.describe())
    serie_h.to_csv(TAB_DIR / "B_numero_hijos.csv", index=False)
    # ==========================
# 3) Convivencia familiar
# ==========================
print("\n=== CONVIVENCIA ===")
if col_conv:
    conteo_conv = df[col_conv].value_counts(dropna=False)
    print(conteo_conv)

    plt.figure(figsize=(6,4))
    conteo_conv.plot(kind="bar", edgecolor="black", color="salmon")
    plt.title("Convivencia con familia")
    plt.xlabel("Respuesta"); plt.ylabel("Cantidad")
    plt.tight_layout()
    plt.savefig(FIG_DIR / "B_convivencia_bar.png", dpi=130)
    plt.show(); plt.close()
    # ==========================
# 4) Patrones cruzados
# ==========================
print("\n=== PATRONES FAMILIARES ===")

# Estado civil vs Hijos
if col_estado and col_hijos:
    ct_ec_h = pd.crosstab(df[col_estado], df[col_hijos], normalize="index")*100
    print("\n% Hijos según Estado Civil:")
    print(ct_ec_h.round(1))
    ct_ec_h.to_csv(TAB_DIR / "B_estado_vs_hijos.csv")

# Hijos vs Convivencia
if col_hijos and col_conv:
    ct_h_c = pd.crosstab(df[col_hijos], df[col_conv], normalize="index")*100
    print("\n% Convivencia según Hijos:")
    print(ct_h_c.round(1))
    ct_h_c.to_csv(TAB_DIR / "B_hijos_vs_convivencia.csv")

# Edad y estado civil
if col_edad and col_estado:
    serie_edad = pd.to_numeric(df[col_edad], errors="coerce")
    resumen = df.groupby(col_estado)[col_edad].mean().round(1)
    print("\nEdad promedio por estado civil:")
    print(resumen)
    resumen.to_csv(TAB_DIR / "B_edad_vs_estado.csv")
# --- Boxplot: Edad ~ Estado civil (corregido) ---
if col_edad and col_estado:
    # Copia segura y tipos correctos
    _tmp = df[[col_edad, col_estado]].copy()
    _tmp[col_edad] = pd.to_numeric(_tmp[col_edad], errors="coerce")
    _tmp = _tmp.dropna(subset=[col_edad, col_estado])

    if not _tmp.empty:
        plt.figure(figsize=(9,6))
        # Usar las referencias de columna reales (no strings literales)
        _tmp.boxplot(column=col_edad, by=col_estado, grid=False)
        plt.title("Edad según Estado Civil")
        plt.suptitle("")  # quita el título automático de pandas
        plt.ylabel("Edad")
        plt.xlabel("Estado Civil")
        plt.xticks(rotation=30)
        plt.tight_layout()
        plt.savefig(FIG_DIR / "B_edad_estado_civil.png", dpi=130)
        plt.show(); plt.close()
    else:
        print("No hay datos válidos para el boxplot de edad por estado civil.")

# Género y familia
if col_genero and col_hijos:
    ct_g_h = pd.crosstab(df[col_genero], df[col_hijos], normalize="index")*100
    print("\n% Hijos según Género:")
    print(ct_g_h.round(1))
    ct_g_h.to_csv(TAB_DIR / "B_genero_vs_hijos.csv")

# Educación y familia
if col_edu and col_hijos:
    ct_e_h = pd.crosstab(df[col_edu], df[col_hijos], normalize="index")*100
    print("\n% Hijos según Nivel Educativo:")
    print(ct_e_h.round(1))
    ct_e_h.to_csv(TAB_DIR / "B_educacion_vs_hijos.csv")
