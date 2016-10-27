import sys
from urllib import request
from podData import PodData
from podfile import PodFile
from slugify import slugify
import re

class Downloader:
    PodData = None
    DownloadedFile = None
    
    def __init__(self, PodData):
        self.PodData = PodData

    def download(self, path):
        safeFileName = slugify(self.PodData.Header)
        self.DownloadedFile = request.urlretrieve(self.PodData.DownloadUrl, path + "\\" + safeFileName + ".mp3")