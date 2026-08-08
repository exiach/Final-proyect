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
# FIGURA 3.1: FLUJOGRAMA METODOLÓGICO CRISP-DM ADAPTADO
# ==============================================================================
def gen_fig_3_1():
    fig, ax = plt.subplots(figsize=(12, 7), dpi=300)
    ax.axis('off')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    
    phases = [
        ("Fase 1: Comprensión del Negocio", "Definición del rezago (nota < 51)\ny contexto U.E. Santiváñez", "#1E3A8A", (0.5, 3.8)),
        ("Fase 2: Comprensión de Datos", "Consolidación de 36 boletines PDF\ny 1,118 registros históricos", "#2563EB", (3.6, 3.8)),
        ("Fase 3: Preparación de Datos", "Limpieza de nulos, feature shift\n(prev/next) e imputación", "#3B82F6", (6.7, 3.8)),
        ("Fase 6: Despliegue de Prototipo", "Aplicación web Streamlit con\nCapa Híbrida de Resguardo", "#059669", (0.5, 0.8)),
        ("Fase 5: Evaluación & Segregación", "Partición estratificada, matrices\ny umbrales Alto/Medio/Bajo", "#0D9488", (3.6, 0.8)),
        ("Fase 4: Modelado Predictivo", "Entrenamiento Decision Tree, RF\n(class_weight='balanced') y MLP", "#0284C7", (6.7, 0.8))
    ]
    
    for title, desc, color, (x, y) in phases:
        # Container Box
        box = mpatches.FancyBboxPatch((x, y), 2.8, 1.6, boxstyle="round,pad=0.04", 
                                      ec=color, fc='#F8FAFC', lw=2)
        ax.add_patch(box)
        
        # Header Banner
        banner = mpatches.FancyBboxPatch((x, y + 1.15), 2.8, 0.45, boxstyle="round,pad=0.01", 
                                         ec=color, fc=color, lw=1)
        ax.add_patch(banner)
        
        # Text
        ax.text(x + 1.4, y + 1.37, title, color='white', weight='bold', fontsize=10, ha='center', va='center')
        ax.text(x + 1.4, y + 0.60, desc, color='#0F172A', fontsize=9.5, ha='center', va='center', multialignment='center')

    # Connecting Arrows for CRISP-DM Cycle
    # Top row left-to-right
    ax.annotate('', xy=(3.5, 4.6), xytext=(3.4, 4.6), arrowprops=dict(arrowstyle="->", color="#475569", lw=2.5))
    ax.annotate('', xy=(6.6, 4.6), xytext=(6.5, 4.6), arrowprops=dict(arrowstyle="->", color="#475569", lw=2.5))
    
    # Right side top-to-bottom
    ax.annotate('', xy=(8.1, 2.5), xytext=(8.1, 3.7), arrowprops=dict(arrowstyle="->", color="#475569", lw=2.5))
    
    # Bottom row right-to-left
    ax.annotate('', xy=(6.5, 1.6), xytext=(6.6, 1.6), arrowprops=dict(arrowstyle="->", color="#475569", lw=2.5))
    ax.annotate('', xy=(3.4, 1.6), xytext=(3.5, 1.6), arrowprops=dict(arrowstyle="->", color="#475569", lw=2.5))
    
    plt.tight_layout()
    plt.savefig(os.path.join(FIG_DIR, "fig_3_1_flujograma_crisp_dm.png"), dpi=300, bbox_inches='tight')
    plt.close()
    print("Generated fig_3_1_flujograma_crisp_dm.png (Redesigned)")

