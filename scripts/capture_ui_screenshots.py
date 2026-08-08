import os
import time
from playwright.sync_api import sync_playwright

FIG_DIR = os.path.abspath("documentacion/figuras")
os.makedirs(FIG_DIR, exist_ok=True)

def capture_streamlit_tabs():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 1440, "height": 900})
        page = context.new_page()
        
        print("Navigating to Streamlit app at http://localhost:8501...")
        page.goto("http://localhost:8501", wait_until="networkidle")
        time.sleep(3) # Ensure Streamlit finishes rendering
        
        # 1. Capture Tab 1: Monitoreo de Curso
        page.screenshot(path=os.path.join(FIG_DIR, "fig_4_8_prototipo_monitoreo_curso.png"), full_page=False)
        print("Captured fig_4_8_prototipo_monitoreo_curso.png")
        
        # 2. Capture Tab 2: Ficha de Estudiante
        tab2_button = page.get_by_role("tab", name="👤 Ficha de Estudiante & Simulador de Notas")
        if tab2_button.is_visible():
            tab2_button.click()
            time.sleep(2)
            page.screenshot(path=os.path.join(FIG_DIR, "fig_4_9_prototipo_ficha_estudiante.png"), full_page=False)
            print("Captured fig_4_9_prototipo_ficha_estudiante.png")
            
        # 3. Capture Tab 3: Simulador Libre
        tab3_button = page.get_by_role("tab", name="🧪 Simulador Libre")
        if tab3_button.is_visible():
            tab3_button.click()
            time.sleep(2)
            page.screenshot(path=os.path.join(FIG_DIR, "fig_4_10_prototipo_simulador_libre.png"), full_page=False)
            print("Captured fig_4_10_prototipo_simulador_libre.png")
            
        browser.close()
        print("All UI screenshots captured successfully!")

if __name__ == "__main__":
    capture_streamlit_tabs()
