from __future__ import unicode_literals
import youtube_dl as y


###################################################
#          DESCARGA EL VIDEO DEL YOUTUBE          #
###################################################

VIDEO_URL=input("Agrega una dirección de YouTube: ")

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }]
}
try:
    with y.YoutubeDL(ydl_opts) as v:
        v.download([VIDEO_URL])
except:
    pass