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
<img width="1800" height="900" alt="A_grado_militar_hist" src="https://github.com/user-attachments/assets/e233786d-60d9-4ef2-aea3-6683dd666c92" />

## 4. Análisis de la Distribución de Género por Grado Militar

Grados más altos:
AT (100% hombres, 0% mujeres): Este es un grado donde solo los hombres están representados. La gráfica indica que no hay mujeres en este grado en la FAC.

T3, T2, T1: La gran mayoría de estos grados también están dominados por hombres (cerca del 70-90% de representación masculina). Esto muestra que los grados más bajos y medios son predominantemente masculinos.

Grados con mayor participación femenina:

Grados superiores (TS, TJC): Aquí, las mujeres tienen una mayor representación, más del 35% en TS y 6.9% en TJC. Esto sugiere que las mujeres están comenzando a ocupar roles más altos, aunque aún es una minoría.

Grados intermedios (CT, T4, TE, ST):

En estos grados, la representación de mujeres varía entre el 25-40%, lo que refleja una mayor inclusión de mujeres en rangos intermedios.

<img width="1500" height="900" alt="B_grado_genero_heatmap" src="https://github.com/user-attachments/assets/3c38f601-9015-4437-bdb7-f09193cd583b" />


## 5. Análisis de la Distribución por Edad y Estrato
  
Estratos medios (3 y 4) concentran la mayor parte de la población en los rangos de edad media-adulta (~25-45 años).

Estrato 5 tiene una presencia reducida en los rangos jóvenes, pero se eleva en las edades más altas (~50-60 años).

Estrato 1 y 2 tienen una mayor representación en los rangos de edad más jóvenes.

<img width="1500" height="900" alt="B_heatmap_edad_estrato" src="https://github.com/user-attachments/assets/de872b85-fb9c-431d-b3fd-fe964081992e" />


# Reporte Estudiante B - Análisis Familiar

# Introducción

Este informe corresponde al trabajo del **Estudiante B** (especialista en datos familiares).  
Incluye el análisis de **estado civil**, **hijos**, **convivencia** y los **patrones cruzados** solicitados.  
Se agregan también las respuestas a las preguntas guía.  

# Estado Civil

Predomina la población **casada con un 60,4%**, lo que refleja un fuerte componente familiar en la **fac**.  
Los **solteros** son el segundo grupo más grande con un **32,7%**.  
El grupo con menos cantidad de personas son los **viudos**.  

<img width="790" height="489" alt="edad segun estado civil" src="https://github.com/user-attachments/assets/df801e36-38e2-40a9-a4fe-a9e61c680c60" />

# Hijos

Más de la mitad del personal ya tiene hijos (**57,1%**),  
lo cual resalta la importancia de políticas de bienestar dirigidas a familias con responsabilidades de crianza.  

<img width="590" height="390" alt="Tienen hijos" src="https://github.com/user-attachments/assets/dcd1f7d4-0ba7-4da1-a13b-df8ceccb099b" />

# Convivencia Familiar

Aunque la mayoría tiene hijos, pocos viven con ellos;  
esto puede deberse a dinámicas propias de la vida militar, traslados o asignaciones en diferentes bases.  
<img width="590" height="390" alt="image" src="https://github.com/user-attachments/assets/63f02314-d04e-422a-86bd-26d03d23234f" />

# Edad y Estado Civil

Existe una clara relación: los **solteros** son mucho más jóvenes,  
mientras que los **viudos** y **separados** son los de mayor edad promedio.  

<img width="630" height="455" alt="edad segun estado civil 2" src="https://github.com/user-attachments/assets/8f2ba608-d824-43da-9654-1590a68f41be" />

# Respuestas a Preguntas

1. ¿Qué porcentaje del personal está casado? → **60,4%**  
2. En total en la **fac** **3.669 personas** tienen hijos (**57,1%**) y solo el **15,0%** convive con ellos.  
3. Se observa que la relación entre edad y estado civil es que los **solteros** son más jóvenes,  
   los **casados** están en etapa media y los **viudos** en edades mayores.  

