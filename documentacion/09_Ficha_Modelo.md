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

| Modelo | Matriz de confusión | Precision rezago | Recall rezago | F1 rezago | Balanced accuracy |
|---|---|---:|---:|---:|---:|
| Árbol de decisión | [[232, 13], [2, 1]] | 0,0714 | 0,3333 | 0,1176 | 0,6401 |
| Random Forest | [[232, 13], [2, 1]] | 0,0714 | 0,3333 | 0,1176 | 0,6401 |
| MLP | [[245, 0], [3, 0]] | 0 | 0 | 0 | 0,5000 |

## Limitaciones

Solo hay seis transiciones positivas. Las métricas son inestables y no prueban
generalización. La capa pedagógica es una regla operativa separada del modelo y
no debe interpretarse como mejora estadística de su probabilidad.
