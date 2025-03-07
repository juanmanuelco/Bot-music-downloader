from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import json

# Especificar la ruta al controlador de Chrome
chrome_driver_path = "C:\\chromedriver.exe"

# Crear un objeto Service
service = Service(chrome_driver_path)

# Crear la instancia de WebDriver usando el Service
driver = webdriver.Chrome(service=service)

# Leer el archivo musics.json
with open('musics.json', 'r', encoding='utf-8') as file:
    music_list = json.load(file)

# Lista para almacenar los resultados
results = []

driver.get('https://www.youtube.com')
time.sleep(5)

# Iterar sobre cada elemento en music_list
for indice, music in enumerate(music_list):
    try:
        search_box = driver.find_element('name', 'search_query')
        search_box.clear()
        search_box.send_keys(music['Name'] + " " + music['Artist'] + Keys.RETURN)
        time.sleep(2)

        first_result = driver.find_elements(By.CSS_SELECTOR, '.ytd-section-list-renderer #contents #dismissible a#thumbnail')
        video_url = first_result[0].get_attribute('href')

        # Almacenar el resultado en la lista en formato JSON
        result_entry = {
            "Artist": music['Artist'],
            "Name": music['Name'],
            "link": video_url
        }
        print(result_entry)
        results.append(result_entry)

    except Exception as e:
        print(f"Music failed: {indice} {music['Name']} - Error: {str(e)}")

# Guardar la lista de resultados en formato JSON en el archivo links.json
with open('links.json', 'w', encoding='utf-8') as json_file:
    json.dump(results, json_file, ensure_ascii=False, indent=2)

driver.quit()