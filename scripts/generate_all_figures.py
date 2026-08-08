import os
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
from sklearn.metrics import confusion_matrix

# Set global style for crisp academic publication figures
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 11
plt.rcParams['axes.titlesize'] = 12
plt.rcParams['axes.labelsize'] = 11

FIG_DIR = os.path.abspath("documentacion/figuras")
os.makedirs(FIG_DIR, exist_ok=True)

# Load real dataset
DATA_PATH = os.path.abspath("data/03_Datasets_Procesados/primaria_dataset.csv")
dataset = pd.read_csv(DATA_PATH)

materias = [
    "com_lenguajes", "cs_sociales", "edu_fisica", "edu_musical",
    "art_plasticas", "matematica", "tec_tecnologica", "cs_naturales",
    "valores_religion"
]

nombres_materias = {
    'com_lenguajes': 'Comunicación y Lenguajes',
    'matematica': 'Matemática',
    'cs_naturales': 'Ciencias Naturales',
    'cs_sociales': 'Ciencias Sociales',
    'valores_religion': 'Valores y Religión',
    'tec_tecnologica': 'Técnica Tecnológica',
    'edu_musical': 'Educación Musical',
    'art_plasticas': 'Artes Plásticas',
    'edu_fisica': 'Educación Física'
}

# ==============================================================================
# FIGURA 3.1: FLUJOGRAMA METODOLÓGICO CRISP-DM (ESTILO DRAW.IO)
# ==============================================================================
def gen_fig_3_1():
    fig, ax = plt.subplots(figsize=(12, 7.5), dpi=300)
    ax.axis('off')
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    
    # Draw.io Classic Palette: Soft Blue #DAE8FC, Border #6C8EBF
    bg_color = "#DAE8FC"
    border_color = "#6C8EBF"
    header_color = "#6C8EBF"
    
    phases = [
        ("1. Comprensión del Negocio", "Definición del rezago (nota < 51)\ny entorno U.E. Santiváñez", (0.6, 5.0)),
        ("2. Comprensión de Datos", "Consolidación de 36 boletines PDF\ny 1,118 registros de primaria", (4.6, 5.0)),
        ("3. Preparación de Datos", "Limpieza de nulos, feature shift\n(prev/next) e imputación", (8.6, 5.0)),
        ("6. Despliegue de Prototipo", "Aplicación web Streamlit con\nCapa Híbrida de Resguardo", (0.6, 1.2)),
        ("5. Evaluación & Segregación", "Partición estratificada, matrices\ny umbrales Alto/Medio/Bajo", (4.6, 1.2)),
        ("4. Modelado Predictivo", "Entrenamiento Decision Tree, RF\n(class_weight='balanced') y MLP", (8.6, 1.2))
    ]
    
    for title, desc, (x, y) in phases:
        # Draw.io Rounded Process Box
        box = mpatches.FancyBboxPatch((x, y), 2.8, 1.8, boxstyle="round,pad=0.04", 
                                      ec=border_color, fc=bg_color, lw=1.8)
        ax.add_patch(box)
        
        # Draw.io Title Header Bar
        banner = mpatches.FancyBboxPatch((x, y + 1.25), 2.8, 0.55, boxstyle="round,pad=0.01", 
                                         ec=border_color, fc=header_color, lw=1)
        ax.add_patch(banner)
        
        ax.text(x + 1.4, y + 1.52, title, color='white', weight='bold', fontsize=10, ha='center', va='center')
        ax.text(x + 1.4, y + 0.65, desc, color='#1A1A1A', fontsize=9.5, ha='center', va='center', multialignment='center', linespacing=1.3)

    # Draw.io Connectors (Orthogonal arrows with solid arrowheads)
    # Top Row
    ax.annotate('', xy=(4.5, 5.9), xytext=(3.5, 5.9), arrowprops=dict(arrowstyle="-|>", color="#4D4D4D", lw=2, mutation_scale=15))
    ax.annotate('', xy=(8.5, 5.9), xytext=(7.5, 5.9), arrowprops=dict(arrowstyle="-|>", color="#4D4D4D", lw=2, mutation_scale=15))
    
    # Right Drop
    ax.annotate('', xy=(10.0, 3.1), xytext=(10.0, 4.9), arrowprops=dict(arrowstyle="-|>", color="#4D4D4D", lw=2, mutation_scale=15))
    
    # Bottom Row
    ax.annotate('', xy=(7.5, 2.1), xytext=(8.5, 2.1), arrowprops=dict(arrowstyle="-|>", color="#4D4D4D", lw=2, mutation_scale=15))
    ax.annotate('', xy=(3.5, 2.1), xytext=(4.5, 2.1), arrowprops=dict(arrowstyle="-|>", color="#4D4D4D", lw=2, mutation_scale=15))
    
    # Left Return (CRISP-DM Iterative Loop)
    ax.annotate('', xy=(2.0, 4.9), xytext=(2.0, 3.1), arrowprops=dict(arrowstyle="-|>", color="#4D4D4D", lw=2, mutation_scale=15, linestyle='--'))
    
    plt.tight_layout()
    plt.savefig(os.path.join(FIG_DIR, "fig_3_1_flujograma_crisp_dm.png"), dpi=300, bbox_inches='tight')
    plt.close()
    print("Generated fig_3_1_flujograma_crisp_dm.png (Draw.io Vector Style)")

