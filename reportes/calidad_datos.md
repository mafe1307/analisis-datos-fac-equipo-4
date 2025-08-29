# Reporte Estudiante C - Calidad de Datos

## 1. Columnas con más datos faltantes

Durante la revisión de la base de datos original *JEFAB_2024.xlsx* se identificaron los siguientes problemas de calidad:

- *Datos faltantes:*
  - Variables con más del 50% de vacíos:  
    - NUMERO_PERSONAS_APORTE_SOSTENIMIENTO2 (61.2%)  
    - NUMERO_HABITAN_VIVIENDA2 (59.3%)  
    - NUMERO_HIJOS (50.1%)  
    - HIJOS_EN_HOGAR (49.8%)  
  - Variables con entre 10% y 30% de vacíos:  
    - EDAD_PADRE y EDAD_RANGO_PADRE (30.2%)  
    - EDAD_MADRE y EDAD_RANGO_MADRE (13–14%)
  - Variables con menos del 1% de vacíos:  
    - EDAD2 (0.2%).

- *Duplicados:*  
  No se encontraron registros duplicados.

- *Encoding:*  
  No se identificaron problemas de codificación en los nombres de las columnas.

- *Tipos de datos:*  
  - 153 columnas numéricas (int64)  
  - 66 categóricas (object)  
  - 12 decimales (float64)

---

## 2. Estrategias de limpieza aplicadas

- *Eliminación de columnas:*  
  Se eliminaron variables con más del 50% de vacíos, por considerarse poco útiles para el análisis.

- *Imputación simple:*  
  - En variables numéricas con pocos faltantes (ej. EDAD2), se aplicó *mediana*.  
  - En variables categóricas, se aplicó *moda*.

- *Imputación condicional:*  
  - HIJOS:  
    - Casados → imputados como “Sí”  
    - Solteros → imputados como “No”  
    - Otros estados civiles → moda general de la variable.  
  - HIJOS_EN_HOGAR:  
    - Si la persona tiene hijos (HIJOS = Sí) → imputado como 1 (convive con hijos).  
    - Si no tiene hijos → imputado como 0.  

- *Estandarización de categorías:*  
  Se normalizaron valores categóricos para evitar variantes por espacios o mayúsculas (ej. “Soltero”, “SOLTERO/A”).

---

## 3. Resultados de la limpieza

- Columnas eliminadas: 4.  
- Registros duplicados eliminados: 0.  
- Valores imputados en HIJOS: XX (indica cuántos).  
- Valores imputados en HIJOS_EN_HOGAR: XX (indica cuántos).  
- La base resultante contiene *N registros y M columnas*.