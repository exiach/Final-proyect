# CAPÍTULO 3: MARCO METODOLÓGICO

Esta sección describe procedimental y técnicamente cómo se desarrolló el proyecto, abarcando desde la concepción del área de estudio hasta la implementación de algoritmos de *Machine Learning* y construcción de la interfaz.

## 3.1 Área de Estudio

El área de estudio se centra en el departamento de Cochabamba, específicamente en una unidad educativa del nivel primario [INSERTE NOMBRE DE LA ESCUELA, ej: ubicada en la zona Sud/Norte de la ciudad]. La institución cuenta con paralelos "A" y "B" desde el primer hasta el sexto curso de primaria. La población objetivo para el análisis de este proyecto comprende a los estudiantes matriculados y evaluados en las gestiones 2022, 2023 y 2024.

*(INSERTE AQUÍ: Figura 3-1: Mapa o fotografía de fachada que ayude a ubicar el área de estudio del colegio. Incluir fuente).*

## 3.2 Flujograma Metodológico

El proyecto de predicción de rezago escolar se estructuró operativamente bajo un enfoque cuantitativo y secuencial referenciado en fases de Ciencia de Datos:

1. **Recopilación y Extracción de Datos:** Obtención de boletines históricos (PDF).
2. **Transformación y Limpieza (ETL):** Conversión a Excel e ingesta en Python (Pandas) para tratar valores nulos y estandarizar nombres.
3. **Análisis Exploratorio y Creación de Atributos:** Cálculo de variables predictoras derivadas (Ej: Promedio anterior, número de reprobadas previas).
4. **Modelado y Entrenamiento (Machine Learning):** Separación en conjuntos de entrenamiento y prueba para Decision Trees, Random Forest y MLP.
5. **Evaluación Comparativa de Modelos:** Medición matemática del rendimiento usando matrices de confusión sobre datos reales.
6. **Implementación del Prototipo (Despliegue):** Diseño de la herramienta gráfica de apoyo docente utilizando la librería Streamlit y los modelos exportados.

*(A CONTINUACIÓN, UNA EXPLICACIÓN TEXTUAL QUE PUEDES CAMBIAR POR UN GRÁFICO O DIBUJARLA EN WORD CON FORMAS)*:

*   **Paso 1:** Extraer archivos RUDE/PDF -> **Paso 2:** Limpiar y Filtrar (Pandas) -> **Paso 3:** Analizar Patrones (EDA) -> **Paso 4:** Entrenar Modelos (RF, MLP) -> **Paso 5:** Desplegar Dashboard (Streamlit).

*(INSERTE AQUÍ: Figura 3-2: Flujograma metodológico dibujado con flechas o bloques)*

## 3.3 Fuentes de la Información

### 3.3.1 Datos Primarios (Generados y Procesados)
La información utilizada consolida los registros de rendimiento académico bimensual y general de los estudiantes.
- **Formato Origen:** Los datos base fueron recolectados en formato PDF, directamente de los centralizadores oficiales (RUDE) de los años 2022 a 2024 proporcionados por la administración educativa.
- **Formato Intermedio:** Para propósitos de carga, los PDF fueron transformados tabularmente a formato `.xlsx` (Excel), particionados en carpetas por gestión (Ej: `/01_Datos_Originales_PDF/Gestion_2022/`).
- **Dataset de Análisis (CSV):** Tras el procesamiento algorítmico, se unificó la información en un repositorio central estandarizado denominado `primaria_dataset.csv`.

*(INSERTE AQUÍ: Figura 3-3: Captura de pantalla de cómo se ve el Excel o una tabla RUDE difuminada para proteger identidad)*

### 3.3.2 Requerimiento y Selección de Variables
De los boletines completos, se delimitaron 9 atributos cuantitativos numéricos clave correspondientes a las asignaturas de tronco común establecidas por la malla curricular primaria: Comunicación y Lenguajes, Ciencias Sociales, Educación Física, Educación Musical, Artes Plásticas, Matemáticas, Técnica Tecnológica, Ciencias Naturales y Valores - Espiritualidad. Se integraron como metadatos de clasificación las variables categóricas: Gestión (Ej: 2022), Año de Escolaridad (Primero a Sexto) y Paralelo (A, B).

## 3.4 Fases Estructurales de Implementación Tecnológica

### 3.4.1 Etapa 1: Recolección y Depuración ETL (Obj. 1)
La limpieza y tratamiento del dataset se ejecutó en código Python nativo a través del entorno de desarrollo tipo Jupyter Notebook (`Obj1_Recoleccion_Limpieza.ipynb`). 

**Herramientas Utilizadas:** Librería matemática `pandas`, motor de lectura `openpyxl`.
**Procedimiento y Parámetros:**
1. **Extracción Estructural:** El script desarrolló heurísticas de escaneo para detectar metadatos flotantes en las cabeceras de los archivos Excel brutos (fila 0: Gestión, fila 1: Año Escolaridad / Paralelo) inyectándolos dinámicamente en el Dataframe de limpieza.
2. **Normalización de Formato y Caracteres:** Se renombraron las cabeceras automatizadas del sistema oficial que mapeaban celdas genéricas ("pa", "pa.1") hacia nombres funcionales ("com_lenguajes", "cs_sociales"). A su vez, se eliminaron caracteres especiales, saltos de línea tildes.
3. **Tratamiento Nulos/Drop:** Toda fila que no presentó registro válido en la columna `RUDE` (indicando filas vacías o de relleno en Excel) fue erradicada del conjunto de entrenamiento base usando el método `.dropna()`.
4. **Calculo de Resumen Algorítmico:** En esta fase se gestó por operación condicional aritmética la clase fundamental `rezago` (Label Y / Target) identificando a los registros donde existiría al menos 1 condición de nota `< 51` sobre todas las materias cardinales. En paralelo se calculó el sumatorio derivado de características (Features) como "promedio_general" y "num_materias_reprobadas".

### 3.4.2 Etapa 2: Análisis Exploratorio Multianual (Obj. 2)
Una vez almacenado el archivo `primaria_dataset.csv`, se estructuraron scripts analíticos gráficos (`Obj2a_Analisis_Patrones.ipynb`).
**Herramientas Utilizadas:** Entorno Jupyter, `matplotlib.pyplot` y rutinas `pandas`.
**Procedimiento:** 
El descubrimiento de la información se dividió enfocándose en patrones comparativos. Se calcularon medias agregadas y descriptivas de proporciones entre variables de reprobación multianual.
A través de diagramas (Boxplots y gráficos de líneas o dispersión temporal por "Gestión"), el código extrajo perfiles específicos de la distribución histórica. Se evidenció un comportamiento comparativo bivariado evaluando la diferencia de la media estadística entre estudiantes etiquetados con la bandera "rezago=1" (estudiantes en rezago) frente a las distribuciones de aquellos estables ("rezago=0"), tanto en cantidad de materias reprobadas como en variabilidad del promedio general.

*(INSERTE AQUÍ: Figura 3-4: Una de las gráficas de Barras o un BoxPlot del EDA extraídas de tu libreta Obj2a)*
