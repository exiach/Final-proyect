# CAPÍTULO 5: CONCLUSIONES Y RECOMENDACIONES

## 5.1 Conclusiones

A la luz de los resultados obtenidos y en estricta correspondencia con los objetivos formulados en la investigación, se presentan las siguientes conclusiones:

### 5.1.1 En relación al Objetivo Específico 1 (Recolectar y depurar datos)
Se logró recolectar, estructurar y depurar exitosamente la información académica histórica de la U.E. José María Santiváñez correspondiente a las gestiones 2021, 2022, 2023 y 2024, mediante el procesamiento programático de 36 boletines centralizadores. Este proceso permitió consolidar un **dataset único y estandarizado de 1,118 registros estudiantil-año** y 9 asignaturas curriculares, identificando una tasa histórica de rezago académico del **2.06% (23 casos)** sobre el total de observaciones, sentando la base de datos necesaria para la analítica educativa.

### 5.1.2 En relación al Objetivo Específico 2 (Analizar patrones y materias críticas)
El Análisis Exploratorio de Datos (EDA) permitió determinar empíricamente que **Comunicación y Lenguajes** ($2.06\%$ de tasa de reprobación) y **Matemática** ($1.70\%$) constituyen las materias críticas primarias de vulnerabilidad en la educación primaria de la institución. Asimismo, se demostró que los estudiantes en rezago no reprueban de forma aislada, sino que acumulan una media de **4.13 asignaturas reprobadas simultáneamente**, registrando brechas de hasta 28.5 puntos en sus promedios respecto al grupo no rezagado.

### 5.1.3 En relación al Objetivo Específico 3 (Diseñar y entrenar modelos predictivos)
Se diseñaron, implementaron y entrenaron tres arquitecturas de clasificación supervisada (Árbol de Decisión, Random Forest y Red Neuronal Perceptrón Multicapa - MLP) utilizando características históricas del año anterior (`promedio_general_prev`, `num_materias_reprobadas_prev`). El modelo **Random Forest** con ponderación de clases (`class_weight='balanced'`) demostró ser la arquitectura más sólida para gestionar el desbalance inherente de los datos escolares sin distorsionar la sensibilidad del sistema.

### 5.1.4 En relación al Objetivo Específico 4 (Evaluar y segregar en grupos de riesgo)
Se estableció un esquema cuantitativo de segregación estudiantil en tres niveles de alerta: **Alto Riesgo** ($P \ge 0.70$), **Medio Riesgo** ($0.40 \le P < 0.70$) y **Bajo Riesgo** ($P < 0.40$). La evaluación sobre conjuntos de prueba independientes evidenció la necesidad de complementar la probabilidad predictiva con reglas de negocio institucionales para garantizar la máxima cobertura operativa frente al riesgo escolar.

### 5.1.5 En relación al Objetivo Específico 5 (Proponer un prototipo de apoyo docente)
Se desarrolló e implementó un prototipo funcional del **Sistema de Alertas Tempranas para el Apoyo a la Decisión Docente** como aplicación web en *Streamlit*. La inclusión de la **Capa Híbrida de Resguardo Pedagógico Normativo** aseguró una fiabilidad del 100% en la detección de alumnos reprobados, proporcionando a los docentes tres pestañas de navegación (Monitoreo de Curso, Ficha de Estudiante & Simulador de Notas, y Simulador Libre) e ingesta dinámica de nóminas 2025.

### 5.1.6 Conclusión General del Proyecto
Se cumplió satisfactoriamente el Objetivo General de la investigación al desarrollar un modelo predictivo e integrarlo en una plataforma de apoyo a la decisión docente basada en Machine Learning y datos multi-años y multi-cursos. El sistema alcanzado demuestra la viabilidad técnica y pedagógica de anticipar el rezago académico en la U.E. José María Santiváñez, proveyendo un instrumento científico que respalda la intervención oportuna sin reemplazar el criterio del maestro.

---

## 5.2 Recomendaciones

### 5.2.1 Recomendaciones Institucionales para la U.E. José María Santiváñez
1. **Adopción del Prototipo Docente**: Se recomienda a la Dirección General y Comisión Pedagógica de la U.E. José María Santiváñez institucionalizar el uso del prototipo de alertas tempranas al inicio de cada bimestre escolar para identificar a los alumnos categorizados en Alto y Medio Riesgo.
2. **Refuerzo Prioritario en Materias Críticas**: Canalizar los recursos de apoyo pedagógico y clases de nivelación de manera prioritaria hacia las áreas de *Comunicación y Lenguajes* y *Matemática*, al haber sido identificadas empíricamente como las de mayor impacto en la reprobación.
3. **Estandarización de Registros Digitales**: Establecer un formato digital único para la elaboración de centralizadores de calificaciones en hojas de cálculo Excel, evitando variaciones de nombres o formatos que dificulten la ingesta automatizada en el sistema analítico.

### 5.2.2 Recomendaciones Pedagógicas para el Cuerpo Docente
1. **Intervención Diferenciada por Niveles de Riesgo**:
   - **Alto Riesgo (🔴)**: Convocar a reunión inmediata con padres de familia, elaborar un plan de acompañamiento individualizado y asignar tutorías intensivas semanales.
   - **Medio Riesgo (🟡)**: Realizar seguimiento bimensual de calificaciones y aplicar guías de refuerzo en asignaturas críticas.
   - **Bajo Riesgo (🟢)**: Mantener el acompañamiento estándar y promover el aprendizaje colaborativo.
2. **Uso del Simulador de Notas**: Utilizar la pestaña de *Ficha de Estudiante & Simulador de Notas* para proyectar escenarios de mejora con el alumno, mostrándole cuantitativamente cuántos puntos requiere incrementar en las materias vulnerables para salir de la zona de riesgo.

---

## 5.3 Trabajos Futuros y Líneas de Investigación

1. **Ampliación al Nivel Secundario**: Adaptar la arquitectura del sistema y los modelos predictivos para abarcar el nivel de Educación Secundaria Comunitaria Productiva, incorporando la mayor complejidad de materias especializadas.
2. **Inclusión de Variables Cualitativas y Socioeconómicas**: Enriquecer el vector de características de entrada incorporando variables de asistencia escolar, composición familiar e indicadores socioeconómicos del estudiante.
3. **Automatización de Pipelines MLOps**: Implementar un pipeline de *MLOps* con reentrenamiento automatizado que actualice periódicamente los ponderadores de los modelos a medida que se registren los boletines de cada nueva gestión escolar.
