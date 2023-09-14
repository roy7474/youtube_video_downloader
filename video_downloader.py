from pytube import YouTube
from sys import argv

link = argv(https://www.youtube.com/watch?v=vEQ8CXFWLZU&t=5s)
yt = YouTube(link)

print("Tittle: ", yt.title)

print('View: ', yt.views)