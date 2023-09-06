from pytube import YouTube

def Downloader(): 
    l = input("Enter Video Link: ")
    url =YouTube(l)
    video = url.streams.first()
    video.download()
    print(video.default_filename + " ["+ str(video.filesize_mb) +" mb] downloaded.")

Downloader()