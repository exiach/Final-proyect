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
    fig, ax = plt.subplots(figsize=(10, 5.5), dpi=300)
    ax.axis('off')
    
    phases = [
        ("1. Comprensión del Negocio", "Definición de rezago (nota < 51)\ny entorno U.E. Santiváñez", "#1E3A8A"),
        ("2. Comprensión de Datos", "Consolidación de 36 boletines PDF\ny 1,118 registros de primaria", "#2563EB"),
        ("3. Preparación de Datos", "Limpieza de nulos, feature shift\n(prev/next) e imputación", "#3B82F6"),
        ("4. Modelado Predictivo", "Entrenamiento Decision Tree, RF\n(class_weight='balanced') y MLP", "#0284C7"),
        ("5. Evaluación & Segregación", "Partición estratificada, matrices\ny umbrales Alto/Medio/Bajo", "#0D9488"),
        ("6. Despliegue de Prototipo", "Aplicación web Streamlit con\nCapa Híbrida de Resguardo", "#059669")
    ]
    
    for i, (title, desc, color) in enumerate(phases):
        row = i // 2
        col = i % 2
        x = 0.05 + col * 0.48
        y = 0.70 - row * 0.30
        
        rect = mpatches.FancyBboxPatch((x, y), 0.42, 0.22, boxstyle="round,pad=0.03", 
                                       ec=color, fc=color, alpha=0.1, lw=2)
        ax.add_patch(rect)
        
        title_box = mpatches.FancyBboxPatch((x, y + 0.15), 0.42, 0.07, boxstyle="round,pad=0.01", 
                                            ec=color, fc=color, lw=1)
        ax.add_patch(title_box)
        
        ax.text(x + 0.21, y + 0.185, title, color='white', weight='bold', fontsize=11, ha='center', va='center')
        ax.text(x + 0.21, y + 0.07, desc, color='#1F2937', fontsize=9.5, ha='center', va='center')
        
    plt.tight_layout()
    plt.savefig(os.path.join(FIG_DIR, "fig_3_1_flujograma_crisp_dm.png"), dpi=300, bbox_inches='tight')
    plt.close()
    print("Generated fig_3_1_flujograma_crisp_dm.png (Clean title)")

# ==============================================================================
# FIGURA 3.2: ARQUITECTURA DE SOFTWARE DEL PROTOTIPO
# ==============================================================================
def gen_fig_3_2():
    fig, ax = plt.subplots(figsize=(11, 5.5), dpi=300)
    ax.axis('off')
    
    components = [
        ("Capa de Datos", "data/03_Datasets_Procesados/\nprimaria_dataset.csv", "#64748B", 0.05, 0.4),
        ("Capa de Modelos ML", "modelos_entrenados/\n(Random Forest & MLP .pkl)", "#0EA5E9", 0.28, 0.4),
        ("Motor Predictivo Híbrido", "src/predictor.py\n(ML + Resguardo Pedagógico)", "#8B5CF6", 0.51, 0.4),
        ("Interfaz Streamlit", "src/ui/ (Monitoreo, Ficha\ny Simulador Libre)", "#10B981", 0.74, 0.4)
    ]
    
    for title, desc, color, x, y in components:
        rect = mpatches.FancyBboxPatch((x, y), 0.20, 0.35, boxstyle="round,pad=0.03", ec=color, fc=color, alpha=0.12, lw=2)
        ax.add_patch(rect)
        
        header = mpatches.FancyBboxPatch((x, y + 0.25), 0.20, 0.10, boxstyle="round,pad=0.01", ec=color, fc=color, lw=1)
        ax.add_patch(header)
        
        ax.text(x + 0.10, y + 0.30, title, color='white', weight='bold', fontsize=10, ha='center', va='center')
        ax.text(x + 0.10, y + 0.12, desc, color='#0F172A', fontsize=9, ha='center', va='center')
        
    for x_arrow in [0.255, 0.485, 0.715]:
        ax.annotate('', xy=(x_arrow + 0.02, 0.57), xytext=(x_arrow - 0.005, 0.57),
                    arrowprops=dict(arrowstyle="->", color="#334155", lw=2.5))
        
    plt.tight_layout()
    plt.savefig(os.path.join(FIG_DIR, "fig_3_2_arquitectura_software.png"), dpi=300, bbox_inches='tight')
    plt.close()
    print("Generated fig_3_2_arquitectura_software.png (Clean title)")

# ==============================================================================
# FIGURA 3.3: FLUJO DE LA CAPA DE RESGUARDO PEDAGÓGICO
# ==============================================================================
def gen_fig_3_3():
    fig, ax = plt.subplots(figsize=(10, 6), dpi=300)
    ax.axis('off')
    
    boxes = [
        ("Entrada Estudiante", "Promedio General & N° Materias Reprobadas", 0.35, 0.80, "#3B82F6"),
        ("Inferencia Modelo ML", "Calcula Probabilidad Base P_ML (RF / MLP)", 0.35, 0.62, "#8B5CF6"),
        ("Evaluación de Reglas de Resguardo", "¿Promedio < 51 ó Reprobadas >= 2?", 0.35, 0.42, "#F59E0B"),
        ("SI: Ajuste Normativo", "P_final = max(P_ML, 0.85) -> ALTO RIESGO", 0.05, 0.20, "#EF4444"),
        ("NO: Evaluación Secundaria", "¿Reprobadas == 1 ó 51 <= Prom < 60?", 0.65, 0.42, "#3B82F6"),
        ("SI: Alerta Media", "P_final = max(P_ML, 0.50) -> MEDIO RIESGO", 0.45, 0.20, "#F59E0B"),
        ("NO: Salida Estándar", "P_final = P_ML -> BAJO RIESGO", 0.75, 0.20, "#10B981")
    ]
    
    for title, desc, x, y, color in boxes:
        w, h = (0.30, 0.12)
        rect = mpatches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02", ec=color, fc=color, alpha=0.15, lw=2)
        ax.add_patch(rect)
        hdr = mpatches.FancyBboxPatch((x, y + h - 0.04), w, 0.04, boxstyle="round,pad=0.005", ec=color, fc=color)
        ax.add_patch(hdr)
        ax.text(x + w/2, y + h - 0.02, title, color='white', weight='bold', fontsize=9, ha='center', va='center')
        ax.text(x + w/2, y + (h-0.04)/2, desc, color='#0F172A', fontsize=8.5, ha='center', va='center')

    plt.tight_layout()
    plt.savefig(os.path.join(FIG_DIR, "fig_3_3_capa_hibrida_resguardo.png"), dpi=300, bbox_inches='tight')
    plt.close()
    print("Generated fig_3_3_capa_hibrida_resguardo.png (Clean title)")

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
    labels = ['Bajo Riesgo', 'Medio Riesgo', 'Alto Riesgo']
    sizes = [1095, 16, 7]
    colors = ['#10B981', '#F59E0B', '#EF4444']
    
    fig, ax = plt.subplots(figsize=(6.5, 4.5), dpi=300)
    wedges, texts, autotexts = ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors,
                                      wedgeprops=dict(width=0.4, edgecolor='white', linewidth=2),
                                      textprops=dict(size=10, weight='bold'))
    
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontsize(10)
        
    plt.tight_layout()
    plt.savefig(os.path.join(FIG_DIR, "fig_4_7_distribucion_riesgo_estudiantes.png"), dpi=300, bbox_inches='tight')
    plt.close()
    print("Generated fig_4_7_distribucion_riesgo_estudiantes.png (Clean title)")


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
