## 2.3 Modelos de Aprendizaje Automático Predictivo (Machine Learning)

El Machine Learning (Aprendizaje Automático) es una rama de la Inteligencia Artificial que permite a los sistemas informáticos aprender de forma autónoma a partir de datos, sin haber sido programados explícitamente para ello (Hastie et al., 2008). En el ámbito educativo, se aplica principalmente el "aprendizaje supervisado", un paradigma donde el algoritmo recibe un conjunto de datos históricos que ya incluye la solución deseada (la variable objetivo o *target*). El modelo analiza las características de los estudiantes y aprende la relación matemática que las vincula con la etiqueta final (por ejemplo: "Aprobado" o "Rezago"). Una vez entrenado, el algoritmo es capaz de predecir la etiqueta de nuevos estudiantes con base en sus características actuales (James, Witten, Hastie & Tibshirani, 2013).

Para la predicción de rezago escolar se han implementado y evaluado comparativamente tres arquitecturas algorítmicas de aprendizaje supervisado, cada una con distintos grados de interpretabilidad y complejidad.

### 2.3.1 Árboles de Decisión (Decision Tree Classifier)
Los Árboles de Decisión son uno de los métodos de clasificación más intuitivos y populares ("Classification and Regression Trees" o CART) introducidos por Breiman, Friedman, Olshen y Stone (1984). Operan dividiendo secuencialmente el espacio de datos en subconjuntos más pequeños a través de reglas de partición tipo "si-entonces" (*if-then*). 

- **Estructura y Funcionamiento:** El modelo comienza con un "nodo raíz" que contiene todos los registros estudiantiles. Luego, elige la característica (ej: Promedio General Previo) que mejor separe a los estudiantes con rezago de los aprobados, basándose en un criterio matemático como la Impureza de Gini o la Ganancia de Información. El árbol se bifurca sucesivamente hasta alcanzar los "nodos hoja", que representan la clasificación o diagnóstico predictivo final (Breiman et al., 1984).
- **Justificación de Uso:** Su principal ventaja en la educación es la "alta interpretabilidad" (Pérez & Martínez, 2024). Un profesor o director académico puede observar gráficamente las reglas del árbol y comprender exactamente bajo qué umbral matemático el sistema ha clasificado a un estudiante como riesgo alto (por ejemplo: "Si el promedio es menor a 55 Y reprobó más de 2 materias, entonces el riesgo es alto").

### 2.3.2 Bosques Aleatorios (Random Forest Classifier)
Si bien los árboles de decisión son interpretables, sufren del problema de "sobreajuste" (overfitting): tienden a memorizar el ruido de los datos de entrenamiento, perdiendo precisión al predecir casos nuevos. Para solucionar esto, Leo Breiman introdujo en 2001 los Bosques Aleatorios (Random Forests), una técnica de "Ensamblado" (*Ensemble Learning*).

- **Estructura y Funcionamiento:** Random Forest no construye un solo árbol, sino una multitud de árboles de decisión (por ejemplo, 100 o 200 árboles) simultáneos e independientes. Cada árbol se entrena utilizando una muestra aleatoria diferente de los datos originales (técnica conocida como *Bagging* o Bootstrap Aggregation) e incluso seleccionando un subconjunto aleatorio de variables (Breiman, 2001). Cuando se necesita predecir el futuro de un estudiante nuevo, cada uno de los 200 árboles emite un "voto" o predicción. El "bosque" determina el resultado final basado en la decisión mayoritaria.
- **Justificación de Uso:** Se considera uno de los algoritmos más robustos y precisos para datos estructurados como las calificaciones escolares (García & Ruiz, 2023). Al promediar el sesgo de cientos de modelos individuales, reduce drásticamente el error de predicción. Además, Random Forest es sumamente eficaz para modelar comportamientos no lineales sin necesidad de estandarizar rigurosamente las variables de entrada.

