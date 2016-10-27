import sys
import re

class PodData:
    __removeRegex = r"\?dest-id=[0-9]*"
    Title = ""
    Header = ""
    Description = ""
    DownloadUrl = ""
    DatePosted = ""

    def __init__(self, title, header, desc, download, date):
        self.Title = title
        self.Header = header
        self.Description = desc
        p = re.compile(self.__removeRegex, re.IGNORECASE)
        self.DownloadUrl = re.sub(p, "", download,)
        self.DatePosted = date
        return super().__init__()