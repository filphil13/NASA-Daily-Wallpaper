from PyQt5.QtWidgets import *
import time
from Window import Window
from TrayIcon import TrayIcon
from NetworkInfo import GetAPIInfo
import threading
import sys
import ctypes


class Application(QApplication):
    def __init__(self):
        super().__init__(sys.argv)
        self.Run = True
        self.networkInfo = GetAPIInfo(self)
        self.trayIcon = TrayIcon(self)
        
        self.update = threading.Thread(target=self.updateLoop, daemon=True)
        self.update.start()

        self.window = Window()
        self.window.show()

    def getAppState(self):
        return self.Run
    
    def showWindow(self):
        self.window.show()

    def updateLoop(self):    
        while(self.Run):
            self.Update()
            time.sleep(8640)

    def setBackground(self, path):
        ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)

    def Update(self):
        #Gets Api data
        self.networkInfo.getApi()
        #Saves image in directory and Sets as background
        if self.networkInfo.dailyapi["media_type"] == "image":
            self.networkInfo.saveImg()
            self.setBackground("Resources\space.jpg")
        else:
            self.setBackground(self.networkInfo.backuppath)

App = Application()
while App.Run == True:
    App.exec()
