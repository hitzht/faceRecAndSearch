import requests
import os

def DownloadImageByUrl(url, name):
      print(url)
      resp = requests.get(url)
      with open(name, "wb") as f:
            f.write(resp.content)

def DeletePhotoByPath(path):
      os.removedirs(path)