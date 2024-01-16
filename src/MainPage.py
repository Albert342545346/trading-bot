from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import pyqtSignal
import sys

from graph import Graf

class MainPage(QWidget):
    page = pyqtSignal()

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        
        grafic = Graf()
        layout.addWidget(grafic)
        

if __name__=="__main__":
    app = QApplication(sys.argv)
    ex = MainPage()
    ex.show()
    app.exec_()