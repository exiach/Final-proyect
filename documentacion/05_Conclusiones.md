# CAPÍTULO 5: CONCLUSIONES

A la luz de los objetivos planteados y los resultados empíricos alcanzados en el presente proyecto de grado, se establecen las siguientes conclusiones:

- **Consolidación y calidad del dataset**: Se estructuraron 1.118 observaciones estudiante-año de 2022 a 2024, correspondientes a 592 estudiantes únicos. Se identificaron 23 observaciones con al menos una asignatura reprobada y se documentó el alto desbalance.
- **Patrones descriptivos**: En la muestra, **Comunicación y Lenguajes** (2,06 %) y **Matemática** (1,70 %) registraron las mayores tasas de reprobación. Las observaciones con rezago acumularon una media de 4,13 asignaturas reprobadas. Estas asociaciones son descriptivas y no prueban causalidad.
- **Alcance del modelado predictivo**: Se construyeron 489 transiciones consecutivas con datos completos en origen y destino, con solo seis resultados positivos. En la prueba temporal, Árbol y Random Forest detectaron uno de tres casos positivos y la MLP no detectó ninguno. Los modelos constituyen evidencia exploratoria y requieren nuevas cohortes y validación prospectiva.
- **Capa pedagógica**: La regla de dominio evita presentar como bajo riesgo perfiles con calificaciones ya reprobatorias. Su salida se diferencia de la probabilidad del modelo y no se interpreta como validación predictiva.
- **Implementación del sistema de apoyo**: Se implementó un prototipo funcional en *Streamlit* con tres niveles de alerta, una categoría adicional **Sin datos** y un simulador de calificaciones. Las pruebas automatizadas verifican funciones del software; no constituyen validación de impacto pedagógico.
