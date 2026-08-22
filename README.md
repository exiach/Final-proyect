# Sistema de apoyo a la decisión docente

Prototipo exploratorio para estimar riesgo de rezago académico en la gestión
siguiente utilizando registros de primaria de 2022 a 2024.

## Evidencia disponible

- 1.118 observaciones estudiante-año y 592 estudiantes únicos.
- 489 transiciones consecutivas T -> T+1 con datos completos en origen y destino.
- 6 transiciones positivas de rezago.
- Evaluación temporal: entrenamiento 2022->2023 y prueba 2023->2024.
- 88 observaciones con calificaciones incompletas; el prototipo las muestra como
  `Sin datos` y no calcula una alerta.

La escasez de positivos impide considerar los modelos como validados para uso
autónomo. La aplicación es una prueba de concepto y mantiene el criterio docente
como decisión final.

## Reproducir modelos y figuras

```bash
python scripts/train_models.py
python scripts/generate_all_figures.py
python -m unittest discover -s tests -v
```

## Ejecutar la aplicación

```bash
cd Obj5_Prototipo_Dashboard_Docente
pip install -r requirements.txt
streamlit run app.py
```

Los datos originales incluyen información de menores y están excluidos de Git.
No deben publicarse. Para reproducir el proyecto se requiere acceso institucional
autorizado o una versión seudonimizada con el mismo esquema.

Los cuadernos no conservan salidas con datos personales. El entrenamiento y la
evaluación canónicos están en `scripts/train_models.py`; los cuadernos de los
objetivos 3 y 4 solo presentan las métricas generadas por ese pipeline.