# Patrones cruzados

## A. Estado civil × Hijos

- **Casados/as**: 76,9% tienen hijos y 23,1% no.  
- **Solteros/as**: 14,7% tienen hijos y 85,3% no.  
- **Viudos/as**: 92,3% tienen hijos y 7,7% no.  
- **Separados/as**: 88,2% tienen hijos.  

Las personas **viudas** presentan el porcentaje más alto de quienes tienen hijos (**92,3%**).  
En segundo lugar se encuentran las personas **separadas** (**88,2%**) y luego los **casados** (**76,9%**).  
Por otro lado, los **solteros** tienen la proporción más baja (**14,7%**).  

## B. Hijos × Convivencia

Del total de personas que reportaron tener hijos, se evidencia una marcada diferencia en los patrones de convivencia.  
En concreto, el **85,0%** de quienes son padres o madres **no viven con sus hijos**, mientras que únicamente el **15,0%** sí convive de manera habitual con ellos.  

## C. Edad × Estado civil

- **Solteros/as**: 30,2 años  
- **Casados/as**: 39,7 años  
- **Divorciados/as**: 40,4 años  
- **Separados/as**: 40,9 años  
- **Viudos/as**: 47,6 años  

Estos resultados reflejan una clara relación entre la edad y la situación conyugal dentro del personal analizado.  

## D. Estrato × Hijos

- **Estrato 1**: 61,9% con hijos, 38,1% sin hijos.  
- **Estrato 2**: 52,6% con hijos, 47,4% sin hijos.  
- **Estrato 3**: 58,9% con hijos, 41,1% sin hijos.  
- **Estrato 4**: 55,6% con hijos, 44,4% sin hijos.  
- **Estrato 5**: 62,7% con hijos, 37,3% sin hijos.  
- **Estrato 6**: 42,3% con hijos, 57,7% sin hijos.
  
<img width="573" height="390" alt="Porcentaje de hijos segun estrato socioeconomico" src="https://github.com/user-attachments/assets/994ded95-50c4-4396-822f-13f4288724c9" />

En la mayoría de los estratos (1 a 5) predominan las personas con hijos, con valores entre el 52% y el 63%.  
El único caso contrario es el estrato 6, donde la mayoría no tiene hijos (57,7%).  
Esto sugiere que en niveles socioeconómicos altos la presencia de hijos es menos frecuente en comparación con los demás estratos.  

## E. Estrato × Estado civil

- **Estrato 1**: 40,1% solteros, 52,3% casados, 3,0% separados, 3,0% divorciados, 1,5% viudos.  
- **Estrato 2**: 41,3% solteros, 53,7% casados, 1,9% separados, 2,8% divorciados, 0,3% viudos.  
- **Estrato 3**: 29,2% solteros, 62,9% casados, 2,7% separados, 4,6% divorciados, 0,6% viudos.  
- **Estrato 4**: 27,3% solteros, 66,0% casados, 2,7% separados, 3,2% divorciados, 0,8% viudos.  
- **Estrato 5**: 18,2% solteros, 75,5% casados, 1,8% separados, 3,6% divorciados, 0,9% viudos.  
- **Estrato 6**: 26,9% solteros, 61,5% casados, 0,0% separados, 11,5% divorciados, 0,0% viudos.
  
<img width="748" height="489" alt="estado civil segun estrato socioeconomico" src="https://github.com/user-attachments/assets/9c8eafb1-2ac1-4a33-85bb-17b8a321c38e" />

En los estratos bajos (1 y 2) se observa una fuerte presencia de **solteros**, cercana al 40%.  
En los estratos medios y altos (3, 4 y 5) predomina claramente la población **casada**, que llega hasta un 75,5% en el estrato 5.  
En el estrato 6 se mantiene la mayoría casada (61,5%), pero se destaca un porcentaje más elevado de **divorciados (11,5%)**, ausente en los demás estratos.


