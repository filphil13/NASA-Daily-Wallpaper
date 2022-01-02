from PyQt5 import QtCore
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel


class TitleWidget(QLabel):
        
    def __init__(self,title):
        super().__init__(title)
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setFont(QFont('Arial', 30)) 
        self.setStyleSheet("""
                                      font-weight: bold;
                                      color: white
                                      """
        )
        self.setWordWrap(True)