import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtCore import QTimer
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Пример с столбчатым графиком в PyQt5 и Matplotlib")
        self.setGeometry(100, 100, 800, 600)

        # Создаем виджет для отображения графика
        self.graph_widget = GraphWidget(self)
        self.setCentralWidget(self.graph_widget)

        # Запускаем таймер для добавления случайных точек
        self.graph_widget.start_timer()

class GraphWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Создаем графический объект и виджет для отображения
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)

        # Создаем макет и добавляем виджет с графиком
        layout = QVBoxLayout(self)
        layout.addWidget(self.canvas)

        # Инициализируем данные для графика
        self.categories = np.arange(1, 11)
        self.values = np.random.rand(10)

        # Построение начального столбчатого графика
        self.bar_container = self.ax.bar(self.categories, self.values)
        self.ax.set_xlabel('Категории')
        self.ax.set_ylabel('Значения')

        # Инициализируем таймер
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_bar_chart)

    def update_bar_chart(self):
        # Обновление значений столбцов
        self.values = np.random.rand(10)

        # Обновление данных в столбчатом графике
        for bar, value in zip(self.bar_container, self.values):
            bar.set_height(value)

        # Перерисовка графика
        self.canvas.draw()

    def start_timer(self):
        # Запуск таймера с интервалом 1000 миллисекунд (1 секунда)
        self.timer.start(1000)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MyMainWindow()
    main_win.show()
    sys.exit(app.exec_())
