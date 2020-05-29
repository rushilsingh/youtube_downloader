
if __name__ == '__main__':
    from sys import argv
    from pytube import YouTube
    yt = YouTube(argv[1])
    stream = yt.streams.first()
    stream.download()

