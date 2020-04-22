from pytube import YouTube, Playlist
from pathlib import Path


class Download:

    def __init__(self):
        pass


    @staticmethod
    def downloadfile(url: str, path: str) -> str:
        """
        performs the video download and returns the file path
        :param url:
        :param path:
        :return path :
        """
        try:
            if Path(path).exists():
                yt = YouTube(url)
                video = yt.streams.first()
                print('Title: ' + video.title)
                path = video.download(path)
                print(path)
                return 'Download complete'
            else:
                return 'Error: Path not exists'
        except ValueError:
            return 'Error: check the url unknown'

    @staticmethod
    def downloadplaylist(urlplaylist: str, path: str) -> str:
        """
        download videos from a playlist
        :param urlplaylist:
        :param path:
        :return:
        """
        playlist = Playlist(urlplaylist)
        if len(playlist) > 0:
            if Path(path).exists():
                try:
                    for url in playlist:
                        yt = YouTube(url)
                        video = yt.streams.first()
                        print('Title: ' + video.title)
                        localpath = video.download(path)
                        print(localpath)
                    return path
                except:
                    return 'Error: check the url unknown'
            else:
                return 'Error: Path not exists'
        else:
            return 'Error: no video was listed in the playlist'
