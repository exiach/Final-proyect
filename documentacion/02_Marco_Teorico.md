# CAPÍTULO 2: MARCO TEÓRICO Y CONCEPTUAL

## 2.1 Rendimiento Académico y Rezago Escolar en Educación Primaria

El **rendimiento académico** se define como una medida cuantitativa y cualitativa del grado de adquisición de conocimientos, habilidades y competencias que un estudiante demuestra dentro del proceso educativo formal (De-La-Peña & Luque-Rojas, 2021). En el contexto del Sistema Educativo Plurinacional de Bolivia, la calificación se expresa en una escala numeral de 1 a 100 puntos, fijando los 51 puntos como la nota mínima requerida para la aprobación de una materia o área saberes (Ministerio de Educación del Estado Plurinacional de Bolivia, 2021).

Por su parte, el **rezago académico** (o vulnerabilidad académica) se manifiesta cuando un alumno no alcanza los estándares mínimos de aprendizaje requeridos para su nivel de escolaridad, acumulando calificaciones reprobatorias (inferiores a 51 puntos) en una o más asignaturas curriculares o presentando una trayectoria escolar discontinua. En la presente investigación, el rezago académico se operacionaliza como una **variable dicotómica ($Y \in \{0, 1\}$)**:

$$Y = \begin{cases} 1, & \text{si el estudiante reprueba } \ge 1 \text{ asignaturas en la gestión } (N_{\text{reprobadas}} > 0) \\ 0, & \text{si el estudiante aprueba la totalidad de sus asignaturas } (N_{\text{reprobadas}} = 0) \end{cases}$$

---

## 2.2 Minería de Datos Educativos (EDM) y Learning Analytics (LA)

La **Minería de Datos Educativos** (*Educational Data Mining* - EDM) es un campo de investigación interdisciplinario centrado en el desarrollo y aplicación de métodos computacionales para explorar datos originados en entornos educativos, permitiendo comprender mejor a los estudiantes y los entornos en los que aprenden (Romero & Ventura, 2020). Complementariamente, la **Analítica del Aprendizaje** (*Learning Analytics* - LA) se enfoca en la medición, recopilación, análisis y presentación de datos sobre los aprendices y sus contextos, con el propósito de optimizar los procesos de enseñanza y los entornos formativos.

Mientras que EDM enfatiza las técnicas algorítmicas automáticas de extracción de patrones a partir de datos estructurados e no estructurados, LA acentúa la interpretación humana y la intervención pedagógica. El presente trabajo integra ambos paradigmas: utiliza EDM para entrenar modelos predictivos supervisados y utiliza LA para diseñar tableros de control interactivos que faciliten la toma de decisiones por parte de los docentes.

---

## 2.3 Sistemas de Alerta Temprana (Early Warning Systems - EWS)

Los **Sistemas de Alerta Temprana** (EWS) en el ámbito educativo son herramientas analíticas diseñadas para identificar oportunamente a aquellos estudiantes en riesgo de bajo rendimiento o deserción escolar mediante el análisis de indicadores históricos y conductuales (Aguiar & Morales, 2021; Macfadyen & Dawson, 2010). Un EWS eficaz no solo predice la probabilidad de una contingencia negativa, sino que categoriza el riesgo en niveles operables y sugiere recomendaciones de intervención pedagógica.

---

## 2.4 Fundamentos de Machine Learning en Clasificación Supervisada

El aprendizaje supervisado abarca aquellos algoritmos de Machine Learning que aprenden una función de mapeo $f: \mathbf{X} \rightarrow Y$ a partir de un conjunto de entrenamiento etiquetado $\mathcal{D} = \{(\mathbf{x}_i, y_i)\}_{i=1}^N$, donde $\mathbf{x}_i \in \mathbb{R}^d$ representa el vector de características del estudiante (e.g., promedios previos, número de materias reprobadas) y $y_i \in \{0, 1\}$ denota la clase real de rezago.

### 2.4.1 Árboles de Decisión (Decision Tree Classifier)
Un Árbol de Decisión es un modelo no paramétrico que particiona recursivamente el espacio de características mediante reglas lógicas de decisión jerárquicas (Breiman, 2001). En cada nodo interno $m$, el algoritmo evalúa la mejor división $j$ de una característica $x_j$ y un umbral $t$ que maximiza la reducción de la impureza de Gini ($I_G$):

$$I_G(m) = 1 - \sum_{k=0}^{1} p_{mk}^2$$

donde $p_{mk}$ es la proporción de instancias pertenecientes a la clase $k$ en el nodo $m$. En nuestro proyecto, el modelo de Árbol de Decisión se parametriza con `max_depth=4` para prevenir el sobreajuste (*overfitting*) en conjuntos de datos de escala escolar.

### 2.4.2 Random Forest Classifier y Balanceo de Clases
Un *Random Forest* (Bosque Aleatorio) es un algoritmo de ensamble basado en la técnica de agregación por arranque (*bootstrap aggregating* o *bagging*), propuesto por Breiman (2001). Construye un conjunto de $B$ árboles de decisión no correlacionados entrenados en diferentes submuestras con reemplazo del dataset original y selecciona subconjuntos aleatorios de características en cada nodo.

Para un vector de características $\mathbf{x}$, la predicción de la probabilidad de rezago resulta de la promediación de los árboles individuales:

$$P(Y=1 \mid \mathbf{x}) = \frac{1}{B} \sum_{b=1}^{B} P_b(Y=1 \mid \mathbf{x})$$

