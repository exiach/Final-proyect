# CAPÍTULO 4: ANÁLISIS DE RESULTADOS Y DISCUSIÓN

## 4.1 Resultados de la Consolidación y Depuración del Dataset (OE1)

La ejecución del pipeline de recolección y limpieza permitió consolidar los registros históricos de la U.E. José María Santiváñez correspondientes a 2022, 2023 y 2024.

### 4.1.1 Caracterización del Dataset Consolidado

El conjunto de datos procesado (`primaria_dataset.csv`) contiene un total de **1,118 observaciones estudiantil-año** distribuidas en 26 variables estructuradas.

| Variable                               | Tipo de Dato         | Descripción                                      | Valores / Rango                        |
| :------------------------------------- | :------------------- | :----------------------------------------------- | :------------------------------------- |
| `gestion`                              | Entero (`int64`)     | Año académico de la evaluación                   | 2022, 2023, 2024                       |
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

Al contrastar descriptivamente los promedios de estudiantes sin rezago ($rezago=0$) y con rezago ($rezago=1$), se observaron las siguientes diferencias. No se afirma significancia estadística porque no se aplicó una prueba inferencial:

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

### 4.3.1 Muestra longitudinal y evaluación temporal

Se obtuvieron 489 transiciones consecutivas T→T+1 con datos completos en ambas gestiones, con seis resultados positivos. Se excluyeron 33 pares con etiqueta objetivo incompleta. El entrenamiento utilizó 241 transiciones 2022→2023 (tres positivas) y la prueba temporal 248 transiciones 2023→2024 (tres positivas).

### 4.3.2 Hiperparámetros de los modelos evaluados

| Modelo                | Algoritmo Base           | Hiperparámetros Principales                                                                            | Preprocesamiento      |
| :-------------------- | :----------------------- | :----------------------------------------------------------------------------------------------------- | :-------------------- |
| **Árbol de Decisión** | `DecisionTreeClassifier` | `max_depth=3`, `min_samples_leaf=10`, `class_weight='balanced'`, `random_state=42` | Ninguno |
| **Random Forest** | `RandomForestClassifier` | `n_estimators=300`, `max_depth=4`, `min_samples_leaf=5`, `class_weight='balanced'`, `random_state=42` | Ninguno |
| **Red Neuronal MLP** | `MLPClassifier` | `hidden_layer_sizes=(4,)`, `alpha=0.1`, `learning_rate_init=0.0001`, `max_iter=1000`, `random_state=42` | `StandardScaler` |

### 4.3.3 Rendimiento en la prueba temporal 2023→2024 (N=248)

| Modelo | TN | FP | FN | TP | Precisión (+) | Recall (+) | F1 (+) | Balanced accuracy | Average precision |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Línea base: siempre sin rezago | 245 | 0 | 3 | 0 | 0 | 0 | 0 | 0,5000 | 0,0121 |
| Árbol de decisión | 232 | 13 | 2 | 1 | 0,0714 | 0,3333 | 0,1176 | 0,6401 | 0,0319 |
| Random Forest | 232 | 13 | 2 | 1 | 0,0714 | 0,3333 | 0,1176 | 0,6401 | 0,0636 |
| MLP | 245 | 0 | 3 | 0 | 0 | 0 | 0 | 0,5000 | 0,2332 |

**Interpretación**: Árbol y Random Forest detectaron uno de tres casos positivos, con 13 falsas alarmas. La MLP no detectó positivos. La evidencia no permite declarar un modelo superior ni afirmar alta precisión. La regla pedagógica se presenta como salvaguarda operativa separada, no como mejora estadística.

