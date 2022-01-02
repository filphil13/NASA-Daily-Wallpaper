from PyQt5 import QtCore
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel


class ExplainWidget(QLabel):
        
    def __init__(self,explanation):
        super().__init__(explanation)
        self.setAlignment(QtCore.Qt.AlignCenter)

        self.setFont(QFont('SansSerif', 8.5)) 
        self.setStyleSheet("""
                                        font-weight: bold;
                                        color: white
                                        """
                            )
        self.setWordWrap(True)