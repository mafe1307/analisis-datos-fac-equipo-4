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

# "Reporte Estudiante B - Análisis Familiar"

## 1. Distribución de la Edad
El rango de edad más común se ubica en **[30–35 años]**, lo que refleja una base poblacional **joven-adulta**.  
La mediana cercana al promedio indica una distribución equilibrada, con un descenso progresivo en los grupos etarios mayores.  
<img width="990" height="590" alt="Distribucion de edades del personal FAC" src="https://github.com/user-attachments/assets/6d603bf7-f1b0-4df0-a624-dae0b88e36fb" />


## 2. Distribución por Género
Predomina el **género masculino (69.59%)**, frente al **femenino (30.41%)**.  
Aunque la diferencia es marcada, se observa una participación creciente de mujeres, lo cual apunta a un avance en la **inclusión y diversidad de género** en la institución.  
<img width="690" height="490" alt="dISTRIBUCION GENERO" src="https://github.com/user-attachments/assets/205437c1-f4c3-4633-a824-a2da820e1632" />

## 3. Grado Militar
El grado más frecuente corresponde a **T3**, lo que evidencia la mayor concentración de personal en ese nivel jerárquico.  

## 4. Análisis de la Distribución de Género por Grado Militar

Grados más altos:
AT (100% hombres, 0% mujeres): Este es un grado donde solo los hombres están representados. La gráfica indica que no hay mujeres en este grado en la FAC.

T3, T2, T1: La gran mayoría de estos grados también están dominados por hombres (cerca del 70-90% de representación masculina). Esto muestra que los grados más bajos y medios son predominantemente masculinos.

Grados con mayor participación femenina:

Grados superiores (TS, TJC): Aquí, las mujeres tienen una mayor representación, más del 35% en TS y 6.9% en TJC. Esto sugiere que las mujeres están comenzando a ocupar roles más altos, aunque aún es una minoría.

Grados intermedios (CT, T4, TE, ST):

En estos grados, la representación de mujeres varía entre el 25-40%, lo que refleja una mayor inclusión de mujeres en rangos intermedios.

## 5. Análisis de la Distribución por Edad y Estrato
  
Estratos medios (3 y 4) concentran la mayor parte de la población en los rangos de edad media-adulta (~25-45 años).

Estrato 5 tiene una presencia reducida en los rangos jóvenes, pero se eleva en las edades más altas (~50-60 años).

Estrato 1 y 2 tienen una mayor representación en los rangos de edad más jóvenes.


# "Reporte Estudiante B - Análisis Familiar"

# Introducción

Este informe corresponde al trabajo del Estudiante B (especialista en datos familiares). 
Incluye el análisis de estado civil, hijos, convivencia y los patrones cruzados solicitados. 
Se agregan también las respuestas a las preguntas guía. 

# Estado Civil

Predomina la población casada con un **60,4%**, lo que refleja un fuerte componente familiar en la FAC. 
Los solteros son el segundo grupo más grande con un **32,7%**. 
El grupo con menos cantidad de personas son los viudos. 
<img width="1040" height="650" alt="B_estado_civil_bar" src="https://github.com/user-attachments/assets/36ea9a32-29aa-4b65-86f8-e7a336fc004b" />

# Hijos

Más de la mitad del personal ya tiene hijos (**57,1%**), 
lo cual resalta la importancia de políticas de bienestar dirigidas a familias con responsabilidades de crianza.

# Convivencia Familiar

Aunque la mayoría tiene hijos, pocos viven con ellos; 
esto puede deberse a dinámicas propias de la vida militar, traslados o asignaciones en diferentes bases.

# Edad y Estado Civil

Existe una clara relación: los solteros son mucho más jóvenes, 
mientras que los viudos y separados son los de mayor edad promedio.

# Respuestas a Preguntas

1. ¿Qué porcentaje del personal está casado? → **85%**  
2. En total en la FAC **3669 personas** tienen hijos (57,1%) y solo el **30%** convive con ellos.  
3. Se observa que la relación entre edad y estado civil es que los solteros son más jóvenes, 
   los casados están en etapa media y los viudos en edades mayores.

# Patrones cruzados

## A. Estado civil × Hijos

Dentro de cada estado civil, el porcentaje de quienes tienen o no tienen hijos es el siguiente:

- **Casados/as**: 76,9% tienen hijos y 23,1% no.  
- **Solteros/as**: 14,7% tienen hijos y 85,3% no.  
- **Viudos/as**: 92,3% tienen hijos y 7,7% no.  
- **Separados/as**: 88,2% tienen hijos.
<img width="630" height="455" alt="edad segun estado civil" src="https://github.com/user-attachments/assets/b0087c4a-de16-4d74-8982-786b3a4cf1eb" />
 

**Observación:**  
Las personas viudas presentan el porcentaje más alto de quienes tienen hijos (**92,3%**). 
En segundo lugar se encuentran las personas separadas (**88,2%**) y luego los casados (**76,9%**). 
Por otro lado, los solteros tienen la proporción más baja, ya que solo el **14,7%** tiene hijos.

## B. Hijos × Convivencia

Del total de personas que reportaron tener hijos, se evidencia una marcada diferencia en los patrones de convivencia.  
En concreto, el **85,0%** de quienes son padres o madres no viven con sus hijos, mientras que únicamente el **15,0%** sí convive de manera habitual con ellos.

## C. Edad × Estado civil

El análisis de la edad promedio según el estado civil muestra diferencias marcadas entre los grupos:

- **Solteros/as**: 30,2 años  
- **Casados/as**: 39,7 años  
- **Divorciados/as**: 40,4 años  
- **Separados/as**: 40,9 años  
- **Viudos/as**: 47,6 años  

Estos resultados reflejan una clara relación entre la edad y la situación conyugal dentro del personal analizado.

# Conclusiones

El estudio sobre las familias demuestra que la mayoría de los integrantes de la Fuerza Aérea Colombiana lleva una vida con un sólido componente familiar y de pareja. 
En términos de estado civil, predominan las personas casadas (60,4%), seguidas por los solteros (32,7%), mientras que los viudos son los que menos representan.  

En lo que respecta a la paternidad o maternidad, se encontró que **3.669 personas (57,1%)** son padres. 
Sin embargo, solo una pequeña parte convive con sus hijos (**15,0%**), frente al 85,0% que no lo hace. 
Este hallazgo refleja las circunstancias particulares de la vida militar, que incluyen cambios de ubicación, asignaciones en diversas unidades y situaciones que complican la permanencia en el hogar.  

Los patrones cruzados refuerzan estos descubrimientos: los viudos son quienes más tienen hijos (92,3%), 
seguido de los separados (88,2%) y los casados (76,9%). 
Por el contrario, los solteros muestran un bajo nivel de paternidad (14,7%). 
Además, la convivencia con hijos se mantiene baja incluso entre quienes los tienen, lo que confirma la fragmentación familiar derivada de las obligaciones laborales.  

Por último, la edad promedio se asocia de forma clara al estado civil: los solteros son los más jóvenes (30,2 años), 
los casados y divorciados están alrededor de los 40 años y los viudos alcanzan la media más alta (47,6 años). 
Esto refleja el curso natural de la vida y confirma que el paso del tiempo está vinculado a cambios en la situación matrimonial.  

**En conclusión**, los hallazgos indican que, aunque una gran parte del personal tiene familias, 
las dinámicas laborales propias de la FAC afectan de manera directa la convivencia cotidiana y la organización de los hogares. 
Este panorama subraya la necesidad de fortalecer políticas de bienestar que beneficien no solo a la persona, sino también a su núcleo familiar.
