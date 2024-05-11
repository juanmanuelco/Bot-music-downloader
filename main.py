from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import json

from selenium.webdriver.support.wait import WebDriverWait

chrome_driver_path = "C:\chromedriver.exe"
prefs = {"download.default_directory" : "I:\Videos"}

# Leer el archivo musics.txt
with open('musics.txt', 'r', encoding='utf-8') as file:
    music_list = file.readlines()

# Crear una instancia de Chrome
driver = webdriver.Chrome(executable_path=chrome_driver_path)


driver.get('https://www.youtube.com')
time.sleep(10)

# Iterar sobre cada línea en musics.txt
for indice,  music in enumerate(music_list):
    try:
        search_box = driver.find_element('name', 'search_query')
        search_box.clear()
        search_box.send_keys(music + Keys.RETURN)
        time.sleep(5)

        first_result = driver.find_elements(By.CSS_SELECTOR ,'.ytd-section-list-renderer #contents #dismissible a#thumbnail')
        video_url = first_result[0].get_attribute('href')

        # Almacenar el resultado en la lista en formato JSON
        #result_entry = {"name": music.strip(), "link": video_url}
        #results.append(result_entry)
        with open("links.txt", "a") as temp_file:
            temp_file.write("%s\n" % video_url)
    except:
        print("music failed: " + str(indice) + " " +  music)

# Guardar la lista de resultados en formato JSON en el archivo links.json
#with open('links.json', 'w') as json_file:
    #json.dump(results, json_file, indent=2)

driver.quit()
