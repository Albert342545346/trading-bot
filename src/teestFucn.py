import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget

class DataTableWidget(QTableWidget):
    def __init__(self, data, parent=None):
        super(DataTableWidget, self).__init__(parent)
        self.load_data(data)

    def load_data(self, data):
        if not data:
            return

        rows = len(data)
        columns = len(data[0])

        self.setRowCount(rows)
        self.setColumnCount(columns)
        header_labels = data[0]

        self.setHorizontalHeaderLabels(header_labels)

        for row_index, row_data in enumerate(data[1:]):
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                self.setItem(row_index, col_index, item)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Пример данных в виде обычного массива с именами столбцов
        data_array = [
            ["Name", "Age", "Country"],
            ["John", 30, "USA"],
            ["Anna", 25, "Canada"],
            ["Mike", 35, "UK"],
        ]

        self.data_table_widget = DataTableWidget(data_array, self)

        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        layout.addWidget(self.data_table_widget)

        self.setCentralWidget(central_widget)
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Data Table Viewer')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
