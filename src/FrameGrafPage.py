import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLabel, QSizePolicy

from graph import Graf, Bar



class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        grid_layout = QGridLayout(self)

        # Виджет 1
        graf1 = Graf("Apple")
        grid_layout.addWidget(graf1, 0, 0)

        # Виджет 2
        graf2 = Graf("Amazon")
        grid_layout.addWidget(graf2, 0, 1)


        graf3 = Graf("Microsoft")
        grid_layout.addWidget(graf3, 0, 2)

        graf4 = Graf("SpaceX")
        grid_layout.addWidget(graf4, 0, 2)

        self.setLayout(grid_layout)

        self.setWindowTitle('Пример приложения с GridLayout')
        self.setGeometry(100, 100, 400, 300)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
