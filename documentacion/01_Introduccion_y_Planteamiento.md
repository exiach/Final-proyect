# CAPÍTULO 1: INTRODUCCIÓN Y PLANTEAMIENTO DEL PROBLEMA

## 1.1 Antecedentes del Estudio

El rendimiento académico en la educación primaria constituye un indicador determinante para la evaluación de la calidad educativa, el desarrollo cognitivo socioemocional y la prevención del abandono o la deserción escolar temprana (De-La-Peña & Luque-Rojas, 2021). A nivel internacional y regional, los avances en las Tecnologías de la Información y la Comunicación (TIC) han propiciado el surgimiento de campos multidisciplinarios como la Minería de Datos Educativos (*Educational Data Mining* - EDM) y la Analítica del Aprendizaje (*Learning Analytics* - LA), cuyo propósito fundamental es la transformación de grandes volúmenes de datos institucionales históricos en información accionable para la toma de decisiones pedagógicas (Romero & Ventura, 2020).

En el contexto del Sistema Educativo Plurinacional de Bolivia, el currículo de Educación Primaria Comunitaria Vocacional —regulado por la Ley de Educación N.º 070 "Avelino Siñani - Elizardo Pérez" y el Reglamento de Evaluación del Desarrollo Curricular (Ministerio de Educación del Estado Plurinacional de Bolivia, 2021)— establece un enfoque de evaluación cuali-cuantitativo orientado a la formación integral en las dimensiones del *Ser, Saber, Hacer y Decidir*. Sin embargo, el seguimiento continuo de los estudiantes a menudo se ve dificultado por la fragmentación de la información académica, la cual suele almacenarse en boletines centralizadores impresos o planillas aisladas de hojas de cálculo por gestión escolar.

En la Unidad Educativa José María Santiváñez, ubicada en el departamento de Cochabamba, el registro del desempeño estudiantil ha dependido históricamente de evaluaciones periódicas almacenadas en documentos en formato PDF y hojas Excel independientes por curso y paralelo. Esta dispersión de datos genera una barrera operativa para la detección oportuna de los estudiantes que presentan un rezago académico persistente, es decir, aquellos alumnos que incurren en la reprobación de una o más asignaturas curriculares o cuyos promedios acumulados se sitúan en niveles de vulnerabilidad académica (nota inferior a 51 puntos sobre 100).

Frente a este escenario, la implementación de Sistemas de Alerta Temprana (*Early Warning Systems* - EWS) impulsados por modelos predictivos de Aprendizaje Automático (*Machine Learning* - ML) surge como una solución tecnológica estratégica (Aguiar & Morales, 2021; Macfadyen & Dawson, 2010). Al analizar patrones históricos multi-años y multi-cursos, estos sistemas permiten anticipar con un margen de tiempo suficiente las dificultades de aprendizaje, otorgando a los equipos directivos y docentes una herramienta científica de apoyo a la decisión que complementa el criterio pedagógico en el aula.

---

## 1.2 Planteamiento del Problema

El rezago académico en la educación primaria rara vez ocurre de manera intempestiva; por el contrario, es el resultado de un proceso acumulativo de deficiencias no detectadas en competencias clave como la lectura, escritura, razonamiento lógico-matemático y comprensión de entorno natural y social. En la U.E. José María Santiváñez, la falta de una plataforma analítica centralizada impide consolidar y correlacionar la trayectoria escolar de los estudiantes a lo largo de los diferentes grados (1.º a 6.º de primaria) y gestiones académicas.

La problemática central se sintetiza en las siguientes condiciones observadas:
1. **Dispersión y Desestructuración de la Información**: Los datos académicos históricos (2021-2024) se encontraban fragmentados en 36 archivos independientes en formatos PDF convertidos a Excel, con variaciones en las estructuras de columnas, formatos de nombres y códigos RUDE, dificultando el seguimiento longitudinal del alumno.
2. **Identificación Tardía del Riesgo**: Las evaluaciones convencionales identifican la reprobación al finalizar el bimestre o la gestión escolar, cuando las posibilidades de aplicar medidas remediales efectivas son reducidas, incrementando el riesgo de repetición de curso o rezago en años posteriores.
3. **Falta de Priorización en Materias Críticas**: No se contaba con un estudio empírico cuantitativo que determinara científicamente cuáles asignaturas representan los principales factores de riesgo en el nivel primario (e.g., *Comunicación y Lenguajes* frente a *Matemática*).
4. **Ausencia de Herramientas Digitales de Apoyo Pedagógico**: Los docentes no disponían de un tablero de control dinámico (*dashboard*) capaz de proyectar alertas tempranas, simular escenarios académicos hipotéticos y clasificar de forma automatizada a la nómina de estudiantes según su nivel de vulnerabilidad.