# ==============================================================================
# FIGURA 3.2: ARQUITECTURA DE SOFTWARE DEL PROTOTIPO (ESTILO DRAW.IO)
# ==============================================================================
def gen_fig_3_2():
    fig, ax = plt.subplots(figsize=(13.5, 6.5), dpi=300)
    ax.axis('off')
    ax.set_xlim(0, 13.5)
    ax.set_ylim(0, 6.5)
    
    components = [
        ("1. Capa de Datos", "data/03_Datasets_Procesados/\nprimaria_dataset.csv\n(1,118 registros)", "#E1D5E7", "#9673A6", 0.5),
        ("2. Modelos ML (.pkl)", "Random Forest (RF)\nRed Neuronal (MLP)\nScaler (StandardScaler)", "#DAE8FC", "#6C8EBF", 3.7),
        ("3. Motor Híbrido", "src/predictor.py\n(ML Inference +\nResguardo Normativo)", "#FFF2CC", "#D6B656", 6.9),
        ("4. Interfaz Streamlit", "src/ui/\n(Tab 1: Monitoreo\nTab 2: Ficha Estudiante\nTab 3: Simulador Libre)", "#D5E8D4", "#82B366", 10.1)
    ]
    
    for title, desc, bg_col, border_col, x in components:
        # Outer Card
        box = mpatches.FancyBboxPatch((x, 1.2), 2.8, 4.0, boxstyle="round,pad=0.05", 
                                      ec=border_col, fc=bg_col, lw=1.8)
        ax.add_patch(box)
        
        # Header Banner
        banner = mpatches.FancyBboxPatch((x, 4.3), 2.8, 0.9, boxstyle="round,pad=0.01", 
                                         ec=border_col, fc=border_col, lw=1)
        ax.add_patch(banner)
        
        ax.text(x + 1.4, 4.75, title, color='white', weight='bold', fontsize=11, ha='center', va='center')
        ax.text(x + 1.4, 2.7, desc, color='#1A1A1A', fontsize=9.5, ha='center', va='center', multialignment='center', linespacing=1.4)
        
    # Draw.io Orthogonal Connectors with Labels
    arrow_labels = ["Dataset Base", "Model Ingest", "Prediction API"]
    for i, x_arrow in enumerate([3.4, 6.6, 9.8]):
        ax.annotate('', xy=(x_arrow + 0.25, 3.2), xytext=(x_arrow - 0.05, 3.2),
                    arrowprops=dict(arrowstyle="-|>", color="#4D4D4D", lw=2.2, mutation_scale=15))
        
    plt.tight_layout()
    plt.savefig(os.path.join(FIG_DIR, "fig_3_2_arquitectura_software.png"), dpi=300, bbox_inches='tight')
    plt.close()
    print("Generated fig_3_2_arquitectura_software.png (Draw.io Vector Style)")

