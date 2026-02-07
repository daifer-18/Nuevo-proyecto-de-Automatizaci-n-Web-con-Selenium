# -*- coding: utf-8 -*-
import sys
import io
# Configurar encoding para Windows
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configuración del driver
driver = webdriver.Chrome()

try:
    print("Abriendo dolarito.ar...")
    driver.get("https://www.dolarito.ar/")
    
    # Esperar más tiempo para que cargue todo el JavaScript
    print("Esperando que cargue el contenido...")
    time.sleep(10)
    
    print("\n" + "=" * 70)
    print("           COTIZACIONES DEL DÓLAR - DOLARITO.AR")
    print("=" * 70)
    
    # Obtener todo el texto visible de la página
    body_text = driver.find_element(By.TAG_NAME, "body").text
    lines = [line.strip() for line in body_text.split('\n') if line.strip()]
    
    # Mostrar información de depuración
    print(f"\n[DEBUG] Total de líneas encontradas: {len(lines)}")
    
    # Buscar dólar oficial y blue
    i = 0
    while i < len(lines):
        line = lines[i].lower()
        
        # Buscar dólar oficial
        if 'dolar oficial' in line or 'dólar oficial' in line:
            print(f"\n💵 DÓLAR OFICIAL")
            print(f"   Línea encontrada: '{lines[i]}'")
            # Mostrar las próximas 10 líneas
            for j in range(1, min(10, len(lines) - i)):
                next_line = lines[i + j]
                print(f"   [{j}] {next_line}")
                if '$' in next_line or 'spread' in next_line.lower():
                    pass  # Continuar mostrando
                elif 'dolar' in next_line.lower() or 'dólar' in next_line.lower():
                    break  # Llegamos a otra cotización
        
        # Buscar dólar blue
        if ('dolar blue' in line or 'dólar blue' in line) and 'oficial' not in lines[max(0, i-1)].lower():
            print(f"\n💶 DÓLAR BLUE")
            print(f"   Línea encontrada: '{lines[i]}'")
            # Mostrar las próximas 10 líneas
            for j in range(1, min(10, len(lines) - i)):
                next_line = lines[i + j]
                print(f"   [{j}] {next_line}")
                if '$' in next_line or 'spread' in next_line.lower():
                    pass  # Continuar mostrando
                elif 'dolar' in next_line.lower() or 'dólar' in next_line.lower():
                    break  # Llegamos a otra cotización
            break  # Salir después de mostrar el blue
        
        i += 1
    
    print("\n" + "=" * 70)
    print("\n✅ Script ejecutado correctamente")
    
except Exception as e:
    print(f"\n❌ Error: {e}")
    import traceback
    traceback.print_exc()

finally:
    print("\nCerrando navegador...")
    time.sleep(2)
    driver.quit()
    print("Navegador cerrado.\n")
