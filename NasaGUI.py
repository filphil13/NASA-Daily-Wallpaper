#%%
from datetime import date
from os import name
import requests
import time
import ctypes
import threading
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap, QFont

#%%
class MainWindow(QMainWindow):
    Run = True
    def __init__(self,app):
        super().__init__()
        self.Run = True
        self.apiinfo = GetAPIInfo()
        self.setWindowTitle('NASA Pic of the Day')
        self.setWindowIcon(QIcon("Resources/Satellite.ico"))
        self.setFixedSize(700,800)

        self.setStyleSheet("background-color: black;")

        self.layout = QVBoxLayout()
        self.explainWidget(self.apiinfo.dailyapi["explanation"])
        self.imageWidget()
        self.titleWidget(self.apiinfo.dailyapi["title"])
        self.centralwidget = QWidget(self)
        self.setCentralWidget(self.centralwidget)
        self.centralwidget.setLayout(self.layout)

        self.trayicon = QSystemTrayIcon(QIcon('Resources\Satellite.ico'),parent=app)
        self.trayicon.setToolTip("NASA Wallpaper")
        
        self.menu = QMenu()
        self.TrayIconQuit()
        self.TrayIconExplain()
        self.trayicon.setContextMenu(self.menu)

        self.trayicon.show()

    def explainWidget(self,explanation):
        self.explainlabel = QLabel(explanation)
        self.explainlabel.setAlignment(Qt.AlignCenter)

        self.explainlabel.setFont(QFont('SansSerif', 8.5)) 
        self.explainlabel.setStyleSheet("""
                                        font-weight: bold;
                                        color: white
                                        """
        )
        self.explainlabel.setWordWrap(True)

        self.layout.addWidget(self.explainlabel)

    def imageWidget(self):
        self.label = QLabel(self)
        self.pixmap = QPixmap('Resources\sample.jpg')
        #self.pixmap.scaled(700,300,Qt.KeepAspectRatio)
        self.label.setPixmap(self.pixmap.scaled(1600,900,Qt.KeepAspectRatio))
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setMaximumSize(700,300)

        self.layout.addWidget(self.label)

    def titleWidget(self,title):
        self.titlelabel = QLabel(title)
        self.titlelabel.setAlignment(Qt.AlignCenter)
        self.titlelabel.setFont(QFont('Arial', 30)) 
        self.titlelabel.setStyleSheet("""
                                      font-weight: bold;
                                      color: white
                                      """
        )
        self.explainlabel.setWordWrap(True)
        self.layout.addWidget(self.titlelabel)

    def ShowWindow(self):
        self.show()

    def quitButton(self):
        self.trayicon.hide()
        self.Run = False
        app.quit()

    def TrayIconQuit(self):
        self.exitAction = self.menu.addAction('Quit')
        self.exitAction.triggered.connect(self.quitButton)

    def TrayIconExplain(self):
        self.explainButton = self.menu.addAction('Explain')
        self.explainButton.triggered.connect(self.ShowWindow)

class GetAPIInfo(MainWindow):
    date="2020-11-20"
    dailyapi = requests.get("https://api.nasa.gov/planetary/apod?api_key=iS0qLB3laA74pCxpMo065L28pe8eSI8cw8ulXqmv&date=" + date).json()
    imgpath = r"C:\Users\filph\Desktop\Sara Project\Resources\sample.jpg"
    backuppath = r"C:\Users\filph\Desktop\Sara Project\Resources\space.jpg"
    path = ""

    def __init__(self):
        #Gets Data from NASA
        self.dailyapi = requests.get("https://api.nasa.gov/planetary/apod?api_key=iS0qLB3laA74pCxpMo065L28pe8eSI8cw8ulXqmv&date=" + self.date).json()
        #Gets HD image URL
        self.imgurl = requests.get(self.dailyapi["hdurl"])
        #Saves image in directory and Sets as background
        self.Update()
        update = threading.Thread(target=self.updateLoop, daemon=True)
        update.start()

    def updateLoop(self):    
        while(MainWindow.Run):
            self.Update()
            time.sleep(86400)
            
    def getApi(self):
        self.dailyapi = requests.get("https://api.nasa.gov/planetary/apod?api_key=iS0qLB3laA74pCxpMo065L28pe8eSI8cw8ulXqmv&date=" + self.date).json()
        self.imgurl = requests.get(self.dailyapi["hdurl"])

    def setBackground(self, path):
        ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)

    def saveImg(self):
        File = open("Resources\sample.jpg","wb")
        File.write(self.imgurl.content)
        File.close()

    def Update(self):
        #Gets Api data
        self.getApi()
        #Saves image in directory and Sets as background
        if self.dailyapi["media_type"] == "image":
            self.saveImg()
            self.setBackground(self.imgpath)
        else:
            self.setBackground(self.backuppath)
            
            

app = QApplication(sys.argv)
window = MainWindow(app)
while window.Run == True:
    app.exec()

# %%
