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
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python scripts/train_models.py
python scripts/sanitize_notebooks.py
python scripts/generate_all_figures.py
python -m unittest discover -s tests -v
```

`resultados_modelos/metricas_modelos.json` registra la fecha UTC, las versiones de
Python y bibliotecas, el orden de variables y la huella SHA-256 del archivo de
entrenamiento. Así se puede comprobar qué datos y entorno produjeron cada artefacto.

## Ejecutar la aplicación

```bash
cd Obj5_Prototipo_Dashboard_Docente
pip install -r requirements.txt
streamlit run app.py
```

La aplicación utiliza el archivo institucional local configurado en `config.py`.
El prototipo no incorpora autenticación ni modos seleccionables mediante variables
de entorno; por ello, no debe publicarse ni desplegarse en un entorno accesible a
terceros.

Los datos originales incluyen información de menores y están excluidos de Git.
No deben publicarse. Para reproducir el proyecto se requiere acceso institucional
autorizado o una versión seudonimizada con el mismo esquema.

La interfaz muestra un código derivado en lugar del RUDE. Los nombres solo deben
visualizarse durante el uso local y por personal autorizado.

Los cuadernos no conservan salidas con datos personales. El entrenamiento y la
evaluación canónicos están en `scripts/train_models.py`; los cuadernos de los
objetivos 3 y 4 solo presentan las métricas generadas por ese pipeline.
