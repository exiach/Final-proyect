# REFERENCIAS BIBLIOGRÁFICAS Y ANEXOS

## Referencias Bibliográficas (Normas APA 7.ª Edición)

1. Aguiar, E. H., & Morales, L. (2021). Educational Data Mining and Learning Analytics: Applications in early warning systems. *IEEE Transactions on Learning Technologies*, 14(3), 345–358. https://doi.org/10.1109/TLT.2021.3089123
2. Breiman, L. (2001). Random Forests. *Machine Learning*, 45(1), 5–32. https://doi.org/10.1023/A:1010933404324
3. Chawla, N. V., Bowyer, K. W., Hall, L. O., & Kegelmeyer, W. P. (2002). SMOTE: Synthetic Minority Over-sampling Technique. *Journal of Artificial Intelligence Research*, 16, 321–357. https://doi.org/10.1613/jair.953
4. De-La-Peña, C., & Luque-Rojas, M. J. (2021). Niveles de rendimiento académico y factores de riesgo en educación primaria. *Revista de Investigación Educativa*, 39(2), 411–427. https://doi.org/10.6018/rie.434101
5. Haykin, S. (2009). *Neural Networks and Learning Machines* (3rd ed.). Pearson Education.
6. Macfadyen, L. P., & Dawson, S. (2010). Mining LMS data to develop an “early warning system” for educators: A case study. *Computers & Education*, 54(2), 588–599. https://doi.org/10.1016/j.compedu.2009.09.008
7. Ministerio de Educación del Estado Plurinacional de Bolivia. (2021). *Reglamento de evaluación del desarrollo curricular del Sistema Educativo Plurinacional*. La Paz, Bolivia.
8. Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., Blondel, M., Prettenhofer, P., Weiss, R., Dubourg, V., Vanderplas, J., Passos, A., Cournapeau, D., Brucher, M., Perrot, M., & Duchesnay, É. (2011). Scikit-learn: Machine Learning in Python. *Journal of Machine Learning Research*, 12, 2825–2830.
9. Romero, C., & Ventura, S. (2020). Educational Data Mining and Learning Analytics: An updated survey. *WIREs Data Mining and Knowledge Discovery*, 10(3), e1355. https://doi.org/10.1002/widm.1355
10. Streamlit Inc. (2024). *Streamlit Documentation: Building interactive data applications in Python*. https://docs.streamlit.io

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

### Anexo 3: Resumen de Boletines Centralizadores Procesados (2021-2024)

Se procesaron un total de **36 archivos de planillas de centralizadores** correspondientes a:
- **Gestión 2021**: 1.º a 6.º de Primaria (Paralelos A y B)
- **Gestión 2022**: 1.º a 6.º de Primaria (Paralelos A y B)
- **Gestión 2023**: 1.º a 6.º de Primaria (Paralelos A y B)
- **Gestión 2024**: 1.º a 6.º de Primaria (Paralelos A y B)
