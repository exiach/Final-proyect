# RESUMEN

El rezago académico en educación primaria requiere mecanismos de seguimiento que permitan priorizar la revisión docente. El proyecto desarrolló un prototipo exploratorio de apoyo a la decisión para estimar el riesgo de reprobación en la gestión siguiente en la U.E. José María Santiváñez, utilizando datos históricos de 2022 a 2024.

Se aplicó un enfoque cuantitativo y una adaptación de CRISP-DM. Se consolidaron **1.118 observaciones estudiante-año** correspondientes a 592 estudiantes y 36 boletines. Para el modelado se construyeron **489 transiciones consecutivas T→T+1 con datos completos en ambas gestiones**, de las cuales solo seis fueron positivas. La evaluación temporal utilizó 241 transiciones de 2022→2023 para entrenamiento y 248 de 2023→2024 para prueba. Se compararon Árbol de Decisión, Random Forest y MLP y se implementó una regla pedagógica complementaria claramente diferenciada de la probabilidad estadística.

Comunicación y Lenguajes (2,06 %) y Matemática (1,70 %) presentaron las mayores tasas descriptivas de reprobación. En la prueba temporal, Árbol y Random Forest detectaron uno de tres casos positivos (recall=0,333; precision=0,063), mientras que la MLP no detectó casos positivos. Los resultados son exploratorios debido al reducido número de eventos. El prototipo Streamlit integra monitoreo grupal, ficha individual y simuladores, y muestra por separado la probabilidad del modelo y la alerta operativa.

Se concluye que la integración de datos y el prototipo son técnicamente viables, pero la evidencia disponible no permite afirmar una alta capacidad predictiva. Se requiere ampliar las cohortes, incorporar nuevos indicadores y realizar validación prospectiva antes de un uso institucional. El sistema debe emplearse únicamente como apoyo sujeto a revisión docente.

**Palabras clave:** Minería de datos educativos, Predicción de rezago académico, Sistemas de alerta temprana escolar, Aprendizaje automático supervisado, Bosques aleatorios (*Random Forest*), Apoyo a la decisión docente.
