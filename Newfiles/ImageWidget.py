from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel

class ImageWidget(QLabel):
    def __init__(self,fileLoc):
        super().__init__()
        
        self.pixmap = QPixmap(fileLoc)
        self.setPixmap(self.pixmap)

    def setPicture(self, imageLocation):
        self.pixmap = QPixmap(imageLocation)
        self.setPixmap(self.pixmap)