## F. Vivienda propia × Hijos

- **Con vivienda propia**: 74.5% con hijos, 25.5% sin hijos.  
- **Sin vivienda propia**: 43.9% con hijos, 56.1% sin hijos.  

Entre quienes tienen hijos, es más común disponer de vivienda propia;  
en contraste, entre quienes no tienen hijos predomina la ausencia de propiedad.  

## G. Vivienda propia × Estado civil

- **Con vivienda propia**:  16.5% solteros, 75.5% casados, 2.7% separados, 4.3% divorciados, 1.0% viudos.  
- **Sin vivienda propia**: 44.6% solteros, 49.1% casados, 2.4% separados, 3.6% divorciados, 0.3% viudos.
  
<img width="748" height="489" alt="estado civil segun tenencia de vivienda" src="https://github.com/user-attachments/assets/fda1da11-34de-4c47-a8df-fe0e079164fd" />

La vivienda propia se concentra en **casados**, **separados** y **viudos**;  
entre los **solteros**, en cambio, predomina el no tener propiedad.  

## H. Género × Hijos × Convivencia

- **Hombres sin hijos**: 79,0% no conviven, 21,0% sí.  
- **Hombres con hijos**: 87,3% no conviven, 12,7% sí.  
- **Mujeres sin hijos**: 71,8% no conviven, 28,2% sí.  
- **Mujeres con hijos**: 80,1% no conviven, 19,9% sí.
  
<img width="690" height="489" alt="convivencia familiar segun sexo e hijos" src="https://github.com/user-attachments/assets/7b80209a-0988-461b-bb1d-4675a2acb639" />

En todos los casos, la convivencia con los hijos es baja, especialmente entre los **hombres**.  
Las **mujeres sin hijos** muestran una convivencia más alta con familia.  

# Conclusiones

El estudio sobre las familias demuestra que la mayoría de los integrantes de la **fuerza aérea colombiana** lleva una vida con un sólido componente familiar y de pareja.  
En términos de estado civil, predominan las personas **casadas (60,4%)**, seguidas por los **solteros (32,7%)**, mientras que los **viudos** son los que menos representan.  

En lo que respecta a la paternidad o maternidad, se encontró que **3.669 personas (57,1%)** son padres.  
Sin embargo, solo una pequeña parte convive con sus hijos (**15,0%**), frente al **85,0%** que no lo hace.  
Este hallazgo refleja las circunstancias particulares de la vida militar, que incluyen cambios de ubicación, asignaciones en diversas unidades y situaciones que dificultan la permanencia en el hogar.  

Los patrones cruzados refuerzan estos descubrimientos: los **viudos** son quienes más tienen hijos (**92,3%**), seguidos de los **separados (88,2%)** y los **casados (76,9%)**.  
Por el contrario, los **solteros** muestran un bajo nivel de paternidad (**14,7%**).  
Además, la convivencia con hijos se mantiene baja incluso entre quienes los tienen, lo que confirma la fragmentación familiar derivada de las obligaciones laborales.  

El análisis por **estrato** y **vivienda propia** aporta un matiz socioeconómico: la estabilidad patrimonial y el acceso a vivienda se relacionan con tener hijos y estar casado, mientras que los **solteros** y personas sin hijos predominan en contextos de menor consolidación económica.  

Finalmente, la dimensión de **género** muestra que, aunque tanto hombres como mujeres presentan bajos niveles de convivencia con sus hijos, las mujeres sin hijos tienden a convivir más en entornos familiares que los hombres.  

En síntesis, los hallazgos indican que la **vida militar condiciona fuertemente la convivencia familiar**.  
Aunque una gran parte del personal tiene hijos, **muy pocos conviven con ellos de manera habitual**, lo cual representa el resultado más crítico del estudio.  
Esta situación resalta la necesidad de considerar políticas de bienestar y apoyo familiar que permitan mitigar los efectos de las dinámicas laborales sobre la organización cotidiana de los hogares.
