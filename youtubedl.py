import youtube_dl
import os

output_dir = os.path.join('./', '%(playlist_title)s', '%(playlist_index + 53)s. %(title)s.%(ext)s')

download_list = [
    'https://youtube.com/playlist?list=PLz8IdUylt_d6pWwp4ix3zKZuLZ-hK9czf'
]

ydl_opt = {
    'outtmpl': output_dir,
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }, {'key': 'FFmpegMetadata'},],
}

with youtube_dl.YoutubeDL(ydl_opt) as ydl:
    ydl.download(download_list)