### 2.3.3 Redes Neuronales Artificiales: Perceptrón Multicapa (MLP)
Las Redes Neuronales Artificiales son el cimiento sobre el que se construye el campo del *Deep Learning* (Aprendizaje Profundo). Inspiradas remotamente en la sinapsis del cerebro biológico, su bloque fundamental es el Perceptrón. Cuando múltiples perceptrones se agrupan en capas interconectadas, forman el Perceptrón Multicapa (Multi-Layer Perceptron o MLP), la arquitectura más clásica de las redes "feedforward" (hacia adelante).

- **Estructura y Funcionamiento:** Un MLP consta, como mínimo, de tres etapas (Haykin, 2009):
  1. **Capa de Entrada (Input Layer):** Recibe las variables estandarizadas del estudiante (ej: Promedio estandarizado, Materias Reprobadas estandarizadas).
  2. **Capas Ocultas (Hidden Layers):** Capas intermedias compuestas por "neuronas" artificiales. Cada conexión entre neuronas posee un "peso" matemático. Dentro de la neurona se aplica una "función de activación no lineal" (como ReLU o Sigmoide) que permite al modelo aprender correlaciones sumamente complejas que serían invisibles para una regresión lineal tradicional.
  3. **Capa de Salida (Output Layer):** Arroja la probabilidad matemática de que el alumno pertenezca a la clase de rezago (Goodfellow, Bengio & Courville, 2016).
- **Entrenamiento:** La red aprende mediante un proceso cíclico llamado "propagación hacia atrás" (*Backpropagation*). Compara su predicción con la realidad, calcula el margen de error, y viaja en reversa a través de la red ajustando los "pesos" matemáticos de las conexiones para minimizar dicha equivocación (Haykin, 2009).
- **Justificación de Uso:** En el análisis del abandono y rezago estudiantil, estudios afirman que las redes neuronales pueden ofrecer una precisión marginal superior al desentrañar relaciones abstractas de alta dimensionalidad (Pérez & Martínez, 2024), representando la vanguardia computacional en Educational Data Mining.

## 2.4 Sistemas de Alerta Temprana y Visualización de Datos (Dashboards)

Finalmente, el ecosistema de la analítica de datos no concluye con la predicción puramente matemática, sino con la transmisión comunicativa del valor predictivo a los tomadores de decisión (en este caso, los docentes).

Un Sistema de Alerta Temprana (Early Warning System) aplicado a la educación es una herramienta procedimental que intercepta a los estudiantes en vías del fracaso antes de materializar el abandono (Cardoso et al., 2021). Para ello se construyen "Dashboards" (Paneles de Control), que son interfaces visuales que muestran indicadores de desempeño clave (KPIs) en una sola pantalla. En el contexto de lenguajes de programación modernos, el uso de frameworks como Streamlit o tecnologías similares permite integrar sin fricciones los complejos modelos de Machine Learning (como Random Forests almacenados en backend) con una interfaz de usuario interactiva en la web (Pérez, 2021). Estos prototipos eximen al especialista en educación de interactuar algorítmicamente con el modelo, habilitando un entorno intuitivo compuesto por semáforos de riesgo (Riesgo Alto, Medio, Bajo), barras de probabilidad predictiva y contextos gráficos del aula en tiempo real.


---
### Referencias Bibliográficas (Adicionar a tu lista APA en el documento final)
- Baker, R. S., & Inventado, P. S. (2014). *Educational data mining and learning analytics*. In Learning analytics (pp. 61-75). Springer, New York, NY.
- Breiman, L., Friedman, J., Olshen, R., & Stone, C. (1984). *Classification and Regression Trees*. Wadsworth.
- Breiman, L. (2001). Random Forests. *Machine Learning*, 45(1), 5-32.
- Goodfellow, I., Bengio, Y., & Courville, A. (2016). *Deep Learning*. MIT Press.
- Han, J., Kamber, M., & Pei, J. (2011). *Data mining: concepts and techniques*. Morgan Kaufmann.
- Hastie, T., Tibshirani, R., & Friedman, J. (2008). *The Elements of Statistical Learning: Data Mining, Inference, and Prediction* (2nd ed.). Springer.
- Haykin, S. (2009). *Neural Networks and Learning Machines* (3rd ed.). Pearson Education.
- James, G., Witten, D., Hastie, T., & Tibshirani, R. (2013). *An Introduction to Statistical Learning: With Applications in R*. Springer.
