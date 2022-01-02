from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMenu, QSystemTrayIcon

class TrayIcon(QSystemTrayIcon):
    def __init__(self,app):
        super().__init__(QIcon('Resources\Satellite.ico'),parent=app)
        self.setToolTip("NASA Wallpaper")

        self.menu = QMenu()

        self.explainButton = self.menu.addAction('Explain')
        self.explainButton.triggered.connect(app.showWindow)

        self.exitAction = self.menu.addAction('Quit')
        self.exitAction.triggered.connect(self.quitButton)

        self.setContextMenu(self.menu)
        self.show()

    def quitButton(self, app):
        self.hide()
        self.Run = False
        app.quit()
