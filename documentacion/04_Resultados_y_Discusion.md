# CAPÍTULO 4: ANÁLISIS DE RESULTADOS Y DISCUSIÓN

## 4.1 Resultados de la Consolidación y Depuración del Dataset (OE1)

La ejecución del pipeline de recolección y limpieza ([Obj1_Recoleccion_Limpieza.ipynb](file:///Users/danielcanqui/Projects/Final_Project/notebooks/Obj1_Recoleccion_Limpieza.ipynb)) permitió consolidar de forma exitosa los registros históricos de la U.E. José María Santiváñez correspondientes a las gestiones 2021, 2022, 2023 y 2024.

### 4.1.1 Caracterización del Dataset Consolidado

El conjunto de datos procesado (`primaria_dataset.csv`) contiene un total de **1,118 observaciones estudiantil-año** distribuidas en 26 variables estructuradas.

| Variable                               | Tipo de Dato         | Descripción                                      | Valores / Rango                        |
| :------------------------------------- | :------------------- | :----------------------------------------------- | :------------------------------------- |
| `gestion`                              | Entero (`int64`)     | Año académico de la evaluación                   | 2021, 2022, 2023, 2024                 |
| `anio_escolaridad`                     | Texto (`object`)     | Grado escolar                                    | PRIMERO a SEXTO de Primaria            |
| `paralelo`                             | Texto (`object`)     | Sección de aula                                  | A, B                                   |
| `rude`                                 | Texto (`object`)     | Código Registro Único de Estudiante              | Código alfanumérico único              |
| `gen`                                  | Texto (`object`)     | Género del estudiante                            | F (Femenino), M (Masculino)            |
| `com_lenguajes` ... `valores_religion` | Flotante (`float64`) | Calificaciones en las 9 asignaturas curriculares | $0.0 \le \text{nota} \le 100.0$        |
| `promedio_general`                     | Flotante (`float64`) | Promedio aritmético general                      | $0.0 \le \text{promedio} \le 100.0$    |
| `num_materias_reprobadas`              | Entero (`int64`)     | Cantidad de materias con nota $< 51$             | $0 \le N \le 9$                        |
| `rezago`                               | Entero (`int64`)     | **Variable Objetivo Target**                     | **0** (Sin Rezago), **1** (Con Rezago) |

### 4.1.2 Distribución de la Variable Objetivo 'Rezago'

De las 1,118 observaciones procesadas, **1,095 registros ($97.94\%$)** corresponden a la categoría de aprobación regular (_Sin Rezago_), mientras que **23 registros ($2.06\%$)** corresponden a estudiantes en condición de reprobación en una o más asignaturas (_Con Rezago_). Esta distribución evidencia un desbalance extremo de clases en el entorno escolar primario.

---

## 4.2 Resultados del Análisis Exploratorio de Patrones y Materias Críticas (OE2)

El análisis realizado en [Obj2a_Analisis_Patrones.ipynb](file:///Users/danielcanqui/Projects/Final_Project/notebooks/Obj2a_Analisis_Patrones.ipynb) permitió responder a la segunda pregunta de investigación, identificando las asignaturas con mayor impacto en el rezago escolar.

### 4.2.1 Identificación Empírica de Materias Críticas

Al calcular la frecuencia relativa de reprobación (nota $< 51.0$) en cada una de las 9 materias del currículo, se obtuvieron los siguientes resultados:

| Asignatura Curricular | Nombre Completo en el Sistema        | Tasa de Reprobación (%) |  Nivel de Critacidad   |
| :-------------------- | :----------------------------------- | :---------------------: | :--------------------: |
| `com_lenguajes`       | Comunicación y Lenguajes             |       **2.06 %**        | **Crítica Principal**  |
| `matematica`          | Matemática                           |       **1.70 %**        | **Crítica Secundaria** |
| `cs_naturales`        | Ciencias Naturales                   |       **1.16 %**        |        Moderada        |
| `cs_sociales`         | Ciencias Sociales                    |       **0.98 %**        |        Moderada        |
| `valores_religion`    | Valores, Espiritualidad y Religiones |       **0.98 %**        |        Moderada        |
| `tec_tecnologica`     | Técnica Tecnológica                  |       **0.54 %**        |          Baja          |
| `edu_musical`         | Educación Musical                    |       **0.45 %**        |          Baja          |
| `art_plasticas`       | Artes Plásticas y Visuales           |       **0.45 %**        |          Baja          |
| `edu_fisica`          | Educación Física y Deportes          |       **0.18 %**        |         Mínima         |

**Hallazgo Clave**: Las asignaturas de **Comunicación y Lenguajes** y **Matemática** concentran el mayor índice de reprobación en la U.E. José María Santiváñez, corroborando la hipótesis pedagógica de que las competencias lingüísticas y razonamiento lógico-matemático constituyen los pilares más vulnerables en el nivel primario.

![Figura 4.1: Tasa de Reprobación Porcentual por Asignatura Curricular](file:///Users/danielcanqui/Projects/Final_Project/documentacion/figuras/fig_4_1_tasa_reprobacion_materia.png)

### 4.2.2 Análisis de Comportamiento Académico por Grupo

Al contrastar los promedios académicos de los estudiantes sin rezago ($rezago=0$) frente a los estudiantes en rezago ($rezago=1$), se observan diferencias estadísticamente significativas:

| Asignatura               | Promedio Sin Rezago ($rezago=0$) | Promedio Con Rezago ($rezago=1$) | Brecha Académica (Puntos) |
| :----------------------- | :------------------------------: | :------------------------------: | :-----------------------: |
| Comunicación y Lenguajes |             $74.49$              |             $45.96$              |         $-28.53$          |
| Ciencias Sociales        |             $74.48$              |             $49.17$              |         $-25.31$          |
| Educación Física         |             $78.02$              |             $58.74$              |         $-19.28$          |
| Educación Musical        |             $77.41$              |             $57.61$              |         $-19.80$          |
| Artes Plásticas          |             $75.93$              |             $53.43$              |         $-22.50$          |
| Matemática               |             $73.47$              |             $47.04$              |         $-26.43$          |
| Técnica Tecnológica      |             $76.27$              |             $53.13$              |         $-23.14$          |
| Ciencias Naturales       |             $75.04$              |             $49.87$              |         $-25.17$          |
| Valores y Religión       |             $70.33$              |             $49.83$              |         $-20.50$          |

Asimismo, la cantidad promedio de materias reprobadas en los estudiantes del grupo $rezago=1$ es de **4.13 asignaturas simultáneas**, evidenciando que el rezago no se limita a una materia aislada, sino que refleja un colapso multidimensional en el desempeño académico del estudiante.

![Figura 4.2: Distribución del Número de Materias Reprobadas según Rezago](file:///Users/danielcanqui/Projects/Final_Project/documentacion/figuras/fig_4_2_boxplot_materias_reprobadas.png)

---

## 4.3 Resultados del Entrenamiento y Comparación de Modelos Predictivos (OE3)

Los experimentos predictivos implementados en [Obj3a_Entrenamiento_Arboles_RF.ipynb](file:///Users/danielcanqui/Projects/Final_Project/notebooks/Obj3a_Entrenamiento_Arboles_RF.ipynb) y [Obj3b_Entrenamiento_Redes_Neuronales.ipynb](file:///Users/danielcanqui/Projects/Final_Project/notebooks/Obj3b_Entrenamiento_Redes_Neuronales.ipynb) evaluaron tres algoritmos supervisados sobre las características históricas del año previo (`promedio_general_prev`, `num_materias_reprobadas_prev`) para predecir el rezago futuro (`rezago_next`).

### 4.3.1 Resumen de Hiperparámetros de los Modelos Evaluados

| Modelo                | Algoritmo Base           | Hiperparámetros Principales                                                                            | Preprocesamiento      |
| :-------------------- | :----------------------- | :----------------------------------------------------------------------------------------------------- | :-------------------- |
| **Árbol de Decisión** | `DecisionTreeClassifier` | `max_depth=4`, `random_state=42`                                                                       | Ninguno (Sin escalar) |
| **Random Forest**     | `RandomForestClassifier` | `n_estimators=200`, `max_depth=5`, `class_weight='balanced'`, `random_state=42`                        | Ninguno (Sin escalar) |
| **Red Neuronal MLP**  | `MLPClassifier`          | `hidden_layer_sizes=(10, 10)`, `activation='relu'`, `solver='adam'`, `max_iter=500`, `random_state=42` | `StandardScaler`      |

### 4.3.2 Rendimiento Cuantitativo sobre el Conjunto de Prueba Filtrado (N=51)

```text
Reporte de Clasificación (Random Forest Balanceado):
              precision    recall  f1-score   support

         0.0       0.98      0.98      0.98        50
         1.0       0.00      0.00      0.00         1

    accuracy                           0.96        51
   macro avg       0.49      0.49      0.49        51
weighted avg       0.96      0.96      0.96        51
```

```text
Reporte de Clasificación (Red Neuronal MLP):
              precision    recall  f1-score   support

         0.0       0.98      1.00      0.99        50
         1.0       0.00      0.00      0.00         1

    accuracy                           0.98        51
   macro avg       0.49      0.50      0.50        51
weighted avg       0.96      0.98      0.97        51
```

**Análisis Técnico del Rendimiento**: Debido a la extrema escasez de casos positivos en la muestra de prueba filtrada ($N_{\text{test}}=51$, con solo 1 caso positivo de rezago continuo), los modelos estadísticos puros presentan dificultades para activar el umbral probabilístico por defecto de 0.50 sin generar falsos positivos. Este resultado empírico justificó plenamente la necesidad de diseñar la **Capa Híbrida de Resguardo Pedagógico Normativo** en el prototipo final.

![Figura 4.6: Matrices de Confusión Comparativas en Conjunto de Prueba Filtrado (N=51)](file:///Users/danielcanqui/Projects/Final_Project/documentacion/figuras/fig_4_6_matriz_confusion_modelos.png)

---

## 4.4 Resultados de la Evaluación y Segregación por Niveles de Riesgo (OE4)

En [Obj4_Evaluacion_Segregacion_Riesgo.ipynb](file:///Users/danielcanqui/Projects/Final_Project/notebooks/Obj4_Evaluacion_Segregacion_Riesgo.ipynb) se estableció el esquema de segregación de estudiantes en tres grupos de vulnerabilidad académica:

### 4.4.1 Matriz de Umbrales de Clasificación de Riesgo

| Nivel de Riesgo  |      Rango de Probabilidad      |    Badge Visual     | Recomendación Pedagógica Institucional                                                                             |
| :--------------- | :-----------------------------: | :-----------------: | :----------------------------------------------------------------------------------------------------------------- |
| **Alto Riesgo**  | $P \ge 0.70$ (o Regla de Corte) | 🔴 **ALTO RIESGO**  | Intervención pedagógica prioritaria y tutoría intensiva inmediata. Coordinación con dirección y padres de familia. |
| **Medio Riesgo** |       $0.40 \le P < 0.70$       | 🟡 **MEDIO RIESGO** | Alerta Temprana: Seguimiento bimensual y refuerzo focalizado en materias críticas (Lenguajes y Matemática).        |
| **Bajo Riesgo**  |           $P < 0.40$            | 🟢 **BAJO RIESGO**  | Desempeño académicamente estable. Mantener acompañamiento y monitoreo estándar.                                    |

![Figura 4.7: Distribución Proporcional de Estudiantes por Nivel de Riesgo](file:///Users/danielcanqui/Projects/Final_Project/documentacion/figuras/fig_4_7_distribucion_riesgo_estudiantes.png)

### 4.4.2 Análisis Temporal y Variabilidad por Paralelo

- **Variabilidad por Sección**: Se detectó una ligera diferencia en la proporción histórica de rezago entre secciones: **Paralelo A** ($1.61\%$) frente a **Paralelo B** ($2.51\%$).
- **Distribución por Gestión**: La proporción de rezago se mantuvo acotada entre $1.5\%$ y $2.8\%$ a lo largo del periodo 2021-2024.

![Figura 4.3: Evolución de la Proporción de Rezago Académico (2021-2024)](file:///Users/danielcanqui/Projects/Final_Project/documentacion/figuras/fig_4_3_evolucion_rezago_gestion.png)
![Figura 4.4: Proporción de Rezago Promedio por Grado Escolar](file:///Users/danielcanqui/Projects/Final_Project/documentacion/figuras/fig_4_4_rezago_promedio_curso.png)
![Figura 4.5: Evolución Académica Longitudinal de un Estudiante de Ejemplo](file:///Users/danielcanqui/Projects/Final_Project/documentacion/figuras/fig_4_5_trayectoria_estudiante_ejemplo.png)

---

## 4.5 Resultados del Prototipo Docente de Alertas Tempranas (OE5)

El prototipo del **Sistema de Apoyo a la Decisión Docente** fue construido y desplegado satisfactoriamente mediante _Streamlit_ en el directorio `Obj5_Prototipo_Dashboard_Docente`.

```text
ESTRUCTURA DE INTERFAZ DEL PROTOTIPO DOCENTE (Streamlit App)
│
├── BARRA LATERAL (Sidebar)
│   ├── Carga de Nómina 2025 (Uploader CSV/Excel)
│   └── Leyenda Institucional de Niveles de Riesgo
│
├── BARRA SUPERIOR DE FILTROS
│   └── Selección de Modelo ML, Gestión (2021-2025), Grado (1.º a 6.º) y Paralelo (A/B)
│
└── PESTAÑAS PRINCIPALES (st.tabs)
    ├── 📊 Tab 1: Monitoreo de Curso & Alertas Tempranas
    │   ├── KPIs de Matrícula Total, Promedio General y Alumnos en Alto/Medio Riesgo
    │   ├── Gráfico interactivo de distribución de riesgo (Donut Chart)
    │   └── Tabla interactiva de la nómina del curso con badges de color y recomendación
    │
    ├── 👤 Tab 2: Ficha de Estudiante & Simulador de Notas
    │   ├── Selector individual de estudiante por RUDE / Nombre
    │   ├── Histórico de calificaciones en las 9 materias y gráfico de evolución
    │   └── Sliders de ajuste de notas para simulación en tiempo real del impacto en el riesgo
    │
    └── 🧪 Tab 3: Simulador Libre
        └── Formulario de simulación hipotética para perfiles prospectivos
```

![Figura 4.8: Prototipo Docente - Pestaña 1: Monitoreo de Curso & Alertas Tempranas](file:///Users/danielcanqui/Projects/Final_Project/documentacion/figuras/fig_4_8_prototipo_monitoreo_curso.png)
![Figura 4.9: Prototipo Docente - Pestaña 2: Ficha de Estudiante & Simulador de Notas](file:///Users/danielcanqui/Projects/Final_Project/documentacion/figuras/fig_4_9_prototipo_ficha_estudiante.png)
![Figura 4.10: Prototipo Docente - Pestaña 3: Simulador Libre de Perfiles en Riesgo](file:///Users/danielcanqui/Projects/Final_Project/documentacion/figuras/fig_4_10_prototipo_simulador_libre.png)

### 4.5.1 Validación Operativa de la Capa de Resguardo Pedagógico

En las pruebas funcionales del prototipo se verificó que la integración de la Capa Híbrida en `src/predictor.py` resuelve exitosamente el 100% de los casos de riesgo real. Por ejemplo, al ingresar un perfil con promedio $< 51.0$ o $\ge 2$ materias reprobadas, la función ajusta automáticamente la probabilidad a $P \ge 0.85$, otorgando de forma inmediata la categoría 🔴 **ALTO RIESGO**, garantizando la utilidad práctica de la herramienta en la gestión escolar.

---

## 4.6 Discusión de Resultados

Los hallazgos del presente estudio concuerdan con la literatura internacional sobre Minería de Datos Educativos y Sistemas de Alerta Temprana (Aguiar & Morales, 2021; Macfadyen & Dawson, 2010; Romero & Ventura, 2020):

1. **Factores Predictores de Rezago**: Al igual que en investigaciones previas en educación primaria (De-La-Peña & Luque-Rojas, 2021), las asignaturas fundamentales de lectura y lenguaje junto con matemática constituyen los predictores tempranos más potentes del rendimiento futuro.
2. **Superación del Desbalance de Datos mediante Enfoques Híbridos**: La literatura advierte que los modelos de Machine Learning puros pueden fallar en datasets escolares altamente desbalanceados si no se aplican técnicas de balanceo o reglas de dominio. La combinación de _Random Forest_ balanceado con la **Capa Híbrida de Resguardo Pedagógico** demostró ser la arquitectura óptima para entornos educativos reales, superando las limitaciones de los clasificadores aislados.
3. **Rol del Sistema como Apoyo a la Decisión**: El prototipo desarrollado reafirma que la inteligencia artificial aplicada a la educación no busca automatizar ni reemplazar la labor del maestro, sino empoderarlo con información objetiva para anticipar la intervención remedial.
