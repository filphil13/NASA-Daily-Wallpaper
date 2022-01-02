from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from ExplainWidget import ExplainWidget
from ImageWidget import ImageWidget
from TitleWidget import TitleWidget


class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('NASA Pic of the Day')
        self.setWindowIcon(QIcon("Resources\Satellite.ico"))
        self.setFixedSize(700,800)

        self.setStyleSheet("background-color: black;")

        self.layout = QVBoxLayout()
        
        #input parameters when networking side is done
        self.titleWidget = TitleWidget("hello")
        self.explainWidget = ExplainWidget("this is a test")
        self.imageWidget = ImageWidget("Resources\sample.jpg")
        self.layout.addWidget(self.explainWidget)
        self.layout.addWidget(self.titleWidget)

    def setExplainWidget(self,explanation):
        self.explainWidget.setText(explanation)
        self.layout.addWidget(self.explainWidget)

    def setTitleWidget(self,title):
        self.titleWidget.setText(title)
        self.layout.addWidget(self.titleWidget)

    def setImageWidget(self):
        
        self.layout.addWidget(self.label)
