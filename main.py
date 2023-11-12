from pytube import YouTube

print("Bonjour !")
url = input("Tapez l'URL d'une vidéo Youtube: ")

def on_download_progress(stream, chunk, bytes_remaining):
    bytes_downloaded = stream.filesize - bytes_remaining
    percent = bytes_downloaded * 100 / stream.filesize
    print(f"Progression du téléchargement: {int(percent)}%")
youtube_video = YouTube(url)
youtube_video.register_on_progress_callback(on_download_progress)
stream = youtube_video.streams.get_highest_resolution()
print("Dévut du téléchargement...")
stream.download()
print(f"Le téléchargement de '{youtube_video.title}' est terminée")
