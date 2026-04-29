# CAPÍTULO 5: CONCLUSIONES

A partir del desarrollo, implementación y evaluación de las herramientas tecnológicas y los modelos predictivos en el presente proyecto, se establecen las siguientes conclusiones fundamentales respaldadas por la evidencia extraída:

**1. Viabilidad de la Transformación de Datos Institucionales (RUDE)**
Se demostró la factibilidad de transformar repositorios estáticos (boletines en PDF) en activos estratégicos. El proceso ETL (Extracción, Transformación y Carga) erradicó la "ceguera de datos" en la institución, consolidando un dataset estructurado y sentando las bases tecnológicas para modernizar su gestión.

**2. Identificación de Predictores Críticos de Riesgo**
El Análisis Exploratorio de Datos (EDA) comprobó que el desempeño global académico del año anterior mantiene una correlación inversa profunda con el atraso escolar. Además, se evidenció que Matemáticas y Lenguaje actúan como puntos críticos fundacionales, concentrando más del 65% de las reprobaciones tempranas.

**3. Superioridad del Bosque Aleatorio en Entornos Educativos**
Tras evaluar Árboles de Decisión, Bosques Aleatorios y Redes Neuronales, se concluye que el *Random Forest* —con penalización de clase balanceada— representa la solución óptima. Este algoritmo superó el desbalance natural de clases (alto índice de aprobados vs pocos reprobados) brindando el desempeño predictivo más robusto.

**4. Priorización Pedagógica de la Sensibilidad (Recall)**
Dentro de un sistema de alerta temprana escolar, métricas orientadas a detectar anomalías como el *Recall* (Sensibilidad) son operativamente superiores a la Exactitud Global (*Accuracy*). Maximizar esta métrica aseguró la intercepción de estudiantes verdaderamente vulnerables; asumiendo técnica y pedagógicamente que es preferible tolerar falsos positivos antes que omitir matemáticamente a un alumno necesitado.

**5. Equilibrio entre Capacidad Predictiva e Interpretabilidad**
La elección del Bosque Aleatorio frente a las Redes Neuronales (Deep Learning) se fundamenta en su explicabilidad. En educación primaria, es vital que las predicciones funcionen como una "caja blanca", permitiendo a docentes y directores comprender los umbrales de decisión para justificar plenamente sus intervenciones pedagógicas.

**6. Transición hacia una Gestión Pedagógica Preventiva**
La integración de Minería de Datos y Machine Learning demostró que es posible anticipar el fracaso antes de que el daño sea irreversible. La institución evoluciona así de un modelo reactivo (actuar frente al boletín final) a un ecosistema de gestión escolar predictivo y altamente proactivo.