# ==============================================================================
# FIGURA 3.2: ARQUITECTURA DE SOFTWARE DEL PROTOTIPO
# ==============================================================================
def gen_fig_3_2():
    fig, ax = plt.subplots(figsize=(13, 6), dpi=300)
    ax.axis('off')
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 6)
    
    components = [
        ("1. Capa de Datos", "data/03_Datasets_Procesados/\nprimaria_dataset.csv\n(1,118 registros)", "#475569", 0.4),
        ("2. Modelos ML (.pkl)", "Random Forest (RF)\nRed Neuronal (MLP)\nScaler (StandardScaler)", "#0EA5E9", 3.6),
        ("3. Motor Híbrido", "src/predictor.py\n(ML Inference +\nResguardo Normativo)", "#8B5CF6", 6.8),
        ("4. Interfaz Streamlit", "src/ui/\n(Tab 1: Monitoreo\nTab 2: Ficha Estudiante\nTab 3: Simulador Libre)", "#10B981", 10.0)
    ]
    
    for title, desc, color, x in components:
        # Container Box
        box = mpatches.FancyBboxPatch((x, 1.2), 2.6, 3.6, boxstyle="round,pad=0.05", 
                                      ec=color, fc='#F8FAFC', lw=2)
        ax.add_patch(box)
        
        # Header Banner
        banner = mpatches.FancyBboxPatch((x, 4.0), 2.6, 0.8, boxstyle="round,pad=0.01", 
                                         ec=color, fc=color, lw=1)
        ax.add_patch(banner)
        
        # Text inside
        ax.text(x + 1.3, 4.4, title, color='white', weight='bold', fontsize=11, ha='center', va='center')
        ax.text(x + 1.3, 2.6, desc, color='#0F172A', fontsize=10, ha='center', va='center', multialignment='center', linespacing=1.4)
        
    # Flow Arrows between stages
    for x_arrow in [3.1, 6.3, 9.5]:
        ax.annotate('', xy=(x_arrow + 0.45, 3.0), xytext=(x_arrow - 0.05, 3.0),
                    arrowprops=dict(arrowstyle="->", color="#334155", lw=3.0))
        
    plt.tight_layout()
    plt.savefig(os.path.join(FIG_DIR, "fig_3_2_arquitectura_software.png"), dpi=300, bbox_inches='tight')
    plt.close()
    print("Generated fig_3_2_arquitectura_software.png (Redesigned)")

