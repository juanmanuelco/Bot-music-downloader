import os
from concurrent.futures import ThreadPoolExecutor
import subprocess
import json

def descargar_video(music):
    # Obtener el artista y el nombre de la música
    artist = music['Artist']
    name = music['Name']
    video_url = music['link']

    # Formato de salida
    output_template = f"{artist} - {name}.mp3"

    subprocess.run([
        "yt-dlp2025.exe", video_url,
        "-f", "bestaudio",
        "--extract-audio",
        "--audio-format", "mp3",
        "--output", output_template,
        "--no-playlist"
    ])

if __name__ == "__main__":
    with open('links.json', 'r', encoding='utf-8') as file:
        music_list = json.load(file)

    # Número de descargas a ejecutar simultáneamente
    num_descargas_simultaneas = 100

    # Utilizar ThreadPoolExecutor para ejecutar en paralelo
    with ThreadPoolExecutor(max_workers=num_descargas_simultaneas) as executor:
        # Lanzar las funciones en paralelo
        executor.map(descargar_video, music_list)