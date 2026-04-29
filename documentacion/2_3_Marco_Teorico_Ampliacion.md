## 2.5 Metodología de Desarrollo: CRISP-DM y KDD

Para garantizar que el modelo de *Machine Learning* sea académicamente válido y tecnológicamente escalable, este proyecto se enmarca teóricamente en el modelo **CRISP-DM** (Cross-Industry Standard Process for Data Mining). Este estándar es la metodología analítica más utilizada globalmente para proyectos de minería de datos (Wirth & Hipp, 2000). 
CRISP-DM establece que un proyecto predictivo (como la anticipación del rezago escolar) no es un proceso lineal, sino un ciclo robusto compuesto por seis fases iterativas:

1. **Comprensión del Negocio (Business Understanding):** En la educación, esto equivale a comprender a profundidad el problema del rezago escolar, las limitaciones del RUDE, y las necesidades del plantel docente antes de tocar una sola línea de código.
2. **Comprensión de los Datos (Data Understanding):** Involucra la exploración inicial (EDA) para identificar la dimensionalidad de las calificaciones históricas.
3. **Preparación de los Datos (Data Preparation):** Coincide con las metodologías ETL previamente discutidas. Es la fase estadística donde se tratan los valores nulos, se limpian imperfecciones en el registro de materias y se estructuran en matrices funcionales.
4. **Modelado (Modeling):** La fase matemática donde se aplican algoritmos (Árboles de Decisión, Redes Neuronales) sobre el dataset limpio.
5. **Evaluación (Evaluation):** El contraste métrico de los modelos (Matriz de Confusión, Precisión, Exhaustividad).
6. **Despliegue (Deployment):** La entrega final de valor, que en este proyecto se consolida a través del panel interactivo (Dashboard) en tecnología Web (Streamlit).

## 2.6 Ingeniería de Características (Feature Engineering)

La Inteligencia Artificial por sí sola no genera valor si los datos subyacentes carecen de significado semántico. Aquí radica la importancia de la Ingeniería de Características, definida por Zheng y Casari (2018) como el proceso de extraer, matemáticamente o lógicamente, nuevos "rasgos" (features) a partir de los datos crudos para ayudar a que los algoritmos de predicción descubran patrones latentes.

En el pronóstico del rezago no basta con introducir al algoritmo las variables puras de la boleta escolar actual. El desgaste cognitivo es acumulativo. Por lo tanto, el marco teórico computacional sugiere calcular métricas longitudinales e intertemporales.
- **Ventanas de Tiempo (Shift):** En la analítica educativa, utilizar el rendimiento de `Gestión = T` para predecir el impacto en `Gestión = T+1` permite que la máquina construya un puente causal entre el pasado y el futuro (Baker & Inventado, 2014).
- **Agregación Matemática:** En lugar de alimentar al algoritmo con diez notas dispersas de materias distintas, la "Ingeniería de Características" consolida el esfuerzo estudiantil calculando vectores agregados como el *Promedio General Histórico* o un sumatorio del *Número Total de Materias Reprobadas Previamente*. Estas variables sintéticas son las que aportan la verdadera capacidad "predictiva" a las Redes Neuronales.

## 2.7 Evaluación Matemática de Modelos Clasificadores

Al entrenar múltiples algoritmos de *Machine Learning* para un mismo propósito educativo (predecir Riesgo/No Riesgo), es imprescindible contar con un marco teórico de evaluación matemática que determine métricamente cuál es el superior. El uso exclusivo del indicador de "Exactitud" (Accuracy) está contraindicado en bases de datos educativas (Fawcett, 2006).

### 2.7.1 La Paradoja de la Exactitud en Datos Educativos
En un escenario donde el 90% de los estudiantes aprueba y el 10% tiene rezago (datos desbalanceados), un algoritmo "tonto" que siempre prediga "Aprobado" para todos, obtendrá matemáticamente un 90% de Exactitud. Aunque estadísticamente parece brillante, este modelo tiene una utilidad del 0% para el docente, pues no detectó a ninguno de los estudiantes en riesgo real (Chawla et al., 2004). Para solventar esto, se utiliza la **Matriz de Confusión**.

### 2.7.2 Matriz de Confusión y Métricas Derivadas
La Matriz de Confusión es una tabla transversal que evalúa el desempeño de algoritmos de clasificación supervisada (Provost & Fawcett, 2013). Descompone las predicciones en cuatro cuadrantes:
- **Verdaderos Positivos (TP):** El algoritmo predijo Riesgo de Rezago y el estudiante efectivamente fracasó (Acierto crítico).
- **Verdaderos Negativos (TN):** El algoritmo predijo Aprobación y el estudiante, en efecto, aprobó.
- **Falsos Positivos (FP - Error Tipo I):** El algoritmo predijo Rezago, pero el estudiante aprobó (Falsa alarma).
- **Falsos Negativos (FN - Error Tipo II):** El algoritmo predijo Aprobación, pero el estudiante fracasó (Error fatal metodológicamente).

A partir de ella se desprenden las métricas reales que evalúan este proyecto:
1. **Precisión (Precision):** De todos los que el modelo etiquetó en riesgo, ¿cuántos realmente fracasaron? (TP / (TP + FP)).
2. **Exhaustividad o Sensibilidad (Recall):** De todos los estudiantes que *realmente* fracasaron históricamente, ¿cuántos logró encontrar el modelo? (TP / (TP + FN)). En sistemas de alerta temprana, maximizar el *Recall* es la prioridad número uno, incluso a costa de algunas falsas alarmas, pues es preferible brindar tutorías a un niño que no las necesitaba (Falso Positivo) que dejar desamparado a un niño que terminó reprobando (Falso Negativo) (García & Ruiz, 2023).

---
### Referencias Bibliográficas Adicionales (Adicionar a la lista anterior)
- Chawla, N. V., Japkowicz, N., & Kotcz, A. (2004). *Special issue on learning from imbalanced data sets*. ACM SIGKDD Explorations Newsletter, 6(1), 1-6.
- Fawcett, T. (2006). *An introduction to ROC analysis*. Pattern Recognition Letters, 27(8), 861-874.
- Provost, F., & Fawcett, T. (2013). *Data Science for Business: What you need to know about data mining and data-analytic thinking*. O'Reilly Media.
- Wirth, R., & Hipp, J. (2000). *CRISP-DM: Towards a standard process model for data mining*. In Proceedings of the 4th international conference on the practical applications of knowledge discovery and data mining.
- Zheng, A., & Casari, A. (2018). *Feature Engineering for Machine Learning: Principles and Techniques for Data Scientists*. O'Reilly Media.
