# CAPÍTULO 2: MARCO TEÓRICO

El presente capítulo desarrolla los sustentos teóricos y conceptuales que fundamentan la investigación. Se abordan las disciplinas centrales del proyecto, comenzando por la Analítica de Datos Educativos, transitando por las metodologías de procesamiento de datos, hasta llegar a los algoritmos específicos de Aprendizaje Automático implementados para la predicción del rezago escolar.

## 2.1 Minería de Datos Educativos (Educational Data Mining - EDM)

A medida que las instituciones educativas digitalizan sus procesos administrativos y académicos, se generan volúmenes masivos de información. La Minería de Datos Educativos (EDM, por sus siglas en inglés) surge como un campo de investigación multidisciplinar cuyo objetivo es desarrollar, investigar y aplicar métodos computacionales para explorar los datos originados en contextos educativos (Romero & Ventura, 2020). 

Según Baker e Inventado (2014), la EDM se diferencia de la minería de datos tradicional debido a la naturaleza jerárquica y longitudinal de los datos escolares (estudiantes agrupados en paralelos, inmersos en cursos, evaluados a lo largo de múltiples gestiones). Su propósito principal es "entender cómo aprenden los estudiantes y los entornos en los que lo hacen". En el contexto de este proyecto, la EDM proporciona el marco teórico para transformar hojas de cálculo pasivas (como los registros del RUDE) en activos estratégicos. Al aplicar técnicas de descubrimiento de conocimiento en bases de datos (KDD), se busca predecir el comportamiento futuro del alumno —específicamente el riesgo de rezago— basándose en su trayectoria pasada, posibilitando así las intervenciones tempranas (Cardoso et al., 2021).

## 2.2 Proceso de Descubrimiento de Conocimiento (Metodología de Datos)

Para que los algoritmos de inteligencia artificial funcionen correctamente, los datos crudos deben someterse a un riguroso proceso de tratamiento. Este proyecto se alinea con las fases estándar de la minería de datos:

### 2.2.1 Extracción, Transformación y Carga (ETL)
El proceso ETL es la piedra angular de cualquier sistema analítico. Consiste en la Extracción de datos desde múltiples fuentes (en este caso, boletines en formato PDF o Excel), la Transformación de los mismos para asegurar su calidad (homogeneización de materias, tratamiento de valores nulos o atípicos) y la Carga en un repositorio central estructurado (Dataset) (Han, Kamber & Pei, 2011). Sin una limpieza adecuada, los modelos predictivos heredarían los sesgos y errores de los registros manuales ("basura entra, basura sale").

### 2.2.2 Estandarización y Escalado de Variables
En el aprendizaje automático, las variables (características) suelen tener diferentes unidades y magnitudes. Por ejemplo, el "Promedio General" de un alumno fluctúa entre 0 y 100, mientras que el "Número de Materias Reprobadas" fluctúa entre 0 y 9. Algoritmos matemáticamente sensibles, como las Redes Neuronales, requieren que todas las entradas tengan una escala comparable para converger correctamente. La estandarización, implementada típicamente restando la media y dividiendo por la desviación estándar a través de herramientas como *StandardScaler*, reescala los datos para que tengan una distribución normal estándar, optimizando así el entrenamiento del modelo (Hastie, Tibshirani & Friedman, 2008).

### 2.2.3 Balanceo de Clases
En la predicción del rezago escolar, es natural encontrar un conjunto de datos desbalanceado: afortunadamente, la mayoría de los estudiantes aprueban, mientras que una minoría presenta rezago. Si un modelo se entrena con esta disparidad sin ajustes, tenderá a predecir siempre "aprobado" para maximizar su precisión global, fallando de manera crítica en la detección temprana del alumno en riesgo. Para mitigar esto, se utilizan técnicas algorítmicas como el ajuste de pesos de clase (*class weights*), que penalizan fuertemente al modelo cuando se equivoca al clasificar a la clase minoritaria (rezago), obligándolo a prestarle la debida atención (Breiman, 2001).
