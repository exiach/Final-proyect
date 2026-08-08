# CAPÍTULO 3: METODOLOGÍA Y DESARROLLO DEL PROYECTO

## 3.1 Enfoque de Investigación y Metodología CRISP-DM

El proyecto adopta un enfoque de investigación aplicada de tipo cuantitativo y explicativo-predictivo. Para guiar el ciclo de vida del desarrollo de la solución analítica, se empleó la metodología estándar de la industria **CRISP-DM** (*Cross-Industry Standard Process for Data Mining*), estructurada en seis fases adaptadas al contexto educativo de la U.E. José María Santiváñez:

```text
[Fase 1: Comprensión del Negocio Educativo]
       │
       ▼
[Fase 2: Comprensión de los Datos (Boletines 2021-2024)]
       │
       ▼
[Fase 3: Preparación de Datos & Ingeniería Longitudinal]
       │
       ▼
[Fase 4: Modelado Predictivo (Decision Tree, RF, MLP)]
       │
       ▼
[Fase 5: Evaluación & Segregación por Niveles de Riesgo]
       │
       ▼
[Fase 6: Despliegue del Prototipo Docente en Streamlit]
```

![Figura 3.1: Flujograma Metodológico CRISP-DM adaptado al Proyecto](file:///Users/danielcanqui/Projects/Final_Project/documentacion/figuras/fig_3_1_flujograma_crisp_dm.png)

---

## 3.2 Comprensión del Negocio y del Entorno Educativo

En esta fase inicial se identificaron las necesidades operativas de la U.E. José María Santiváñez en la ciudad de Cochabamba. La institución imparte educación en el nivel de Educación Primaria Comunitaria Vocacional (grados 1.º a 6.º de primaria, paralelos A y B). La evaluación se efectúa de acuerdo al marco normativo vigente en Bolivia (Ministerio de Educación, 2021), considerando 9 asignaturas fundamentales:
1. Comunicación y Lenguajes (`com_lenguajes`)
2. Ciencias Sociales (`cs_sociales`)
3. Educación Física y Deportes (`edu_fisica`)
4. Educación Musical (`edu_musical`)
5. Artes Plásticas y Visuales (`art_plasticas`)
6. Matemática (`matematica`)
7. Técnica Tecnológica (`tec_tecnologica`)
8. Ciencias Naturales (`cs_naturales`)
9. Valores, Espiritualidad y Religiones (`valores_religion`)

---

## 3.3 Recopilación y Consolidación de Datos Históricos (Objetivo 1)

Los datos originales consistían en 36 archivos independientes en formato PDF resultantes de las evaluaciones centralizadoras de las gestiones 2021, 2022, 2023 y 2024. Mediante herramientas de conversión documental, estos archivos fueron transformados a planillas de Excel (`data/02_Datos_Extraidos_Excel`).

### 3.3.1 Proceso de Extracción y Limpieza
Para automatizar la consolidación de los boletines heterogéneos, se diseñó la función `limpiar_boletin_v2()` en el cuaderno `Obj1_Recoleccion_Limpieza.ipynb`. Esta función identifica dinámicamente la fila de encabezados mediante la búsqueda de palabras clave como `"PATERNO"`, `"NOMBRES"` o `"RUDE"`, descarta filas de metadatos institucionales y estandariza los nombres de las columnas.

```python
# Snippet 3.1: Función de extracción y homogenización de boletines escolares
# Extraído de: notebooks/Obj1_Recoleccion_Limpieza.ipynb

def limpiar_boletin_v2(path):
    import pandas as pd
    import os
    raw = pd.read_excel(path, header=None, engine="openpyxl")
    
    # Detectar dinámicamente la fila donde inician los datos del centralizador
    start_row = None
    for i in range(len(raw)):
        row_str = raw.iloc[i].astype(str).str.upper().tolist()
        if any("PATERNO" in cell or "NOMBRES" in cell or "RUDE" in cell for cell in row_str):
            start_row = i
            break
            
    if start_row is None:
        raise ValueError(f"No se encontró fila de encabezados en {path}")
        
    df = pd.read_excel(path, skiprows=start_row, engine="openpyxl")
    
    # Normalizar nombres de columnas a minúsculas sin espacios
    df.columns = (
        df.columns.astype(str)
        .str.strip()
        .str.lower()
        .str.replace("\n", "")
        .str.replace(" ", "_")
    )
    
    # Extraer metadatos de año escolar y paralelo desde el nombre del archivo
    filename = os.path.basename(path)
    df["archivo_origen"] = filename
    return df
```

### 3.3.2 Consolidación y Construcción de la Variable 'Rezago'
Tras procesar los 36 archivos, se obtuvo un total de **1,118 registros de estudiantes**. Sobre esta estructura se calcularon las métricas agregadas y la variable dependiente `rezago`:

```python
# Snippet 3.2: Consolidación del dataset y creación de la variable target 'rezago'
# Extraído de: notebooks/Obj1_Recoleccion_Limpieza.ipynb

import glob, os, pandas as pd

materias = [
    "com_lenguajes", "cs_sociales", "edu_fisica", "edu_musical",
    "art_plasticas", "matematica", "tec_tecnologica", "cs_naturales",
    "valores_religion"
]

# Definición de la condición de reprobación (nota < 51) y variable rezago
dataset["num_materias_reprobadas"] = (dataset[materias] < 51).sum(axis=1)
dataset["promedio_general"] = dataset[materias].mean(axis=1)
dataset["rezago"] = (dataset["num_materias_reprobadas"] > 0).astype(int)

# Exportación del conjunto consolidado
dataset.to_csv("../data/03_Datasets_Procesados/primaria_dataset.csv", index=False, encoding="utf-8")
```

---

## 3.4 Análisis Exploratorio de Datos e Identificación de Patrones (Objetivo 2)

En el cuaderno `Obj2a_Analisis_Patrones.ipynb` se ejecutó un análisis descriptivo riguroso para caracterizar el desempeño académico de la población estudiantil.

### 3.4.1 Identificación de Materias Críticas de Reprobación
Se evaluó la tasa de reprobación porcentual por cada asignatura sobre el total de registros observados:

```python
# Snippet 3.3: Cálculo de la tasa de reprobación por asignatura
# Extraído de: notebooks/Obj2a_Analisis_Patrones.ipynb

materias_criticas = (dataset[materias] < 51).mean().sort_values(ascending=False) * 100
print(materias_criticas)
```

Los resultados empíricos revelaron que **Comunicación y Lenguajes** ($2.06\%$) y **Matemática** ($1.70\%$) constituyen las áreas de mayor vulnerabilidad académica en el nivel primario.

### 3.4.2 Comparación de Medias por Condición de Rezago
El análisis comparativo de promedios entre estudiantes aprobados ($rezago=0$) y rezagados ($rezago=1$) demostró que los alumnos en riesgo sufren un deterioro generalizado en todas las áreas del conocimiento:

```python
# Snippet 3.4: Comparación de promedios por grupo de rezago
# Extraído de: notebooks/Obj2a_Analisis_Patrones.ipynb

promedios_por_grupo = dataset.groupby("rezago")[materias].mean()
```

---

## 3.5 Ingeniería de Características y Transformación Longitudinal (Objetivo 3)

Para predecir el riesgo de rezago académico en una gestión futura a partir del desempeño previo del alumno, se aplicó una transformación de estructura temporal en los cuadernos `Obj3b` y `Obj4`. Se ordenó el conjunto de datos por el identificador único del estudiante (`rude`) y el año académico (`gestion`), aplicando operaciones de desplazamiento (*shifting*):

```python
# Snippet 3.5: Ingeniería de características históricas previas (shift temporal)
# Extraído de: notebooks/Obj3b_Entrenamiento_Redes_Neuronales.ipynb

# Ordenar secuencialmente por estudiante y año
dataset = dataset.sort_values(["rude", "gestion"]).reset_index(drop=True)

# Crear variables descriptivas del año anterior
features_base = ["promedio_general", "num_materias_reprobadas"]
for col in features_base:
    dataset[f"{col}_prev"] = dataset.groupby("rude")[col].shift(1)

# Crear la variable objetivo a predecir (rezago en la siguiente gestión)
dataset["rezago_next"] = dataset.groupby("rude")["rezago"].shift(-1)

# Filtrar únicamente registros que poseen historial completo previo y posterior
model_data = dataset.dropna(subset=["promedio_general_prev", "num_materias_reprobadas_prev", "rezago_next"])
```

---

## 3.6 Diseño, Entrenamiento e Hiperparametrización de Modelos Predictivos (Objetivo 3)

Se experimentó con tres arquitecturas de clasificación supervisada para anticipar el rezago futuro (`rezago_next`):

### 3.6.1 Árbol de Decisión (`DecisionTreeClassifier`)
Entrenado con restricción de profundidad máxima (`max_depth=4`) para prevenir el sobreajuste y mantener la interpretabilidad de las reglas de decisión (`Obj3a_Entrenamiento_Arboles_RF.ipynb`).

### 3.6.2 Random Forest Balanceado (`RandomForestClassifier`)
Configurado con 200 estimadores y ponderación balanceada de clases para contrarrestar el desbalance de datos:

```python
# Snippet 3.6: Entrenamiento de Random Forest con ponderación de clases
# Extraído de: notebooks/Obj3a_Entrenamiento_Arboles_RF.ipynb y Obj4

from sklearn.ensemble import RandomForestClassifier

rf_model = RandomForestClassifier(
    n_estimators=200,
    max_depth=5,
    class_weight="balanced",
    random_state=42
)

rf_model.fit(X_train, y_train)
```

### 3.6.3 Red Neuronal MLP (`MLPClassifier`)
Implementada en `Obj3b_Entrenamiento_Redes_Neuronales.ipynb` previa estandarización de características mediante `StandardScaler`:

```python
# Snippet 3.7: Estandarización y entrenamiento del Perceptrón Multicapa (MLP)
# Extraído de: notebooks/Obj3b_Entrenamiento_Redes_Neuronales.ipynb

from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

mlp_model = MLPClassifier(
    hidden_layer_sizes=(10, 10),
    activation="relu",
    solver="adam",
    max_iter=500,
    random_state=42
)

mlp_model.fit(X_train_scaled, y_train)
```

---

## 3.7 Evaluación Comparativa y Segregación de Niveles de Riesgo (Objetivo 4)

Los modelos fueron evaluados sobre el conjunto de prueba independiente mediante partición estratificada (`test_size=0.3`, `stratify=y`). 

Para operativizar los resultados en la práctica pedagógica, la probabilidad estimada por el modelo $P(Y=1 \mid \mathbf{x})$ se mapea a tres categorías de riesgo mediante la función `nivel_riesgo()`:

```python
# Snippet 3.8: Lógica de segregación de niveles de riesgo
# Extraído de: notebooks/Obj4_Evaluacion_Segregacion_Riesgo.ipynb

def nivel_riesgo(p):
    if p >= 0.70:
        return "Alto"
    elif p >= 0.40:
        return "Medio"
    else:
        return "Bajo"

model_data["nivel_riesgo"] = model_data["prob_rezago"].apply(nivel_riesgo)
```

---

## 3.8 Diseño e Implementación del Prototipo de Apoyo a la Decisión Docente (Objetivo 5)

El prototipo del **Sistema de Alertas Tempranas para la Prevención de Rezago Escolar** fue desarrollado como una aplicación web en *Streamlit* dentro del directorio `Obj5_Prototipo_Dashboard_Docente`.

### 3.8.1 Arquitectura Modular del Software
El sistema está estructurado bajo principios de modularidad y separación de responsabilidades:
- `app.py`: Punto de entrada principal y coordinador del flujo de renderizado.
- `config.py`: Definición de constantes, umbrales institucionales (`MIN_APROBACION_NOTA = 51.0`) y paleta de colores de alerta.
- `src/data_loader.py`: Servicio de lectura de datasets base e integración de nuevas nóminas 2025 subidas por el usuario.
- `src/predictor.py`: Servicio de carga de modelos serializados (`.pkl`) y motor de inferencia con Capa Híbrida.
- `src/ui/`: Componentes modulares de interfaz gráfica (barra de filtros, sidebar, tabs de monitoreo y simuladores).

![Figura 3.2: Arquitectura de Software del Prototipo de Apoyo Docente](file:///Users/danielcanqui/Projects/Final_Project/documentacion/figuras/fig_3_2_arquitectura_software.png)

### 3.8.2 Capa de Resguardo Pedagógico Normativo (Sistema Híbrido)
Para asegurar que la herramienta sea 100% confiable y no emita falsos negativos frente a alumnos con notas reprobatorias, el archivo `src/predictor.py` encapsula la lógica híbrida:

```python
# Snippet 3.9: Motor predictivo híbrido con Capa de Resguardo Pedagógico Normativo
# Extraído de: Obj5_Prototipo_Dashboard_Docente/src/predictor.py

def predict_student_risk(promedio, reprobadas, modelo_nombre, rf_model, mlp_model, scaler):
    input_data = pd.DataFrame({
        "promedio_general_prev": [promedio],
        "num_materias_reprobadas_prev": [reprobadas]
    })
    
    # Inferencia probabilística del modelo ML seleccionado
    if "Random Forest" in modelo_nombre:
        prob = float(rf_model.predict_proba(input_data)[0][1])
    else:
        input_scaled = scaler.transform(input_data)
        prob = float(mlp_model.predict_proba(input_scaled)[0][1])
        
    # --- CAPA DE RESGUARDO PEDAGÓGICO NORMATIVO ---
    # Garantiza que cualquier alumno con promedio < 51 o >= 2 materias reprobadas sea clasificado en ALTO RIESGO
    if promedio < 51.0 or reprobadas >= 2:
        prob = max(prob, 0.85)
    elif reprobadas == 1 or (51.0 <= promedio < 60.0):
        prob = max(prob, 0.50)

    # Categorización en umbrales de alerta
    if prob >= 0.70:
        cat = "Alto Riesgo"
    elif prob >= 0.40:
        cat = "Medio Riesgo"
    else:
        cat = "Bajo Riesgo"
        
    info = PALETA_RIESGO[cat]
    return prob, cat, info["color"], info["badge"], info["rec"]
```

![Figura 3.3: Diagrama de Flujo de la Capa Híbrida de Resguardo Pedagógico](file:///Users/danielcanqui/Projects/Final_Project/documentacion/figuras/fig_3_3_capa_hibrida_resguardo.png)

