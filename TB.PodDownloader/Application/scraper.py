import sys
from urllib import request
from bs4 import BeautifulSoup
from podData import PodData

class Scraper(BeautifulSoup):
    soup = ""
    PodList = []


    def __init__(self, url):
        __html = request.urlopen(url)
        self.soup = BeautifulSoup(__html, "html.parser")

    def scrape(self):
        title = self.soup.find("div", class_="podcastTitle").string
        contentNode = self.soup.find("div", class_="content")
        podList = contentNode.find_all("td")
        for item in podList:
            if item.next.next == " ":
                continue
            header = item.find("div", class_="postTitle").find("a", class_="postTitle").string
            url = item.find("div", class_="postTitle").next['href']
            desc = item.find("div", class_="postBody").stripped_strings
            date = item.find("div", class_="postDate").string
            descString = date + "\n"
            for str in desc:
                descString += str + "\n"
            poditem = PodData(title, header, descString, url, date)
            self.PodList.append(poditem)
        