![Figura 4.6: Matrices de Confusión en la Prueba Temporal 2023-2024](file:///Users/danielcanqui/Projects/Final_Project/documentacion/figuras/fig_4_6_matriz_confusion_modelos.png)

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

La figura incluye una categoría **Sin datos** para las 88 observaciones que no contienen las nueve calificaciones. Esas filas se conservan para trazabilidad descriptiva, pero el prototipo no les asigna probabilidad ni nivel de riesgo hasta completar la información.

### 4.4.2 Análisis Temporal y Variabilidad por Paralelo

- **Variabilidad por Sección**: Se detectó una ligera diferencia en la proporción histórica de rezago entre secciones: **Paralelo A** ($1.61\%$) frente a **Paralelo B** ($2.51\%$).
- **Distribución por Gestión**: La proporción de rezago se mantuvo acotada entre aproximadamente 1,5 % y 2,8 % durante 2022-2024.

![Figura 4.3: Evolución de la Proporción de Rezago Académico (2022-2024)](file:///Users/danielcanqui/Projects/Final_Project/documentacion/figuras/fig_4_3_evolucion_rezago_gestion.png)
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
│   └── Selección de Modelo ML, Gestión disponible, Grado (1.º a 6.º) y Paralelo (A/B)
│
└── PESTAÑAS PRINCIPALES (st.tabs)
    ├── 📊 Tab 1: Monitoreo de Curso & Alertas Tempranas
    │   ├── KPIs de Matrícula Total, Promedio General y Alumnos en Alto/Medio Riesgo
    │   ├── Gráfico interactivo de distribución de riesgo (Donut Chart)
    │   └── Tabla interactiva de la nómina del curso con badges de color y recomendación
    │
    ├── 👤 Tab 2: Ficha de Estudiante & Simulador de Notas
    │   ├── Selector individual de estudiante por RUDE / Nombre
    │   ├── Perfil académico de la gestión seleccionada y alerta proyectada
    │   └── Campos de ajuste de notas para simulación en tiempo real del impacto en el riesgo
    │
    └── 🧪 Tab 3: Simulador Libre
        └── Formulario de simulación hipotética para perfiles prospectivos
```

![Figura 4.8: Prototipo Docente - Pestaña 1: Monitoreo de Curso & Alertas Tempranas](file:///Users/danielcanqui/Projects/Final_Project/documentacion/figuras/fig_4_8_prototipo_monitoreo_curso.png)
![Figura 4.9: Prototipo Docente - Pestaña 2: Ficha de Estudiante & Simulador de Notas](file:///Users/danielcanqui/Projects/Final_Project/documentacion/figuras/fig_4_9_prototipo_ficha_estudiante.png)
![Figura 4.10: Prototipo Docente - Pestaña 3: Simulador Libre de Perfiles en Riesgo](file:///Users/danielcanqui/Projects/Final_Project/documentacion/figuras/fig_4_10_prototipo_simulador_libre.png)

### 4.5.1 Validación Operativa de la Capa de Resguardo Pedagógico

Las pruebas unitarias verificaron que la regla programada clasifica como alerta alta todo perfil con promedio menor a 51 o dos o más materias reprobadas. Esto valida la implementación de la regla, pero no representa sensibilidad predictiva ni garantiza detectar todos los casos futuros.

---

## 4.6 Discusión de Resultados

Los hallazgos se interpretan a la luz de la literatura sobre Minería de Datos Educativos y Sistemas de Alerta Temprana (Macfadyen & Dawson, 2010; Romero & Ventura, 2020):

1. **Materias con mayor reprobación descriptiva**: Comunicación y Lenguajes y Matemática presentaron las tasas más altas en este conjunto. Este resultado describe la institución estudiada, pero no demuestra causalidad ni que cada asignatura sea un predictor independiente.
2. **Desbalance y enfoque híbrido**: La escasez de eventos limitó a los clasificadores. Las reglas de dominio mejoran la seguridad operativa del prototipo, pero requieren validación prospectiva y no pueden considerarse una arquitectura óptima con la evidencia disponible.
3. **Rol del Sistema como Apoyo a la Decisión**: El prototipo desarrollado reafirma que la inteligencia artificial aplicada a la educación no busca automatizar ni reemplazar la labor del maestro, sino empoderarlo con información objetiva para anticipar la intervención remedial.
