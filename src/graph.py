from PyQt5.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

import random


MAXCOUNTPOINT = 10


class Graf(QWidget):
    def __init__(self, name:str="Название акции"):
        '''
        
        '''
        
        super().__init__()
        
        self.timer:int = 1000
        self.sizeFigure:tuple = (8, 5)
        
        self.axLine:str = "Время"
        self.ayLine:str = "Курс акции"
        self.titleGraf:str = name
        
        # инициализируем осоновные моменты для отображения графика
        self.initUI()
        
        
    def initUI(self):
        '''
        
        '''
        
        self.layout = QVBoxLayout(self)

        # Создаем виджет для графика Matplotlib
        self.canvas = FigureCanvas(Figure(figsize=self.sizeFigure))
        self.layout.addWidget(self.canvas)

        # Получаем объект оси графика
        self.ax = self.canvas.figure.add_subplot(111)

        # Инициализация данных
        self.x_data = []
        self.y_data = []

        # Инициализация линии графика
        self.line, = self.ax.plot([], [], 'ro-')

        # Создаем анимацию для обновления графика
        self.animation = self.canvas.figure.canvas.new_timer(interval=self.timer)
        self.animation.add_callback(self.update)
        self.animation.start()
        
    def update(self):
        
        # Добавляем новые данные
        self.x_data.append(len(self.x_data) + 1)
        self.y_data.append(random.randint(1, 10))
        
        if len(self.x_data) >= MAXCOUNTPOINT:
            del self.x_data[0]
            
        
        # Очищаем предыдущий график и рисуем новый
        self.ax.clear()
        self.ax.plot(self.x_data, self.y_data, 'ro-')

        # Настройка внешнего вида графика
        self.ax.set_xlabel(self.axLine)
        self.ax.set_ylabel(self.ayLine)
        self.ax.set_title(self.titleGraf)

        # Обновляем виджет
        self.canvas.draw()
        
        

# построение столбчатого графика (диаграммы)
class Bar(QWidget):
    def __init__(self, data:dict):
        super().__init__()
        
        # данные для построения столбчатого графика
        self.data = data
        
        self.initUI()
        
    def initUI(self):

        self.layout = QVBoxLayout(self)

        # Создаем виджет для отображения графика
        self.canvas = FigureCanvas(Figure())
        self.layout.addWidget(self.canvas)

        self.plot()
        
    def plot(self):
        # Извлекаем ключи и значения из словаря
        categories = list(self.data.keys())
        values = list(self.data.values())
        
        figure = self.canvas.figure
        ax = figure.add_subplot(111)

        ax.bar(categories, values, color='black')

        # Обновляем виджет для отображения изменений
        self.canvas.draw()
    
    