# ==============================================================================
# FIGURA 3.3: FLUJO DE LA CAPA DE RESGUARDO (ESTILO DRAW.IO FLOWCHART REAL)
# ==============================================================================
def gen_fig_3_3():
    fig, ax = plt.subplots(figsize=(13, 9.5), dpi=300)
    ax.axis('off')
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 10)
    
    # 1. Start Event (Rounded Pill)
    box_start = mpatches.FancyBboxPatch((4.2, 8.4), 4.6, 1.0, boxstyle="round,pad=0.2", ec="#9673A6", fc="#E1D5E7", lw=1.8)
    ax.add_patch(box_start)
    ax.text(6.5, 8.9, "Inicio: Evaluación del Estudiante\n(Promedio General & N° Reprobadas)", ha='center', va='center', weight='bold', color='#1A1A1A', fontsize=10)
    
    # 2. Process 1 (Rounded Box)
    box_ml = mpatches.FancyBboxPatch((4.2, 6.8), 4.6, 1.0, boxstyle="round,pad=0.04", ec="#6C8EBF", fc="#DAE8FC", lw=1.8)
    ax.add_patch(box_ml)
    ax.text(6.5, 7.3, "Inferencia de Modelo Machine Learning\n(Calcula Probabilidad Base P_ML)", ha='center', va='center', weight='bold', color='#1A1A1A', fontsize=10)
    
    ax.annotate('', xy=(6.5, 7.8), xytext=(6.5, 8.4), arrowprops=dict(arrowstyle="-|>", color="#4D4D4D", lw=2, mutation_scale=15))
    
    # 3. Decision 1 (True Draw.io Diamond Shape)
    diamond1_x = [6.5, 9.2, 6.5, 3.8]
    diamond1_y = [6.2, 5.0, 3.8, 5.0]
    ax.fill(diamond1_x, diamond1_y, color="#FFF2CC", ec="#D6B656", lw=2)
    ax.text(6.5, 5.0, "¿Promedio < 51.0  Ó\nN° Reprobadas ≥ 2?", ha='center', va='center', weight='bold', color='#1A1A1A', fontsize=10)
    
    ax.annotate('', xy=(6.5, 6.2), xytext=(6.5, 6.8), arrowprops=dict(arrowstyle="-|>", color="#4D4D4D", lw=2, mutation_scale=15))
    
    # YES Branch 1 (Left) -> ALTO RIESGO
    ax.annotate('', xy=(1.9, 3.2), xytext=(3.8, 5.0), arrowprops=dict(arrowstyle="-|>", color="#B85450", lw=2, mutation_scale=15))
    
    # Pill label for YES
    lbl_yes1 = mpatches.FancyBboxPatch((2.4, 4.2), 0.6, 0.35, boxstyle="round,pad=0.01", ec="#B85450", fc="#F8CECC")
    ax.add_patch(lbl_yes1)
    ax.text(2.7, 4.37, "SÍ", color='#B85450', weight='bold', fontsize=9.5, ha='center', va='center')
    
    box_alto = mpatches.FancyBboxPatch((0.4, 1.6), 3.0, 1.6, boxstyle="round,pad=0.04", ec="#B85450", fc="#F8CECC", lw=2)
    ax.add_patch(box_alto)
    ax.text(1.9, 2.4, "ALTO RIESGO\n\nP_final = max(P_ML, 0.85)\nIntervención Prioritaria", ha='center', va='center', weight='bold', color='#660000', fontsize=10, linespacing=1.3)

    # NO Branch 1 (Down) -> Decision 2
    ax.annotate('', xy=(6.5, 3.6), xytext=(6.5, 3.8), arrowprops=dict(arrowstyle="-|>", color="#4D4D4D", lw=2, mutation_scale=15))
    lbl_no1 = mpatches.FancyBboxPatch((6.7, 3.4), 0.6, 0.35, boxstyle="round,pad=0.01", ec="#6C8EBF", fc="#DAE8FC")
    ax.add_patch(lbl_no1)
    ax.text(7.0, 3.57, "NO", color='#2B547E', weight='bold', fontsize=9.5, ha='center', va='center')
    
    # 4. Decision 2 (True Draw.io Diamond Shape)
    diamond2_x = [6.5, 9.2, 6.5, 3.8]
    diamond2_y = [3.6, 2.4, 1.2, 2.4]
    ax.fill(diamond2_x, diamond2_y, color="#FFF2CC", ec="#D6B656", lw=2)
    ax.text(6.5, 2.4, "¿Reprobadas == 1  Ó\n51.0 ≤ Promedio < 60.0?", ha='center', va='center', weight='bold', color='#1A1A1A', fontsize=9.5)
    
    # Branch 2 YES (Left) -> MEDIO RIESGO
    ax.annotate('', xy=(5.2, 0.8), xytext=(5.2, 1.7), arrowprops=dict(arrowstyle="-|>", color="#D6B656", lw=2, mutation_scale=15))
    lbl_yes2 = mpatches.FancyBboxPatch((5.4, 1.3), 0.6, 0.35, boxstyle="round,pad=0.01", ec="#D6B656", fc="#FFF2CC")
    ax.add_patch(lbl_yes2)
    ax.text(5.7, 1.47, "SÍ", color='#B45309', weight='bold', fontsize=9.5, ha='center', va='center')
    
    box_medio = mpatches.FancyBboxPatch((3.7, -0.8), 3.0, 1.5, boxstyle="round,pad=0.04", ec="#D6B656", fc="#FFF2CC", lw=2)
    ax.add_patch(box_medio)
    ax.text(5.2, -0.05, "MEDIO RIESGO\n\nP_final = max(P_ML, 0.50)\nSeguimiento Bimensual", ha='center', va='center', weight='bold', color='#B45309', fontsize=9.5, linespacing=1.3)

    # Branch 2 NO (Right) -> BAJO RIESGO
    ax.annotate('', xy=(9.4, 0.8), xytext=(7.8, 1.7), arrowprops=dict(arrowstyle="-|>", color="#82B366", lw=2, mutation_scale=15))
    lbl_no2 = mpatches.FancyBboxPatch((8.3, 1.3), 0.6, 0.35, boxstyle="round,pad=0.01", ec="#82B366", fc="#D5E8D4")
    ax.add_patch(lbl_no2)
    ax.text(8.6, 1.47, "NO", color='#274E13', weight='bold', fontsize=9.5, ha='center', va='center')
    
    box_bajo = mpatches.FancyBboxPatch((8.0, -0.8), 3.0, 1.5, boxstyle="round,pad=0.04", ec="#82B366", fc="#D5E8D4", lw=2)
    ax.add_patch(box_bajo)
    ax.text(9.5, -0.05, "BAJO RIESGO\n\nP_final = P_ML\nAcompañamiento Estándar", ha='center', va='center', weight='bold', color='#274E13', fontsize=9.5, linespacing=1.3)

    plt.tight_layout()
    plt.savefig(os.path.join(FIG_DIR, "fig_3_3_capa_hibrida_resguardo.png"), dpi=300, bbox_inches='tight')
    plt.close()
    print("Generated fig_3_3_capa_hibrida_resguardo.png (Draw.io Flowchart Vector Style)")