#### Tratamiento del Desbalance de Clases mediante Ponderación (`class_weight='balanced'`)
En conjuntos de datos educativos escolares, la clase de rezago ($Y=1$) suele ser altamente minoritaria (e.g., 2.06% de la nómina). Para evitar que el modelo favorezca a la clase mayoritaria ($Y=0$), se utiliza el ajuste ponderado del costo de error:

$$w_k = \frac{N}{K \cdot N_k}$$

donde $N$ es el total de observaciones, $K=2$ es el número de clases y $N_k$ es la cantidad de muestras en la clase $k$. De este modo, la penalización por clasificar erróneamente un estudiante en rezago se incrementa automáticamente en proporción a su rareza estadística.

### 2.4.3 Redes Neuronales Artificiales: Perceptrón Multicapa (MLP)
El Perceptrón Multicapa (*Multilayer Perceptron* - MLP) es una arquitectura de red neuronal prealimentada (*feedforward*) compuesta por una capa de entrada, una o más capas ocultas y una capa de salida (Haykin, 2009). Cada neurona $j$ en la capa $l$ computa una combinación lineal de las salidas de la capa anterior $l-1$, seguida de una función de activación no lineal $g(\cdot)$:

$$a_j^{(l)} = g\left( \sum_{i} w_{ji}^{(l)} a_i^{(l-1)} + b_j^{(l)} \right)$$

En el proyecto se implementa una arquitectura con dos capas ocultas de 10 neuronas cada una (`hidden_layer_sizes=(10, 10)`), utilizando la función de activación Unidad Rectificada Lineal (ReLU) para las capas ocultas:

$$\text{ReLU}(z) = \max(0, z)$$

y el optimizador Adam para la minimización de la pérdida de entropía cruzada binaria:

$$\mathcal{L}(\theta) = -\frac{1}{N} \sum_{i=1}^N \left[ y_i \log(\hat{y}_i) + (1-y_i) \log(1-\hat{y}_i) \right]$$

---

## 2.5 Tratamiento del Desbalance de Clases en Datos Educativos

La disparidad de clases es un fenómeno inherente a la Minería de Datos Educativos. Cuando la proporción de reprobación es muy baja (alrededor del 2%), los modelos estándar tienden a predecir siempre la clase mayoritaria ($Y=0$), obteniendo una exactitud engañosamente elevada (98%), pero con una sensibilidad de cero ($Recall=0$), inutilizando el sistema para propósitos de prevención. Para mitigar esta distorsión, el proyecto adopta tres estrategias fundamentales:
1. **Separación Estratificada (*Stratified Split*)**: Garantiza que las proporciones relativas de la clase de rezago se mantengan exactamente iguales en los subconjuntos de entrenamiento y evaluación (`stratify=y`).
2. **Algoritmos Sensibles al Costo (*Cost-Sensitive Learning*)**: Configuración de `class_weight='balanced'` en Random Forest.
3. **Métricas de Evaluación Centradas en la Clase Minoritaria**: Evaluación basada en Sensibilidad (*Recall*), Precisión y F1-Score para la clase $Y=1$.

---

## 2.6 Sistemas Híbridos de Soporte a la Decisión (Expert Rules + ML Inference)

Un inconveniente conocido de los modelos de Machine Learning probables es que, bajo situaciones extremas de desbalance de datos o falta de observaciones históricas complejas, pueden generar falsos negativos (estudiantes con notas desfavorables pero con probabilidades estimadas por debajo del umbral de alerta).

Para resolver esta vulnerabilidad operativa, el proyecto implementa un **Sistema Híbrido de Soporte a la Decisión**. Esta arquitectura combina la inferencia estadística del modelo de Machine Learning ($P_{\text{ML}}$) con una **Capa de Resguardo Pedagógico Normativo** basada en reglas expertas derivadas del Reglamento de Evaluación (Ministerio de Educación del Estado Plurinacional de Bolivia, 2021):

$$P_{\text{final}} = \begin{cases} \max(P_{\text{ML}}, 0.85), & \text{si } \text{Promedio} < 51.0 \text{ o } N_{\text{reprobadas}} \ge 2 \\ \max(P_{\text{ML}}, 0.50), & \text{si } N_{\text{reprobadas}} = 1 \text{ o } 51.0 \le \text{Promedio} < 60.0 \\ P_{\text{ML}}, & \text{en cualquier otro caso} \end{cases}$$

Esta capa de resguardo garantiza que ningún estudiante en reprobación efectiva quede sin una alerta de nivel **Alto** o **Medio Riesgo**, asegurando la confiabilidad ética y pedagógica del sistema frente al cuerpo docente.

---

## 2.7 Stack Tecnológico del Proyecto

El desarrollo técnico del proyecto se soporta en un ecosistema de código abierto robusto sobre el lenguaje **Python 3.12** (Pedregosa et al., 2011; Streamlit Inc., 2024):
- **Pandas & NumPy**: Manipulación, agregación, limpieza estructurada e ingeniería de variables temporales.
- **OpenPyXL**: Lectura y extracción programática de libros de cálculo Excel resultantes de la digitalización de boletines centralizadores en PDF.
- **Scikit-Learn**: Entrenamiento, escalamiento (`StandardScaler`), hiperparametrización y evaluación cuantitativa de los modelos supervisados (`DecisionTreeClassifier`, `RandomForestClassifier`, `MLPClassifier`).
- **Joblib**: Serialización e ingesta binaria de los modelos entrenados (`.pkl`).
- **Matplotlib & Seaborn**: Generación de diagnósticos gráficos del análisis exploratorio de datos.
- **Streamlit**: Entorno de desarrollo para la construcción de la aplicación web interactiva de apoyo docente, desplegada localmente con arquitectura modular.