### 1.2.1 Formulación de Preguntas de Investigación
Para orientar el desarrollo de la presente investigación, se plantean las siguientes interrogantes:
- **Pregunta General**: ¿Cómo predecir el rezago académico en estudiantes de educación primaria de la U.E. José María Santiváñez mediante el análisis de datos históricos multi-años y multi-cursos utilizando técnicas de Machine Learning para respaldar la toma de decisiones pedagógicas docentes?
- **Preguntas Específicas**:
  1. ¿De qué manera se pueden recolectar, estructurar y depurar los datos académicos dispersos de las gestiones 2021 a 2024 para garantizar un dataset consistente y de calidad?
  2. ¿Cuáles son los patrones de rezago académico y qué asignaturas presentan las mayores tasas de reprobación en el nivel primario de la U.E. José María Santiváñez?
  3. ¿Qué algoritmos de Machine Learning (Árboles de Decisión, Random Forest, Redes Neuronales MLP) presentan la mayor eficacia predictiva al procesar características históricas del desempeño estudiantil?
  4. ¿Cómo clasificar a los estudiantes en niveles de riesgo diferenciados (Alto, Medio, Bajo) para orientar planes de intervención pedagógica oportuna?
  5. ¿De qué forma diseñar e implementar un prototipo interactivo de apoyo a la decisión docente que incorpore alertas tempranas y simulaciones de rendimiento académico?

---

## 1.3 Justificación

### 1.3.1 Justificación Institucional y Social
La educación primaria sienta las bases del desarrollo intelectual y personal de los niños. Prevenir el rezago académico en la U.E. José María Santiváñez contribuye directamente a la equidad educativa, asegurando que todos los estudiantes reciban la atención pedagógica necesaria para culminar exitosamente el ciclo de escolaridad. Institucionalmente, fortalece la gestión educativa basada en evidencias empíricas y optimiza los recursos de apoyo pedagógico.

### 1.3.2 Justificación Pedagógica
El sistema propuesto no pretende sustituir la evaluación cualitativa ni la sensibilidad del maestro en el aula. Por el contrario, se concibe como una **herramienta de apoyo a la decisión pedagógica**. Al proveer alertas tempranas fundadas en patrones estadísticos e históricos, el docente cuenta con un insumo previo para focalizar la tutoría individualizada, coordinar acciones con la comisión pedagógica y los padres de familia, y ajustar las estrategias didácticas antes de que la reprobación se concrete.

### 1.3.3 Justificación Tecnológica
Desde la perspectiva de las Ciencias de la Computación y la Minería de Datos Educativos, este proyecto demuestra la factibilidad de aplicar algoritmos supervisados de Machine Learning (como *Random Forest* con balanceo de clases y *Perceptrones Multicapa*) sobre conjuntos de datos del contexto escolar boliviano. Asimismo, la integración de una Capa Híbrida de Resguardo Pedagógico Normativo garantiza la validez ética y operativa de las predicciones, cerrando la brecha entre los modelos matemáticos teóricos y la práctica docente cotidiana a través de una interfaz moderna construida en *Streamlit*.

---

## 1.4 Objetivos del Proyecto

### 1.4.1 Objetivo General
Desarrollar un modelo de predicción del rezago académico en estudiantes de educación primaria utilizando datos multi-años y multi-cursos, con el fin de anticipar dificultades de aprendizaje y apoyar a los docentes en la toma de decisiones pedagógicas en la U.E. José María Santiváñez.

### 1.4.2 Objetivos Específicos
1. Recolectar y depurar datos académicos históricos de alumnos de varios cursos y gestiones (2021-2024), consolidando una estructura de datos estandarizada.
2. Analizar los datos para identificar patrones de rezago académico y factores asociados, como la determinación empírica de materias críticas de reprobación.
3. Diseñar y entrenar modelos predictivos de Machine Learning (Árboles de Decisión, Random Forest y Redes Neuronales MLP) para anticipar alumnos en riesgo.
4. Evaluar los modelos propuestos y segregar a los estudiantes en grupos de riesgo (Alto, Medio y Bajo) para facilitar planes de apoyo pedagógico diferenciado.
5. Proponer un prototipo de apoyo a la decisión docente que integre alertas tempranas, fichas individuales y simuladores de rendimiento académico para el seguimiento de los alumnos.

---

## 1.5 Alcance y Delimitación

- **Delimitación Geográfica e Institucional**: El estudio se realiza exclusivamente en la Unidad Educativa José María Santiváñez, situada en la ciudad de Cochabamba, Bolivia.
- **Delimitación Poblacional y Temporal**: Comprende la nómina histórica de estudiantes del nivel de Educación Primaria Comunitaria Vocacional (grados 1.º a 6.º de primaria, paralelos A y B) correspondiente a las gestiones escolares 2021, 2022, 2023 y 2024, alcanzando un total consolidado de **1,118 observaciones estudiantil-año**.
- **Delimitación Temática y Tecnológica**: La investigación abarca la minería de datos educativos, el procesamiento de tablas con *pandas*, la clasificación supervisada con *scikit-learn*, la serialización de modelos con *joblib* y el desarrollo de un prototipo web de interfaz docente mediante el marco de trabajo *Streamlit*. No incluye la implementación en nivel secundario ni la automatización de la firma digital de boletines oficiales.
