# Reporte Estudiante C - Calidad de Datos

## Metodología de limpieza y preparación de datos

### 1) Corrección de encoding (mojibake)

**Objetivo.**  
Eliminar artefactos de codificación (p. ej., Ã, Â, ¿, ¡) tanto en nombres de columnas como en celdas de texto para evitar categorías duplicadas o fallos en agrupaciones/joins.

**Qué hicimos.**
- Normalización Unicode (NFKD) y corrección de rutas comunes UTF-8 ↔️ latin-1.  
- Escaneo de tokens sospechosos para cuantificar el problema.  
- Revisión puntual posterior (quedaron 2 celdas residuales por homologar).  

---

### 2) Consolidación de variables dummy `_SI` / `_NO` / `_NO_RESP` → `*_BIN`

**Objetivo.**  
Evitar contradicciones (“SI” y “NO” simultáneos) convirtiendo cada grupo en una sola variable binaria.

**Regla.**
- `1` = “Sí”  
- `0` = “No”  
- `NaN` = “No responde” (no se confunde con “No”)  

**Qué hicimos.**
- Identificamos grupos `_SI` / `_NO` / `_NO_RESP`.  
- Creamos 16 columnas `*_BIN` y eliminamos sus dummies originales.  

---

### 3) Tratamiento de “NO RESPONDE” (texto) → `NaN`

**Objetivo.**  
Evitar sesgo interpretando “No responde” como “No”. Se trata como faltante.  

**Qué hicimos.**
- Mapeo de variantes: `NO RESPONDE`, `NO RESP.`, `SIN RESPUESTA`, `NR`, `N/R` → `NaN` (insensible a acentos/espacios).  
- Aplicado a todas las hojas del Excel final.  

---

### 4) Imputación de faltantes (numéricas y categóricas)

**Objetivo.**  
Completar faltantes con métodos que respeten el dominio y aprovechen correlaciones.  

**Estrategia aplicada.**
- **Categóricas (texto):** moda (global o por segmento, si procede).  
  → Resultado: 34 columnas imputadas; 118,732 celdas completadas.  
- **Numéricas:** en la versión final no se registró imputación adicional (0 columnas en el reporte).  
  (En corridas previas se usó MICE con límites: bin 0–1, Likert 0–10, continuas [p1,p99]+clipping).  

---

### 5) Análisis de Componentes Principales (PCA) para reducción de colinealidad

**Objetivo.**  
Compactar información de variables altamente correlacionadas en componentes ortogonales, estabilizando análisis y modelos.  

**Qué hicimos.**
- Estandarizamos numéricas y aplicamos PCA con criterio de 80% de varianza acumulada.  
- Se seleccionaron 79 componentes (`PC1..PC79`), con varianza acumulada de **80.40%**.  
