from DownloadYoutube import Download
import sys


def __init__(self):
    pass


if __name__ == "__main__":
    print('Seja bem vindo viajante do tempo !')
    print('Digite as seguintes argumentos:')
    print('tipoDownload url path')
    idx = 1
    if len(sys.argv) > 1:
        for p in sys.argv:
            if idx == 2:
                tipo = p
            elif idx == 3:
                url = p
            elif idx == 4:
                path = p
            idx = idx + 1
    else:
        tipo = input('Tipo de Download (video ou playlist): ')
        url = input('informe a url: ')
        path = input('informe a caminho: ')

    if tipo == "video":
        result = Download.downloadfile(url, path)
        print(result)
    elif tipo == "playlist":
        result = Download.downloadplaylist(url, path)
        print(result)
    else:
        print("Informe um dos tipos video ou playlist")