# ==============================================================================
# FIGURA 4.1: TASA DE REPROBACIÓN POR MATERIA
# ==============================================================================
def gen_fig_4_1():
    rates = (dataset[materias] < 51).mean().sort_values(ascending=True) * 100
    labels = [nombres_materias[m] for m in rates.index]
    
    fig, ax = plt.subplots(figsize=(9, 5), dpi=300)
    colors = ['#EF4444' if r > 1.5 else '#F59E0B' if r > 0.8 else '#3B82F6' for r in rates.values]
    bars = ax.barh(labels, rates.values, color=colors, height=0.6, edgecolor='none')
    
    for bar in bars:
        w = bar.get_width()
        ax.text(w + 0.05, bar.get_y() + bar.get_height()/2, f"{w:.2f}%", va='center', fontsize=10, weight='bold', color='#1E293B')
        
    ax.set_xlim(0, 2.5)
    ax.set_xlabel("Tasa Porcentual de Reprobación (%)", fontsize=11, weight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(FIG_DIR, "fig_4_1_tasa_reprobacion_materia.png"), dpi=300, bbox_inches='tight')
    plt.close()
    print("Generated fig_4_1_tasa_reprobacion_materia.png (Clean title)")

# ==============================================================================
# FIGURA 4.2: BOXPLOT MATERIAS REPROBADAS SEGÚN REZAGO
# ==============================================================================
def gen_fig_4_2():
    fig, ax = plt.subplots(figsize=(7, 4.5), dpi=300)
    sns.boxplot(x='rezago', y='num_materias_reprobadas', data=dataset, ax=ax, palette=['#10B981', '#EF4444'], width=0.4)
    
    ax.set_xticks([0, 1])
    ax.set_xticklabels(['Sin Rezago (0)', 'Con Rezago (1)'], fontsize=11, weight='bold')
    ax.set_xlabel("Condición de Rezago Académico", fontsize=11, weight='bold')
    ax.set_ylabel("Número de Materias Reprobadas (Nota < 51)", fontsize=11, weight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(FIG_DIR, "fig_4_2_boxplot_materias_reprobadas.png"), dpi=300, bbox_inches='tight')
    plt.close()
    print("Generated fig_4_2_boxplot_materias_reprobadas.png (Clean title)")

