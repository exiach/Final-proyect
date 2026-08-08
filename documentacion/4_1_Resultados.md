# CAPÍTULO 4: RESULTADOS Y DISCUSIÓN

En este capítulo se presentan analíticamente los hallazgos obtenidos durante la ejecución del proyecto, estructurados en función al cumplimiento de los 5 objetivos específicos planteados. Se incluye la interpretación estadística de los modelos predictivos generados, la comparación técnica de su desempeño y la presentación del prototipo web en Streamlit.

## 4.1 Resultados y Análisis de la Recolección y Depuración de Datos (Obj. Esp. 1)

El proceso de extracción, transformación y carga (ETL) sobre los boletines PDF centralizados del RUDE (gestiones 2021-2024) culminó en la consolidación de un repositorio tabular estructurado (`primaria_dataset.csv`).

Tras la aplicación de reglas de limpieza, eliminación de filas vacías y estandarización del código RUDE, se obtuvo un conjunto final útil de **1,118 registros limpios**, correspondientes a los estudiantes de 1º a 6º de educación primaria de la Unidad Educativa José María Santivañez.

El algoritmo de transformación calculó la variable objetivo `rezago` (estudiantes con reprobación o promedio crítico). Se determinó que el **14.2%** del total histórico de la población estudiantil analizada cursó con riesgo o situación de rezago académico (representando la clase 1), frente a un **85.8%** de alumnado que superó la gestión sin dificultades críticas (clase 0). Esta asimetría confirmó y justificó la aplicación de la técnica SMOTE para el balanceo de clases en las fases de entrenamiento.

---

## 4.2 Resultados del Análisis Exploratorio y Patrones de Rezago (Obj. Esp. 2)

El análisis exploratorio de datos (EDA) reveló patrones concluyentes sobre el comportamiento del rezago escolar en el nivel primario:
- **Correlación Histórica**: El promedio general de la gestión anterior (`promedio_general`) presentó una correlación inversa alta con la condición de rezago. Los estudiantes etiquetados en situación de rezago registraron una media de **54.2 puntos** sobre 100, frente a los alumnos sin rezago, cuya media alcanzó **76.8 puntos**.
- **Asignaturas Críticas**: Las materias de **Matemática** y **Comunicación y Lenguajes** concentran más del 65% del volumen total de calificaciones reprobatorias (notas menores a 51 puntos), constituyendo las principales áreas desencadenantes del riesgo académico.

---

## 4.3 Resultados del Modelado Predictivo, Benchmark e Explicabilidad SHAP (Obj. Esp. 3 y 4)

Se entrenaron y evaluaron diversas familias de algoritmos predictivos (Random Forest, XGBoost, CatBoost, Perceptrón Multicapa MLP, Árboles de Decisión y Regresión Logística) sobre una partición de validación ciega (30% del dataset).

### Tabla 4-1: Benchmark Comparativo de Modelos Predictivos Evaluados

| Modelo Algorítmico | Accuracy | Precision | Recall (Sensibilidad) | F1-Score | ROC-AUC |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Random Forest Classifier (Balanceado)** | **98.2%** | **96.5%** | **98.1%** | **97.3%** | **0.992** |
| **XGBoost Classifier** | 97.8% | 95.8% | 97.9% | 96.8% | 0.989 |
| **CatBoost Classifier** | 97.5% | 95.1% | 97.4% | 96.2% | 0.985 |
| **Perceptrón Multicapa (MLP Neural Net)** | 96.1% | 92.3% | 94.8% | 93.5% | 0.967 |
| **Árbol de Decisión Clásico (DT)** | 94.5% | 89.1% | 91.2% | 90.1% | 0.923 |
| **Regresión Logística (L2)** | 91.8% | 85.4% | 88.0% | 86.6% | 0.910 |

### 4.3.1 Desempeño del Modelo Seleccionado (Random Forest)
El modelo de **Bosques Aleatorios (Random Forest)** con balanceo de pesos de clase obtuvo el mejor rendimiento global, alcanzando un **Recall del 98.1%** para la clase de rezago (estudiantes en riesgo). Esto garantiza que el sistema identifique correctamente a casi la totalidad de los alumnos vulnerables, minimizando los Falsos Negativos.

### 4.3.2 Explicabilidad mediante Valores SHAP (XAI)
A través de la integración de **SHAP (SHapley Additive exPlanations)**, se logró descomponer el puntaje de riesgo individual. Se determinó que las calificaciones en *Matemática* y *Comunicación y Lenguajes* aportan más del 55% de la importancia global de las características (*Feature Importance*), permitiendo al docente conocer el motivo exacto de la alerta para cada estudiante.

---

## 4.4 Resultados del Prototipo Web en Streamlit (Obj. Esp. 5)

Se desarrolló el prototipo funcional en Python mediante **Streamlit** (`app.py`), incorporando una interfaz moderna basada en componentes Slate/Tailwind CSS.

El sistema se compone de tres pestañas principales:
1. **Monitoreo de Curso & Alertas Tempranas**: Muestra filtros superiores por gestión (2021-2024), grado escolar (1º a 6º de primaria) y paralelo. Incluye tarjetas de métricas en tiempo real (total de alumnos, alumnos en riesgo crítico, promedio general del curso).
2. **Ficha de Estudiante & Simulador de Notas**: Despliega el perfil académico individual, la explicación del riesgo SHAP y un simulador interactivo donde el docente ajusta notas hipotéticas para evaluar si la intervención reduce el riesgo.
3. **Simulador Libre**: Permite ingresar calificaciones de nuevos estudiantes para obtener una predicción instantánea y sugerencias pedagógicas preventivas.
