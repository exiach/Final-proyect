# REFERENCIAS BIBLIOGRÁFICAS Y ANEXOS

## Referencias Bibliográficas (Normas APA 7.ª Edición)

Baker, R. S., & Inventado, P. S. (2014). Educational data mining and learning analytics. En J. A. Larusson y B. White (Eds.), *Learning analytics: From research to practice* (pp. 61–75). Springer. https://doi.org/10.1007/978-1-4614-3305-7_4

Breiman, L. (2001). Random forests. *Machine Learning, 45*(1), 5–32. https://doi.org/10.1023/A:1010933404324

Chawla, N. V., Bowyer, K. W., Hall, L. O., & Kegelmeyer, W. P. (2002). SMOTE: Synthetic minority over-sampling technique. *Journal of Artificial Intelligence Research, 16*, 321–357. https://doi.org/10.1613/jair.953

Fawcett, T. (2006). An introduction to ROC analysis. *Pattern Recognition Letters, 27*(8), 861–874. https://doi.org/10.1016/j.patrec.2005.10.010

Goodfellow, I., Bengio, Y., & Courville, A. (2016). *Deep learning*. MIT Press.

Han, J., Kamber, M., & Pei, J. (2012). *Data mining: Concepts and techniques* (3rd ed.). Morgan Kaufmann.

Hastie, T., Tibshirani, R., & Friedman, J. (2009). *The elements of statistical learning* (2nd ed.). Springer. https://doi.org/10.1007/978-0-387-84858-7

Haykin, S. (2009). *Neural networks and learning machines* (3rd ed.). Pearson.

James, G., Witten, D., Hastie, T., & Tibshirani, R. (2013). *An introduction to statistical learning*. Springer. https://doi.org/10.1007/978-1-4614-7138-7

Macfadyen, L. P., & Dawson, S. (2010). Mining LMS data to develop an “early warning system” for educators: A case study. *Computers & Education, 54*(2), 588–599. https://doi.org/10.1016/j.compedu.2009.09.008

Ministerio de Educación del Estado Plurinacional de Bolivia. (2021). *Reglamento de evaluación del desarrollo curricular del Sistema Educativo Plurinacional*.

Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., Blondel, M., Prettenhofer, P., Weiss, R., Dubourg, V., Vanderplas, J., Passos, A., Cournapeau, D., Brucher, M., Perrot, M., & Duchesnay, É. (2011). Scikit-learn: Machine learning in Python. *Journal of Machine Learning Research, 12*, 2825–2830.

Provost, F., & Fawcett, T. (2013). *Data science for business*. O’Reilly Media.

Romero, C., & Ventura, S. (2020). Educational data mining and learning analytics: An updated survey. *WIREs Data Mining and Knowledge Discovery, 10*(3), e1355. https://doi.org/10.1002/widm.1355

Streamlit. (2024). *Streamlit documentation*. https://docs.streamlit.io

Wirth, R., & Hipp, J. (2000). CRISP-DM: Towards a standard process model for data mining. En *Proceedings of the 4th International Conference on the Practical Applications of Knowledge Discovery and Data Mining* (pp. 29–39).

---

## ANEXOS

### Anexo 1: Estructura de Directorios del Código Fuente del Proyecto

```text
/Users/danielcanqui/Projects/Final_Project
├── data/
│   ├── 01_Datos_Originales_PDF/              # Boletines centralizadores originales en PDF
│   ├── 02_Datos_Extraidos_Excel/             # Planillas de Excel extraídas por gestión y grado
│   └── 03_Datasets_Procesados/               # Dataset unificado (primaria_dataset.csv / xlsx)
├── modelos_entrenados/
│   ├── random_forest_model.pkl               # Binario del modelo Random Forest entrenado
│   ├── mlp_model.pkl                         # Binario de la Red Neuronal MLP entrenada
│   └── scaler.pkl                            # Binario del estandarizador StandardScaler
├── notebooks/
│   ├── Obj1_Recoleccion_Limpieza.ipynb       # Extracción, consolidación y limpieza (OE1)
│   ├── Obj2a_Analisis_Patrones.ipynb         # Análisis exploratorio y materias críticas (OE2)
│   ├── Obj3a_Entrenamiento_Arboles_RF.ipynb  # Entrenamiento Árboles y Random Forest (OE3)
│   ├── Obj3b_Entrenamiento_Redes_Neuronales.ipynb # Entrenamiento Red Neuronal MLP (OE3)
│   └── Obj4_Evaluacion_Segregacion_Riesgo.ipynb # Evaluación y umbrales de riesgo (OE4)
├── Obj5_Prototipo_Dashboard_Docente/
│   ├── app.py                                # Punto de entrada principal de la app Streamlit
│   ├── config.py                             # Configuración global, constantes y umbrales
│   ├── requirements.txt                      # Dependencias del proyecto Python
│   └── src/
│       ├── data_loader.py                    # Servicio de carga e integración de nóminas
│       ├── predictor.py                     # Motor predictivo con Capa Híbrida de Resguardo
│       └── ui/                               # Componentes visuales de interfaz Streamlit
└── documentacion/                            # Capítulos de la monografía académica
```

