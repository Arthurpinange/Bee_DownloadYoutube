from pytube import YouTube
from pathlib import Path
class Download:

    def __init__(self):
        pass

    @staticmethod
    def DownloadFile(url, path):
        '''
        performs the video download and returns the file path
        :param url:
        :param path:
        :return path :
        '''
        try:
            if Path(path).exists():
                yt = YouTube(url)
                video = yt.streams.first()
                path = video.download(path)
                return path
            else:
                return "Error: Path not exists"
        except:
            return "Error: check the url unknown"

    @staticmethod
    def DownloadPlayList(urlplaylist, path):
        '''
        download videos from a playlist
        :param urlplaylist:
        :param path:
        :return:
        '''
        playlist = Playlist(urlplaylist)
        if len(playlist) >0:
            if Path(path).exists():
                try:
                    for url in playlist:
                        yt = YouTube(url)
                        video = yt.streams.first()
                        video.download(path)
                    return path
                except:
                    return "Error: check the url unknown"
            else:
                return "Error: Path not exists"
        else:
            return "Error: no video was listed in the playlist"