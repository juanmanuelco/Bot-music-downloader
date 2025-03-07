#import os

#with open('links.txt', 'r', encoding='utf-8') as file:
#    music_list = file.readlines()
#music_list = list(set(music_list))

#for indice,  music in enumerate(music_list):
#    os.system("yt-dlp.exe '" + music + "' -f " + 'best[height<1025]'+ "  --no-playlist  -r 30M --buffer-size 16k --windows-filenames  --write-thumbnail  --write-subs
#    --extract-audio --audio-format mp3 --keep-video -S res,ext:mp4:m4a")


import os
from concurrent.futures import ThreadPoolExecutor
import subprocess

def descargar_video(music):
    
    #os.system(
    #    "yt-dlp.exe " + music + " -f " + 'best[height<1025]+bestvideo[ext=mp4]+bestaudio/best[ext=mp4]/best' +
    #    " --no-playlist -r 30M --buffer-size 16k --windows-filenames --write-thumbnail --write-subs --extract-audio --audio-format mp3 --keep-video -S res,ext:mp4:m4a"
    #)

    output_template = "%(title)s [%(id)s].%(ext)s"

    output_filename = subprocess.check_output([
        "yt-dlp2025.exe", "--get-filename", "-o", output_template, music
    ]).decode("utf-8").strip()

    print("Trying to download: " +output_filename)

    if not os.path.exists(output_filename):
        print("Downloading: " + output_filename)
        os.system(
            "yt-dlp2025.exe " + music + " -f " + 'best[height<1025]+bestvideo[ext=mp4]+bestaudio/best[ext=mp4]/best' +
            " --no-playlist -r 30M --buffer-size 16k --extract-audio --audio-format mp3 --keep-video -S res,ext:mp4:m4a"
        )
    else:
        print("File already exists: " + output_filename)


if __name__ == "__main__":
    with open('links.txt', 'r', encoding='utf-8') as file:
        music_list = file.readlines()
    music_list = list(set(music_list))

    # Número de descargas a ejecutar simultáneamente
    num_descargas_simultaneas = 100

    # Utilizar ThreadPoolExecutor para ejecutar en paralelo
    with ThreadPoolExecutor(max_workers=num_descargas_simultaneas) as executor:
        # Lanzar las funciones en paralelo
        executor.map(descargar_video, music_list)






# -f "best[height=720]" --no-playlist -r 10M --buffer-size 16k --windows-filenames  --write-thumbnail  --write-subs  --extract-audio --audio-format mp3 --keep-video -S res,ext:mp4:m4a



#yt-dlp.exe "https://www.youtube.com/watch?v=LHaOt4mdecI&pp=ygUZWm9kaWFjbyBNb2RlcmF0dG8gb2ZpY2lhbA%3D%3D" -f "best[height<1025]" --no-playlist  -r 30M --buffer-size 16k
# --windows-filenames  --write-thumbnail  --write-subs  --extract-audio --audio-format mp3 --keep-video -S res,ext:mp4:m4a