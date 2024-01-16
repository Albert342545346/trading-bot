# 
# 
# 
# 

from PyQt5.QtWidgets import QStackedWidget, QMainWindow, QApplication


from LoginPage import LoginPage
from MainPage import MainPage



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Пример QStackedWidget с разными классами QWidget")
        self.setGeometry(100, 100, 400, 300)

        # Создаем QStackedWidget
        self.navigator = QStackedWidget()

        # Создаем экземпляры классов QWidget
        page1 = LoginPage()
        page2 = MainPage()

        # Добавляем виджеты в QStackedWidget
        self.navigator.addWidget(page1)
        self.navigator.addWidget(page2)

        # Устанавливаем QStackedWidget в качестве центрального виджета
        self.setCentralWidget(self.navigator)

        page1.page.connect(self.show_login)
        page2.page.connect(self.show_main)

    def show_login(self):
        self.navigator.setCurrentIndex(1)
        
    def show_main(self):
        self.navigator.setCurrentIndex(0)

# сработает только при запуске файла
# не сработает при импорте из других файлов
if __name__ == '__main__':
    
    app = QApplication([])
    main_win = MainWindow()
    main_win.show()
    app.exec_()
    
    
    
