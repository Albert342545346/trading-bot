import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLabel, QSpacerItem, QSizePolicy

class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        grid_layout = QGridLayout(self)

        # Виджет 1
        button1 = QPushButton('Виджет 1', self)
        grid_layout.addWidget(button1, 0, 0)

        # Виджет 2
        button2 = QPushButton('Виджет 2', self)
        grid_layout.addWidget(button2, 0, 1)

        # Пустая ячейка
        spacer_item = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        grid_layout.addItem(spacer_item, 0, 2)

        # Виджет 3
        button3 = QPushButton('Виджет 3', self)
        grid_layout.addWidget(button3, 0, 3)

        # Пустая ячейка
        spacer_item = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        grid_layout.addItem(spacer_item, 1, 0)

        # Виджет 4
        label4 = QLabel('Виджет 4', self)
        grid_layout.addWidget(label4, 1, 1)

        self.setLayout(grid_layout)

        self.setWindowTitle('Пример приложения с GridLayout')
        self.setGeometry(100, 100, 400, 300)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