### Anexo 2: Manual de Despliegue y Ejecución del Prototipo en Streamlit

#### 1. Requisitos de Entorno
- Python 3.12+
- Bibliotecas necesarias: `streamlit`, `pandas`, `numpy`, `scikit-learn`, `joblib`, `openpyxl`

#### 2. Comandos de Instalación y Ejecución
```bash
# Navegar al directorio del prototipo (Objetivo 5)
cd Obj5_Prototipo_Dashboard_Docente

# Instalar dependencias requeridas
pip install -r requirements.txt

# Ejecutar la aplicación web interactiva en Streamlit
streamlit run app.py
```

El sistema iniciará automáticamente un servidor web local accesible desde el navegador en `http://localhost:8501`.

---

### Anexo 3: Resumen de Boletines Centralizadores Procesados (2022-2024)

Se procesaron un total de **36 archivos de planillas de centralizadores** correspondientes a:
- **Gestión 2022**: 1.º a 6.º de Primaria (Paralelos A y B)
- **Gestión 2023**: 1.º a 6.º de Primaria (Paralelos A y B)
- **Gestión 2024**: 1.º a 6.º de Primaria (Paralelos A y B)

---

### Anexo 4: Trazabilidad de la Muestra Predictiva

| Etapa | Registros | Casos positivos |
|---|---:|---:|
| Dataset consolidado | 1.118 | 23 observaciones con rezago descriptivo |
| Transiciones consecutivas T→T+1 con origen y destino completos | 489 | 6 |
| Entrenamiento 2022→2023 | 241 | 3 |
| Prueba temporal 2023→2024 | 248 | 3 |

### Anexo 5: Resultados Reproducibles

Las métricas y los hiperparámetros se guardan en `resultados_modelos/metricas_modelos.json`. El comando `python scripts/train_models.py` reconstruye las transiciones, evalúa temporalmente los modelos y exporta los artefactos de despliegue. Las figuras 4.6 y 4.7 se generan desde estos resultados y no contienen valores escritos manualmente.

### Anexo 6: Privacidad y Uso Responsable

El protocolo completo se incluye en `documentacion/08_Protocolo_Privacidad.md`. Los datos originales no forman parte del repositorio Git y cualquier acceso externo requiere autorización institucional y seudonimización.

### Anexo 7: Pruebas del Prototipo

La suite `tests/test_project.py` verifica el esquema de archivos cargados, los rangos de notas, el rechazo de columnas faltantes y la separación entre probabilidad del modelo y regla pedagógica.

---

### Anexo 8: Códigos QR y Enlaces a Recursos Digitales

Para facilitar la verificación y reproducción de los resultados, se disponen los accesos directos digitales:

| Recurso Digital | Descripción | Código QR |
| :--- | :--- | :---: |
| **Repositorio GitHub** | Código fuente, notebooks de modelado y aplicación Streamlit.<br>Enlace: [github.com/exiach/Final-proyect](https://github.com/exiach/Final-proyect) | ![QR GitHub](file:///Users/danielcanqui/Projects/Final_Project/documentacion/figuras/qr_github.png) |
| **Carpeta Google Drive restringida** | Material autorizado para evaluación. No debe conceder acceso público a datos identificables de menores.<br>Enlace: [Carpeta de Recursos Drive](https://drive.google.com/drive/folders/1PQvYRbyuSNka2ZJkGrQ1J6fSVhsV317g?usp=sharing) | ![QR Google Drive](file:///Users/danielcanqui/Projects/Final_Project/documentacion/figuras/qr_drive.png) |
