from PyQt5.QtWidgets import QVBoxLayout, QMainWindow, QApplication, QDesktopWidget
from PyQt5.QtGui import QIcon

from getdata import getDataFromServer
from graph import Graf, Bar
from database import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.WindowSize = (1200, 700)
        self.title = "Trading-Bot"
        
        
        self.initHead()
        self.initUI()
    
    
    def initHead(self):
        
        self.setGeometry(100, 100,*self.WindowSize)
        self.setWindowTitle(self.title)
        
        screen_geometry = QDesktopWidget().availableGeometry()
        window_geometry = self.frameGeometry()
        window_geometry.moveCenter(screen_geometry.center())
        self.move(window_geometry.topLeft())
    
    def initUI(self):
        k = Bar({"apple":100, "microsoft": 12})
        
        layout = QVBoxLayout()
        
        layout.addWidget(k)
        
        self.setLayout(layout)



if __name__ == '__main__':
    createData()
    
    app = QApplication([])
    main_win = MainWindow()
    main_win.show()
    app.exec_()
    
    
    
