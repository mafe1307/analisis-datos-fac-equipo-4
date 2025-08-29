# Reporte Estudiante C - Calidad de Datos

## 1. Columnas con más datos faltantes

Durante la revisión de la base de datos original *JEFAB_2024.xlsx* se identificaron los siguientes problemas de calidad:

- *Datos faltantes:*
  - Variables con más del 50% de vacíos:  
    - NUMERO_PERSONAS_APORTE_SOSTENIMIENTO2 (61.2%)  
    - NUMERO_HABITAN_VIVIENDA2 (59.3%)  
    - NUMERO_HIJOS (50.1%)   
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

## 1. Distribución de la Edad
El rango de edad más común se ubica en **[30–35 años]**, lo que refleja una base poblacional **joven-adulta**.  
La mediana cercana al promedio indica una distribución equilibrada, con un descenso progresivo en los grupos etarios mayores.  
<img width="990" height="590" alt="Distribucion de edades del personal FAC" src="https://github.com/user-attachments/assets/6d603bf7-f1b0-4df0-a624-dae0b88e36fb" />


## 2. Distribución por Género
Predomina el **género masculino (69.59%)**, frente al **femenino (30.41%)**.  
Aunque la diferencia es marcada, se observa una participación creciente de mujeres, lo cual apunta a un avance en la **inclusión y diversidad de género** en la institución.  
<img width="690" height="490" alt="dISTRIBUCION GENERO" src="https://github.com/user-attachments/assets/205437c1-f4c3-4633-a824-a2da820e1632" />

## 3. Grado Militar
Al considerar todas las respuestas, destaca un número importante de **“No responde” (30%)**.  
Excluyéndolos, el grado más frecuente corresponde a **T3**, lo que evidencia la mayor concentración de personal en ese nivel jerárquico.  


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
