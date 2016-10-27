import sys
import os
sys.path.append("./Application")
from PyQt4 import QtGui, QtCore
from functools import partial
from scraper import Scraper
from downloader import Downloader
from podfile import PodFile


class Window(QtGui.QMainWindow):
    __WindowWidth = 500
    __WindowHeight = 500
    __ToolBarHeight = 30
    __ElementPadding = 5
    __StatusBarHeight = 20
    statusmessage = "Hello World"


    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, self.__WindowWidth, self.__WindowHeight)
        self.setWindowTitle("Poddscraper & downloader")
        self.setWindowIcon(QtGui.QIcon("./Content/Bitmaps/Icons/trollface.png"))

        self.exitApplication = QtGui.QAction("&Quit",self)
        self.exitApplication.setShortcut("Ctrl+Q")
        self.exitApplication.setStatusTip("Exit application")
        self.exitApplication.triggered.connect(self.close_application)

        self.statusBar()

        self.mainMenu = self.menuBar()
        self.mainMenu.resize(500, self.__ToolBarHeight)
        self.fileMenu = self.mainMenu.addMenu("&File")
        self.fileMenu.addAction(self.exitApplication)
        
        self.btn = QtGui.QPushButton("Quit",self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move((self.__WindowWidth - self.btn.size().width()), ((self.__WindowHeight - self.__StatusBarHeight) - self.btn.size().height()))
        self.btn.clicked.connect(self.close_application)
        
        self.textbox = QtGui.QLineEdit(self)
        self.textbox.move(20, self.__ToolBarHeight)
        self.textbox.resize(150, 20)
        
        self.comboBox = QtGui.QComboBox(self)
        self.comboBox.addItem("50")
        self.comboBox.addItem("100")
        self.comboBox.addItem("200")
        self.comboBox.addItem("300")
        self.comboBox.addItem("500")
        self.comboBox.addItem("800")
        self.comboBox.addItem("1600")
        self.comboBox.addItem("3200")
        self.comboBox.addItem("6400")
        self.comboBox.addItem("12800")
        self.comboBox.resize(60, 20)
        self.comboBox.move(200, self.__ToolBarHeight)
        
        self.fetchbtn = QtGui.QPushButton("Fetch",self)
        self.fetchbtn.resize(self.fetchbtn.sizeHint())
        self.fetchbtn.move((500 - self.fetchbtn.size().width()), self.__ToolBarHeight)
        self.fetchbtn.clicked.connect(self.FetchPodcastFiles)

        self.statuslabel = QtGui.QLabel(self)
        self.statuslabel.setText(self.statusmessage)
        self.statuslabel.resize(250, 20)
        self.statuslabel.move(20, 150)

        self.show()
        

    def close_application(self):
        sys.exit()

    def FetchPodcastFiles(self):
        path = os.path.normpath(QtGui.QFileDialog.getExistingDirectory())
        myScraper = Scraper("http://{}.libsyn.com/webpage/page/1/size/{}".format(self.textbox.text(), self.comboBox.currentText()))
        myScraper.scrape()
        for pod in myScraper.PodList:
            downloader = Downloader(pod)
            downloader.download(path)
            file = PodFile(downloader.DownloadedFile)
            file.writeTag(pod)






def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()      
    sys.exit(app.exec_())


run()