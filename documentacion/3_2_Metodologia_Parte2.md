### 3.4.3 Etapa 3: Modelado de Machine Learning y Entrenamiento (Obj. 3)
La configuración arquitectónica predictiva recayó en una transformación intertemporal (`Obj3_` y `Obj4_`).
**Transformación Multianual:** El dataset requirió redefinir la unidad de predicción hacia la próxima gestión escolar calculando retardos cronológicos (uso de la función `shift` sobre `RUDE` agrupado). Se declararon variables descriptoras como: `promedio_general_prev` y `num_materias_reprobadas_prev`. La variable a pronosticar mutó a `rezago_next`. 

A partir de estos predictores unificados (*Features* X) y el objetivo (*Target* Y = rezago_next), se implementó un proceso de subdivisión aleatoria estratificada (`train_test_split`). Se reservó el 70% del dataset original para la fase rigurosa de entrenamiento (*train*) y un 30% aislado herméticamente para validación empírica y prueba técnica (*test*).

Se instanciaron y configuraron matemáticamente tres modelos clasificadores (Scikit-Learn).

1.  **Iteración 1: Árbol de Decisión Clásico:**
    *   **Algoritmo Base:** `DecisionTreeClassifier`.
    *   **Hiperparámetros:** Restricción vertical a `max_depth = 4` y homogeneidad en generador probabilístico `random_state = 42`.
    *   **Mecánica de Entrenamiento:** Alimentado directo desde el 70% del dataset (`X_train`, `y_train`) derivado de variables no estandarizadas.

2.  **Iteración 2: Random Forest Clasificador:**
    *   **Algoritmo Base:** `RandomForestClassifier`.
    *   **Hiperparámetros Principales:** Volumen arbóreo definido artificialmente a `n_estimators = 200`, con control de sobreajuste limitando la profundidad celular con `max_depth = 5`.
    *   **Mecánica Contra Desbalanceo:** El factor clave introducido fue el parámetro heurístico `class_weight = "balanced"`. Al existir asimetría severa natural en educación (muchos aprobados, escasos reprobados), este ajuste alteró dinámicamente el ensamblado de los árboles, amplificando el peso penalizador si el algoritmo fallaba en detectar la minoría que entraría en riesgo.

3.  **Iteración 3: Perceptrón Multicapa (MLP) - Redes Neuronales:**
    *   **Preparación Categórica:** Dado que las RNA son topológicamente sensibles, la matriz de predictores sufrió un pre-procesamiento de estandarización (*StandardScaler*) para comprimir las magnitudes de `promedio` y `materias reprobadas` en desviaciones uniformes.
    *   **Configuración Estructural (Topología):** `MLPClassifier(hidden_layer_sizes=(10, 10))`. Red *feedforward* estructurada con capa de entrada (2 nodos), 2 capas intermedias densamente conectadas y convergencia en 1 nodo unitario probabilístico (Capa de Salida).
    *   **Mecánicas Computacionales Adicionales:** Función de activación matricial iterada por "ReLU", integrando retropropagación de la validación matemática resuelta por gradientes estocásticos del optimizador "Adam" a `max_iter=500`.

### 3.4.4 Etapa 4: Desempeño y Segregación de Riesgos Estudiantiles (Obj. 4)
Para comprobar si la capacidad descriptora fue la idónea y seleccionar el producto informático, el 30% del volumen inicial aislado (`X_test`) se alimentó como dato experimental o de ensayo ciego en cada uno de los 3 modelos ya entrenados.
Se recopilaron los vectores resultantes `y_pred` y se contrastaron matricialmente con las etiquetas verdaderas vectorizadas en `y_test`.
*   **Resultados de Computación Evaluativa:** Se instanció el cálculo procedimental de `confusion_matrix` y `classification_report`. La prioridad de este proyecto se basó en el indicador de "Recall" respecto a la clase (Rezago).
*   **Segmentación Heurística de Respuestas:** El diseño procedió a crear la tabla matriz inferencia que utilizarán los tomadores de decisión. Para el modelo dominante seleccionado, el componente `.predict_proba()` devolvió la métrica matemática cruda en un intervalo flotante de [0 a 1.0]. A través de una función `nivel_riesgo`, el algoritmo separó al estudiantado en clústeres artificiales: Riesgo *Alto* (>= 0.70), Riesgo *Medio* (0.40 a 0.70) y Resto *Bajo* (< 0.40).

*(INSERTE AQUÍ: Figura 3-5: Matriz de Confusión obtenida en tus libretas, ej: la del bosque o red neuronal)*

### 3.4.5 Etapa 5: Aplicativo Docente Web - Prototipo Final (Obj. 5)
Para lograr que la comunidad educativa interactuara con el backend predictivo con tecnología punta sin requerir consola informática, los flujos del aprendizaje automático exportado se serializaron y empaquetaron operativamente con la biblioteca computacional de integración (Joblib). (Guarda física en directorio `/modelos_entrenados/`).

Posterior a esta exportación en binarios (.pkl) `rf` (Random Forest), `MLP` (Redes) y `scaler`, se procedió al montaje técnico de una Interfaz de Usuario (UI).
-   **Framework Operativo:** La renderización interactiva y reactiva se generó utilizando el entorno unificado de servidor y frontend para Ciencia de Datos *Streamlit* (`Obj5_Prototipo_Dashboard_Docente/app.py`).
-   **Diseño de Módulo Docente:** En la sub-plataforma (*sidebar*), los educadores inician los parámetros deslizantes (*Sliders* controlados en Python) y designan con selectores ("Random Forest" o "Red Neuronal").
-   **Trazabilidad Continua:** Se vinculó directamente por renderización con la librería `Plotly.Express`. El sistema construye localmente un grafo de dispersión ("Scatter") en tiempo real usando el archivo original de 3 gestiones (`primaria_dataset.csv`), sobreponiendo de manera condicional sobre un marco de referencia las fronteras históricas y calculando dónde se "posiciona" visualmente (marcador estrellado) la predicción el estudiante simulado.
-   **Respuesta de la Función:** Generación automática de Alerta en pantalla principal y colores hexadecimales asociados por condicional iterativo (`#ff4b4b` -> Riesgo).

*(INSERTE AQUÍ: Figura 3-6: Capturas de Pantalla del panel web interactivo o dashboard de Streamlit ejecutándose)*
