import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import random


class StockPredictionApp(QMainWindow):
    def __init__(self):
        super(StockPredictionApp, self).__init__()

        self.setWindowTitle('Stock Prediction App')

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        # Создаем виджет для графика Matplotlib
        self.canvas = FigureCanvas(Figure(figsize=(8, 5)))
        self.layout.addWidget(self.canvas)

        # Получаем объект оси графика
        self.ax = self.canvas.figure.add_subplot(111)

        # Инициализация данных
        self.x_data = []
        self.y_data = []

        # Инициализация линии графика
        self.line, = self.ax.plot([], [], 'ro-')

        # Создаем анимацию для обновления графика
        self.animation = self.canvas.figure.canvas.new_timer(interval=1000)
        self.animation.add_callback(self.update_plot)
        self.animation.start()

    def update_plot(self):
        # Добавляем новые данные
        self.x_data.append(len(self.x_data) + 1)
        self.y_data.append(random.randint(1, 10))

        # Очищаем предыдущий график и рисуем новый
        self.ax.clear()
        self.ax.plot(self.x_data, self.y_data, 'ro-')

        # Настройка внешнего вида графика
        self.ax.set_xlabel('Time')
        self.ax.set_ylabel('Stock Price')
        self.ax.set_title('Stock Price Prediction')

        # Обновляем виджет
        self.canvas.draw()


def main():
    app = QApplication(sys.argv)
    stock_app = StockPredictionApp()
    stock_app.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
