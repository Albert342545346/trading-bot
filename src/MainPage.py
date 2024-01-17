from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget
from PyQt5.QtCore import pyqtSignal
import sys

from graph import Graf, Bar

class MainPage(QWidget):
    page = pyqtSignal()

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        
        grafic = Bar({"Apple":10, "Amazon": 20, "Microsoft":50})
        
        layout.addWidget(grafic)
        
    def start(self):
        pass
        

if __name__=="__main__":
    app = QApplication(sys.argv)
    ex = MainPage()
    ex.show()
    app.exec_()