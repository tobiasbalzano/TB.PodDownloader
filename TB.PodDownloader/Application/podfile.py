from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, TIT2, TPE1, TALB, TDRC, COMM, WXXX, error
from datetime import datetime

class PodFile:
    audiofile = None

    def __init__(self, podFile):
        self.audiofile = MP3(podFile[0], ID3=ID3)
    
    def writeTag(self, podData):
        try:
            self.audiofile.clear()
            self.audiofile.add_tags()
        except:
            pass
        
        self.audiofile.tags.add(TIT2(encoding=3, text=podData.Header))
        self.audiofile.tags.add(TPE1(encoding=3, text=podData.Title))
        self.audiofile.tags.add(TALB(encoding=3, text=podData.Title))
        self.audiofile.tags.add(WXXX(encoding=3, text=podData.DownloadUrl))
        self.audiofile.tags.add(COMM(encoding=3, text=podData.Description))
        self.date = datetime.strptime(podData.DatePosted, "%a, %d %B %Y")
        self.dateinput = u"" + str(self.date.year) + "-" + str(self.date.month) + "-" + str(self.date.day)
        self.audiofile.tags.add(TDRC(encoding=3, text=[self.dateinput]))
        self.audiofile.save(v1=2)
