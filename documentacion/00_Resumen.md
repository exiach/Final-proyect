# RESUMEN

El rezago académico en educación primaria compromete la continuidad escolar si no se interviene oportunamente. El presente proyecto de grado tuvo como objetivo desarrollar un sistema predictivo de apoyo a la decisión docente para la detección temprana del rezago escolar en la U.E. José María Santiváñez, empleando modelos de *Machine Learning* sobre datos históricos multi-años (2021–2024).

La metodología comprendió un enfoque cuantitativo y aplicado. Se consolidó un dataset de **1,118 registros estudiantil-año** a partir de 36 boletines centralizadores. Ante una tasa histórica de rezago del **2.06%** (23 casos), se evaluaron tres algoritmos supervisados (*Árbol de Decisión*, *Random Forest* y *Red Neuronal MLP*). Para garantizar la aplicabilidad práctica, se incorporó una **Capa Híbrida de Resguardo Normativo** y se construyó un prototipo web interactivo en *Streamlit* con módulos de monitoreo grupal, fichas individuales y simulador de calificaciones.

Los resultados determinaron que **Comunicación y Lenguajes** ($2.06\%$ de reprobación) y **Matemática** ($1.70\%$) constituyen las asignaturas críticas primarias, acumulando los estudiantes en rezago una media de **4.13 materias reprobadas simultáneamente**. La arquitectura **Random Forest** (balanceada) integrada con la Capa Híbrida alcanzó una fiabilidad operativa del **100%** en la segregación de tres niveles de alerta: **Alto** ($P \ge 0.70$), **Medio** ($0.40 \le P < 0.70$) y **Bajo Riesgo** ($P < 0.40$).

Se concluye que la minería de datos educativos permite anticipar con alta precisión el riesgo de reprobación, transformando registros históricos en herramientas preventivas objetivas que fortalecen la toma de decisiones pedagógicas sin sustituir el criterio profesional del maestro.

**Palabras clave:** Minería de datos educativos, Predicción de rezago académico, Sistemas de alerta temprana escolar, Aprendizaje automático supervisado, Bosques aleatorios (*Random Forest*), Apoyo a la decisión docente.
