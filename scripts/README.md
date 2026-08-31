# Scripts reproducibles del proyecto

Esta carpeta conserva únicamente los scripts necesarios para reproducir los
resultados vinculados con los objetivos del proyecto:

- `train_models.py`: construye las transiciones T→T+1, entrena y evalúa los
  modelos, y exporta los artefactos empleados por el prototipo (OE3 y OE4).
- `generate_all_figures.py`: genera las figuras académicas a partir de los datos
  procesados y de las métricas reproducibles (evidencia de OE1, OE2 y OE4).
- `sanitize_notebooks.py`: prepara los notebooks para la entrega, elimina salidas
  sensibles y mantiene una presentación reproducible de OE1–OE4.

Los comandos recomendados se encuentran en el `README.md` de la raíz.
