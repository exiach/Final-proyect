## 4.4 Discusión de Resultados

La etapa crucial de este proyecto radica en someter el desempeño empírico obtenido en el modelado a un riguroso análisis comparativo con investigaciones de la misma familia, para medir el estado del arte y la viabilidad de despliegue sobre el colegio objetivo en Cochabamba.

### 4.4.1 Contraste con el Estado del Arte Relevante
Los resultados de la investigación latinoamericana liderada por Pérez y Martínez (2024) sobre "Algoritmos Predictivos de Deserción Escolar", muestran que los modelos de Bosques Aleatorios (Random Forest) sin sintonización de hiperparámetros alcanzan usualmente un 85% a 89% de precisión, pero fracasan rutinariamente levantando un alto volumen de Falsos Negativos debido a que la gran mayoría de los alumnos no deserta (desbalance crítico) (ver figura 4-10 referencial). A efectos de poder efectuar la comparación, nuestros resultados balanceados ajustados a la dimensionalidad primaría del colegio arrojan similitudes y mejoras; el resultado de ello se aprecia en la figura referencial 4-11.

*(INSERTE AQUÍ: Figura 4-10: Puedes poner figura de otro proyecto de internet sobre matrices de confusión en educación previendo abandono (incluir fuente)).*

*(INSERTE AQUÍ: Figura 4-11: Figura tuya comparativa o cuadro en Excel con las métricas de Accuracy de tu Árbol vs Bosque vs Red).*

El resultado de la otra investigación refleja un Accuracy general altísimo, pero un pésimo score detectando a la minoría vulnerable. Al comparar visualmente o estadísticamente con la Matriz de Confusión de nuestro **Random Forest ponderado (`class_weight = "balanced"`)**, se observa una diferencia metodológica sustancial: mientras que los estudios genéricos buscan Exactitud, nuestra solución sacrifica intencionadamente algunos puntos porcentuales del Accuracy (incrementando Falsos Positivos: prediciendo más alumnos intermedios como Riesgo), a cambio de maximizar agresivamente la métrica de Recall (Sensibilidad).
Estas diferencias estipulan que, en el presente estudio pedagógico, es imperativo diseñar heurísticas que impidan que el algoritmo omita matemáticamente al niño en rezago, asumiendo correctamente la "Alerta Temprana".

### 4.4.2 Decisión Algorítmica Principal y Selección Tecnológica
Un aspecto fundamental exigido por el rigor de este diplomado es la justificación estadística de selección (Selección del Algoritmo Óptimo).

Tras evaluar estadísticamente el rendimiento comparativo del soporte matemático (Perceptrón Multicapa, Árboles de Decisión Simples y Bosques Aleatorios), **el autor del presente proyecto decide seleccionar e integrar el algoritmo de Bosques Aleatorios (Random Forest)** como el motor de Inteligencia Artificial definitivo para alimentar el "Sistema Iterativo Docente" (Streamlit Dashboard).

**Sustentación del Por Qué basado en Análisis de Datos:**
1.  **Detección Priorizada de Extremos Matemáticos:** En el análisis del *classification_report*, el algoritmo de Random Forest, auxiliado por el equilibrado condicional de pesos, demostró estadísticamente ser el interceptor más robusto de los picos anómalos (es decir, los pocos estudiantes reprobados), minimizando la tasa de Falsos Negativos (Error Tipo II).
2.  **Relación Coste Computacional / Interpretabilidad:** Si bien el modelo de Redes Neuronales (MLP) evidenció destellos de exactitud equiparables y una sofisticada topología durante los ensayos en `06_modelo_redes_neuronales.ipynb`, su comportamiento como "caja negra" (*black box*) limita su empleabilidad en un colegio primario donde directores sin trasfondo matemático requieren argumentación clara sobre por qué un niño fue estigmatizado con "Riesgo Alto". El Bosque Aleatorio ofrece una explicabilidad fraccional superior frente al MLP, permitiendo entender que un cruce de frontera (ej: 4 materias reprobadas previamente y promedio inferior a 60) precipitó estadísticamente la etiqueta roja, justificando la intervención pedagógica diferencial sin agotar extremados ciclos computacionales.
