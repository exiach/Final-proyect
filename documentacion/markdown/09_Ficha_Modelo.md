# Ficha del modelo

## Propósito

Estimar de forma exploratoria el riesgo de que un estudiante presente al menos
una asignatura reprobada en la gestión T+1, a partir del promedio general y el
número de asignaturas reprobadas en la gestión T.

## Datos y evaluación

- Periodo: 2022-2024.
- Dataset consolidado: 1.118 observaciones y 592 estudiantes únicos.
- Transiciones consecutivas con origen y destino completos: 489, con 6 positivas.
- Entrenamiento temporal: 2022->2023, N=241, 3 positivas.
- Prueba temporal: 2023->2024, N=248, 3 positivas.
- Registros descriptivos sin las nueve calificaciones: 88; no reciben predicción
  en el prototipo hasta completar la información.

## Resultados a umbral 0,50

| Modelo | Matriz de confusión | Precisión (+) | Recall (+) | F1 (+) | Balanced accuracy | Average precision |
|---|---|---:|---:|---:|---:|---:|
| Línea base: siempre sin rezago | [[245, 0], [3, 0]] | 0 | 0 | 0 | 0,5000 | 0,0121 |
| Árbol de decisión | [[232, 13], [2, 1]] | 0,0714 | 0,3333 | 0,1176 | 0,6401 | 0,0319 |
| Random Forest | [[232, 13], [2, 1]] | 0,0714 | 0,3333 | 0,1176 | 0,6401 | 0,0636 |
| MLP | [[245, 0], [3, 0]] | 0 | 0 | 0 | 0,5000 | 0,2332 |

La MLP presenta mayor *average precision*, pero no detecta positivos al umbral
0,50. Por ello ese valor no demuestra superioridad operativa.

## Trazabilidad del artefacto

`resultados_modelos/metricas_modelos.json` registra versión del artefacto, fecha
UTC de entrenamiento, orden de variables, versiones del entorno y SHA-256 del
dataset. Estos datos se regeneran con `python scripts/train_models.py`.

## Limitaciones

Solo hay seis transiciones positivas. Las métricas son inestables y no prueban
generalización. La capa pedagógica es una regla operativa separada del modelo y
no debe interpretarse como mejora estadística de su probabilidad.
