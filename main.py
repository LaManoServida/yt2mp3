import os
import yt_dlp


archivo = 'videos.txt'
carpeta_destino = 'mp3'
opciones = {
    'format': 'bestaudio',
    'outtmpl': os.path.join(carpeta_destino, '%(title)s.mp3'),
    'ignoreerrors': True,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': 192
    }]
}

youtube_dl = yt_dlp.YoutubeDL(opciones)

with open(archivo, 'r') as f:
    for url in f:
        if url.strip():
            youtube_dl.download([url.strip()])

