import os
import yt_dlp


archivo = 'videos.txt'
carpeta_destino = 'mp3'
opciones = {
    'format': 'bestaudio',
    'outtmpl': os.path.join(carpeta_destino, '%(title)s.mp3')
}


with open(archivo, 'r') as f:
    lista = [url for url in f.read().splitlines() if url]

yt_dlp.YoutubeDL(opciones).download(lista)