# ==============================================================================
# FIGURA 3.3: FLUJO DE LA CAPA DE RESGUARDO PEDAGÓGICO
# ==============================================================================
def gen_fig_3_3():
    fig, ax = plt.subplots(figsize=(13, 8.5), dpi=300)
    ax.axis('off')
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 9)
    
    # 1. Start Node
    box_start = mpatches.FancyBboxPatch((4.2, 7.3), 4.6, 1.1, boxstyle="round,pad=0.04", ec="#2563EB", fc="#EFF6FF", lw=2)
    ax.add_patch(box_start)
    ax.text(6.5, 7.85, "Entrada del Estudiante\n(Promedio General & N° Materias Reprobadas)", ha='center', va='center', weight='bold', color='#1E3A8A', fontsize=10.5)
    
    # 2. ML Inference Node
    box_ml = mpatches.FancyBboxPatch((4.2, 5.5), 4.6, 1.1, boxstyle="round,pad=0.04", ec="#8B5CF6", fc="#F5F3FF", lw=2)
    ax.add_patch(box_ml)
    ax.text(6.5, 6.05, "Inferencia de Modelo Machine Learning\n(Calcula Probabilidad Base P_ML)", ha='center', va='center', weight='bold', color='#5B21B6', fontsize=10.5)
    
    # Arrow Start -> ML
    ax.annotate('', xy=(6.5, 6.6), xytext=(6.5, 7.3), arrowprops=dict(arrowstyle="->", color="#334155", lw=2.5))
    
    # 3. Decision Node 1
    box_d1 = mpatches.FancyBboxPatch((3.8, 3.6), 5.4, 1.3, boxstyle="round,pad=0.04", ec="#F59E0B", fc="#FFFBEB", lw=2.5)
    ax.add_patch(box_d1)
    ax.text(6.5, 4.25, "¿Promedio < 51.0  Ó  N° Reprobadas ≥ 2?", ha='center', va='center', weight='bold', color='#92400E', fontsize=11)
    
    # Arrow ML -> D1
    ax.annotate('', xy=(6.5, 4.9), xytext=(6.5, 5.5), arrowprops=dict(arrowstyle="->", color="#334155", lw=2.5))
    
    # YES Branch (Left) -> ALTO RIESGO
    ax.annotate('', xy=(2.0, 2.7), xytext=(4.2, 3.6), arrowprops=dict(arrowstyle="->", color="#EF4444", lw=2.5))
    ax.text(2.6, 3.3, "SÍ", color='#DC2626', weight='bold', fontsize=12)
    
    box_alto = mpatches.FancyBboxPatch((0.5, 1.0), 3.0, 1.7, boxstyle="round,pad=0.04", ec="#EF4444", fc="#FEF2F2", lw=2.5)
    ax.add_patch(box_alto)
    ax.text(2.0, 1.85, "🔴 ALTO RIESGO\n\nP_final = max(P_ML, 0.85)\nIntervención Prioritaria", ha='center', va='center', weight='bold', color='#991B1B', fontsize=10.5, linespacing=1.3)

    # NO Branch (Right) -> Decision Node 2
    ax.annotate('', xy=(6.5, 2.7), xytext=(6.5, 3.6), arrowprops=dict(arrowstyle="->", color="#2563EB", lw=2.5))
    ax.text(6.7, 3.15, "NO", color='#2563EB', weight='bold', fontsize=12)
    
    # 4. Decision Node 2
    box_d2 = mpatches.FancyBboxPatch((4.3, 1.0), 4.4, 1.7, boxstyle="round,pad=0.04", ec="#3B82F6", fc="#EFF6FF", lw=2)
    ax.add_patch(box_d2)
    ax.text(6.5, 1.85, "¿Reprobadas == 1  Ó\n51.0 ≤ Promedio < 60.0?", ha='center', va='center', weight='bold', color='#1E40AF', fontsize=10.5)
    
    # Branch 2 YES (Top Right) -> MEDIO RIESGO
    ax.annotate('', xy=(9.4, 2.6), xytext=(8.7, 2.2), arrowprops=dict(arrowstyle="->", color="#F59E0B", lw=2.5))
    ax.text(9.0, 2.6, "SÍ", color='#D97706', weight='bold', fontsize=11)
    
    box_medio = mpatches.FancyBboxPatch((9.4, 2.0), 3.1, 1.5, boxstyle="round,pad=0.04", ec="#F59E0B", fc="#FFFBEB", lw=2.5)
    ax.add_patch(box_medio)
    ax.text(10.95, 2.75, "🟡 MEDIO RIESGO\n\nP_final = max(P_ML, 0.50)\nSeguimiento Bimensual", ha='center', va='center', weight='bold', color='#B45309', fontsize=10, linespacing=1.3)

    # Branch 2 NO (Bottom Right) -> BAJO RIESGO
    ax.annotate('', xy=(9.4, 0.8), xytext=(8.7, 1.3), arrowprops=dict(arrowstyle="->", color="#10B981", lw=2.5))
    ax.text(9.0, 0.9, "NO", color='#059669', weight='bold', fontsize=11)
    
    box_bajo = mpatches.FancyBboxPatch((9.4, 0.1), 3.1, 1.5, boxstyle="round,pad=0.04", ec="#10B981", fc="#ECFDF5", lw=2.5)
    ax.add_patch(box_bajo)
    ax.text(10.95, 0.85, "🟢 BAJO RIESGO\n\nP_final = P_ML\nAcompañamiento Estándar", ha='center', va='center', weight='bold', color='#065F46', fontsize=10, linespacing=1.3)

    plt.tight_layout()
    plt.savefig(os.path.join(FIG_DIR, "fig_3_3_capa_hibrida_resguardo.png"), dpi=300, bbox_inches='tight')
    plt.close()
    print("Generated fig_3_3_capa_hibrida_resguardo.png (Redesigned & Clean)")



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
