from pytube import YouTube
from sys import argv

link = "https://www.youtube.com/watch?v=vEQ8CXFWLZU"
yt = YouTube(link)
print ("Tittle:", yt.title)
print ("views: ", yt.views )
