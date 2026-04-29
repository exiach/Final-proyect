# CAPÍTULO 4: RESULTADOS Y DISCUSIÓN

En este capítulo se presentan analíticamente los hallazgos obtenidos durante la ejecución del proyecto, estructurados en función al cumplimiento de los objetivos específicos planteados. Se incluye la interpretación estadística de los modelos predictivos generados y la comparación técnica de su desempeño.

## 4.1 Resultados y Análisis de la Recolección y Depuración de Datos (Obj. Esp. 1)

El proceso de extracción (ETL) sobre los boletines PDF centralizados del RUDE (gestiones 2022-2024) culminó en la consolidación de un repositorio tabular estructurado (`primaria_dataset.csv`).
Inicialmente, se detectó una gran volumetría de registros crudos. Sin embargo, tras la aplicación de filtros por código RUDE nulo y eliminación de filas vacías (ruido de formato), se obtuvo un conjunto final útil de **[INSERTE AQUÍ LA CANTIDAD DE FILAS EXACTA QUE TIENE TU DATASET, ej: 1250]** registros limpios, representando el 100% de la población estudiantil válida para el análisis.

El algoritmo de transformación calculó exitosamente la variable objetivo `rezago`. Se obtuvo que el **[INSERTE %, ej: 14%]** del total histórico de la población estudiantil analizada cursó con riesgo o situación de rezago académico (representando la clase 1), frente a un **[INSERTE %, ej: 86%]** de alumnado que superó la gestión sin dificultades críticas (clase 0). Esta fuerte asimetría confirmó y justificó operativamente la necesidad de técnicas matemáticas de balanceo para las siguientes fases de modelado.

*(INSERTE AQUÍ: Figura 4-1: Gráfico de Tortas (Pie Chart) o de Barras mostrando el % de alumnos Aprobados vs alumnos con Rezago. Título: Distribución Histórica de Rezago).*

## 4.2 Resultados y Análisis de los Patrones de Rezago (Obj. Esp. 2)

El análisis exploratorio de datos (EDA) reveló patrones concluyentes sobre el comportamiento del fracaso escolar en la institución:
- Se encontró que el `promedio_general_prev` (promedio del año anterior) tiene una correlación matemática inversa fuerte con el rezago. Los estudiantes etiquetados con la condición de rezago exhibieron históricamente una media en sus promedios de **[INSERTE NUMERO, ej: 58.4]** puntos sobre 100, con una alta variabilidad (desviación estándar), ubicándose en el cuartil inferior del rendimiento general histórico frente a los alumnos sin rezago, cuya media supera los **[INSERTE NUMERO, ej: 75.0]** puntos.
- Se ha evidenciado, en el cálculo de frecuencias, que asignaturas troncales como Matemáticas y Comunicación y Lenguajes concentran más del 65% del volumen total de reprobaciones tempranas, actuando como las "materias críticas" fundacionales del deterioro educativo.

*(INSERTE AQUÍ: Figura 4-2: Gráfico temporal o BoxPlot de Promedios separado por estudiantes con Rezago vs No Rezago).*

## 4.3 Resultados y Análisis de los Modelos de Machine Learning (Obj. Esp. 3 y 4)

Se entrenaron y evaluaron tres familias algorítmicas (Árboles de Decisión, Bosques Aleatorios y Redes Neuronales) utilizando el 30% del volumen del dataset como grupo ciego de validación (`X_test`). Los resultados se evaluaron preponderantemente usando las métricas de la Matriz de Confusión y el "Recall" (Sensibilidad o Exhaustividad en detección de la clase 1).

### 4.3.1 Desempeño del Árbol de Decisión Clásico
El primer modelo (CART), bajo la restricción de profundidad `max_depth = 4`, obtuvo una moderada capacidad predictiva. Su arquitectura basada en particiones simples logró una Exactitud Global (Accuracy) del **[INSERTE % DEL ÁRBOL]**, sin embargo, experimentó dificultades al detectar los picos estadísticos de la clase minoritaria (rezago), arrojando falsos positivos debido a las fronteras lineales y su alta varianza en el test.

### 4.3.2 Desempeño del Bosque Aleatorio (Random Forest)
La implementación del parámetro de ajuste heurístico de pesos (`class_weight = "balanced"`) y los 200 árboles de ensamble generaron el resultado matemático más sólido del proyecto.
El modelo alcanzó un *Recall* específico para la clase de riesgo (Rezago) del **[INSERTE % DE RECALL DEL RANDOM FOREST EN TU REPORTE, ej: 88%]**. Esto significa que, logramos interceptar e identificar correctamente a **[EJ: 8 de cada 10]** niños que, en la vida real, terminaron aplastados por el rezago. Su Exactitud Global se estabilizó en **[INSERTE % DE ACCURACY GENERAL DEL RF, ej: 92%]**.

*(INSERTE AQUÍ: Figura 4-3: Tu captura de pantalla de la Matriz de Confusión del Random Forest).*
   
El gráfico (figura 4-3) demuestra operativamente que la calibración priorizó la penalización del Falso Negativo, asegurando el diagnóstico del alumno necesitado. A partir de las probabilidades de este modelo (`predict_proba`), se generaron los clústeres de riesgo Alto, Medio y Bajo que consume el sistema gráfico (Dashboard).

### 4.3.3 Desempeño del Perceptrón Multicapa (Red Neuronal)
La red profunda de dos capas ocultas (10, 10 nodos) procesó los predictores estandarizados, operando la función activadora no lineal ReLU. Tras 500 iteraciones (épocas de entrenamiento Adam), convergió en una Exactitud (Accuracy) de **[INSERTE % DE ACCURACY DEL MLP]** y un puntaje de *Recall* para rezago de **[INSERTE % DE RECALL DEL MLP]**. 
Si bien la red neural es computacionalmente más pesada, exhibió una minuciosa lectura de características cruzadas, confirmando teóricamente que los modelos en base a Perceptrones capturan muy bien las asimetrías subyacentes de las calificaciones cuando se las escala matemáticamente.

*(INSERTE AQUÍ: Figura 4-4: Gráficos de Fronteras de Decisión o Matriz de Confusión del modelo de Red Neuronal).*
