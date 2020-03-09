# Bee_DownloadYoutube
download videos from youtube with just one command line
### why and for what
Just a utility to make life easier for DEV's who need to download videos, and don't want to install programs on their machines or use the dubious and advertising-laden websites that offer the service.

With bee you will only need to run a single command line to download your favorite videos, or even download the entire playlist for that python course.
### Getting Started
There are two ways to run the program:
 * Running just a Python3 command line type (types can be video or playlist) url path.
```
python3 Youtube.py video https://www.youtube.com/watch?v=fYR9L2ZmodM c:\temp
```
* Or if you prefer we create a simple menu where it will ask for each parameter. just type and download the file.
### Requirements
We use pytube to download the videos.
```
pip install pytube
```
```
pip install path
```

The solution is very simple, we only need two classes, the first is DownloadYoutube.py and it is the magic that happens.

We implemented two methods

DownloadFile responsible for downloading the video from the past url
```
def DownloadFile(url,path):
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
 ```
 The second method is responsible for downloading all videos from a playlist
 
 ```
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
  ```
  
 baixa ai e melhora o código !!!