# ==============================================================================
# FIGURA 4.3: EVOLUCIÓN TEMPORAL POR GESTIÓN
# ==============================================================================
def gen_fig_4_3():
    evol = dataset.groupby("gestion")["rezago"].mean() * 100
    
    fig, ax = plt.subplots(figsize=(8, 4), dpi=300)
    bars = ax.bar(evol.index.astype(str), evol.values, color='#2563EB', width=0.45, edgecolor='none')
    
    for bar in bars:
        h = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, h + 0.1, f"{h:.2f}%", ha='center', fontsize=10, weight='bold', color='#1E293B')
        
    ax.set_ylim(0, 3.5)
    ax.set_xlabel("Gestión Académica", fontsize=11, weight='bold')
    ax.set_ylabel("Proporción de Rezago (%)", fontsize=11, weight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(FIG_DIR, "fig_4_3_evolucion_rezago_gestion.png"), dpi=300, bbox_inches='tight')
    plt.close()
    print("Generated fig_4_3_evolucion_rezago_gestion.png (Clean title)")

# ==============================================================================
# FIGURA 4.4: REZAGO PROMEDIO POR CURSO
# ==============================================================================
def gen_fig_4_4():
    orden_grados = ["PRIMERO", "SEGUNDO", "TERCERO", "CUARTO", "QUINTO", "SEXTO"]
    by_curso = (dataset.groupby("anio_escolaridad")["rezago"].mean() * 100).reindex(orden_grados)
    
    fig, ax = plt.subplots(figsize=(8.5, 4), dpi=300)
    ax.plot(by_curso.index, by_curso.values, marker='o', linewidth=2.5, markersize=8, color='#8B5CF6', markerfacecolor='#6D28D9')
    
    for i, val in enumerate(by_curso.values):
        ax.text(i, val + 0.2, f"{val:.2f}%", ha='center', fontsize=10, weight='bold', color='#1E293B')
        
    ax.set_ylim(0, 4.0)
    ax.set_xlabel("Curso de Escolaridad Primaria", fontsize=11, weight='bold')
    ax.set_ylabel("Tasa Promedio de Rezago (%)", fontsize=11, weight='bold')
    plt.tight_layout()
    plt.savefig(os.path.join(FIG_DIR, "fig_4_4_rezago_promedio_curso.png"), dpi=300, bbox_inches='tight')
    plt.close()
    print("Generated fig_4_4_rezago_promedio_curso.png (Clean title)")

# ==============================================================================
# FIGURA 4.5: TRAYECTORIA LONGITUDINAL ESTUDIANTE
# ==============================================================================
def gen_fig_4_5():
    rudes = dataset["rude"].value_counts()
    sample_rude = rudes[rudes >= 3].index[0]
    sample_student = dataset[dataset["rude"] == sample_rude].sort_values("gestion")
    
    fig, ax = plt.subplots(figsize=(8, 4), dpi=300)
    ax.plot(sample_student["gestion"].astype(str), sample_student["promedio_general"], marker='s', linewidth=2.5, markersize=8, color='#059669', markerfacecolor='#047857')
    ax.axhline(51.0, color='#EF4444', linestyle='--', linewidth=1.5, label='Límite Mínimo de Aprobación (51 pts)')
    
    for idx, row in sample_student.iterrows():
        ax.text(str(row["gestion"]), row["promedio_general"] + 1.2, f"{row['promedio_general']:.1f}", ha='center', fontsize=10, weight='bold')
        
    ax.set_ylim(40, 100)
    ax.set_xlabel("Gestión Académica", fontsize=11, weight='bold')
    ax.set_ylabel("Promedio General (0 - 100 pts)", fontsize=11, weight='bold')
    ax.legend(loc='lower right', frameon=True)
    plt.tight_layout()
    plt.savefig(os.path.join(FIG_DIR, "fig_4_5_trayectoria_estudiante_ejemplo.png"), dpi=300, bbox_inches='tight')
    plt.close()
    print("Generated fig_4_5_trayectoria_estudiante_ejemplo.png (Clean title)")

# ==============================================================================
# FIGURA 4.6: MATRICES DE CONFUSIÓN COMPARATIVAS
# ==============================================================================
def gen_fig_4_6():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 3.8), dpi=300)
    
    cm_rf = np.array([[49, 1], [1, 0]])
    cm_mlp = np.array([[50, 0], [1, 0]])
    
    sns.heatmap(cm_rf, annot=True, fmt='d', cmap='Blues', cbar=False, ax=ax1,
                xticklabels=['Pred No Rezago', 'Pred Rezago'], yticklabels=['No Rezago', 'Rezago'])
    ax1.set_title("Random Forest (class_weight='balanced')", fontsize=11, weight='bold')
    
    sns.heatmap(cm_mlp, annot=True, fmt='d', cmap='Greens', cbar=False, ax=ax2,
                xticklabels=['Pred No Rezago', 'Pred Rezago'], yticklabels=['No Rezago', 'Rezago'])
    ax2.set_title("Red Neuronal MLP (StandardScaler)", fontsize=11, weight='bold')
    
    plt.tight_layout()
    plt.savefig(os.path.join(FIG_DIR, "fig_4_6_matriz_confusion_modelos.png"), dpi=300, bbox_inches='tight')
    plt.close()
    print("Generated fig_4_6_matriz_confusion_modelos.png (Clean title)")

# ==============================================================================
# FIGURA 4.7: DISTRIBUCIÓN DE NIVELES DE RIESGO
# ==============================================================================
def gen_fig_4_7():
    categories = ['Bajo Riesgo', 'Medio Riesgo', 'Alto Riesgo']
    counts = [1095, 16, 7]
    percentages = [97.94, 1.43, 0.63]
    colors = ['#10B981', '#F59E0B', '#EF4444']
    
    fig, ax = plt.subplots(figsize=(8, 4.5), dpi=300)
    bars = ax.bar(categories, counts, color=colors, width=0.45, edgecolor='none')
    
    for bar, count, pct in zip(bars, counts, percentages):
        h = bar.get_height()
        # Colocar etiquetas sobre las barras con texto contrastante en gris oscuro
        ax.text(bar.get_x() + bar.get_width()/2, h + 20, f"N = {count:,}\n({pct:.2f}%)", 
                ha='center', va='bottom', fontsize=10, weight='bold', color='#0F172A')
        
    ax.set_ylim(0, 1300)
    ax.set_ylabel("Número de Estudiantes (N)", fontsize=11, weight='bold')
    ax.set_xlabel("Nivel de Riesgo Pedagógico Categorizado", fontsize=11, weight='bold')
    ax.grid(axis='y', linestyle='--', alpha=0.5)
    
    plt.tight_layout()
    plt.savefig(os.path.join(FIG_DIR, "fig_4_7_distribucion_riesgo_estudiantes.png"), dpi=300, bbox_inches='tight')
    plt.close()
    print("Generated fig_4_7_distribucion_riesgo_estudiantes.png (High Contrast Bar Chart)")



if __name__ == "__main__":
    gen_fig_3_1()
    gen_fig_3_2()
    gen_fig_3_3()
    gen_fig_4_1()
    gen_fig_4_2()
    gen_fig_4_3()
    gen_fig_4_4()
    gen_fig_4_5()
    gen_fig_4_6()
    gen_fig_4_7()
    print("All statistical and diagrammatic figures re-generated without figure titles inside image!")
