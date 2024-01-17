import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QFormLayout

class ProfileApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Профиль пользователя')
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout(self)

        # Создаем форму для отображения информации о профиле
        form_layout = QFormLayout()

        # Добавляем поля для ввода информации
        form_layout.addRow('Имя:', QLineEdit(self))
        form_layout.addRow('Фамилия:', QLineEdit(self))
        form_layout.addRow('Возраст:', QLineEdit(self))
        form_layout.addRow('Город:', QLineEdit(self))

        # Добавляем форму в основной layout
        layout.addLayout(form_layout)

        # Дополнительная информация
        additional_info_label = QLabel('Дополнительная информация:', self)
        layout.addWidget(additional_info_label)

        # Пример текстового блока с дополнительной информацией
        additional_info_text = QLabel('Привет! Это мой пример профиля пользователя. '
                                      'Здесь вы можете внести свои данные.', self)
        layout.addWidget(additional_info_text)

        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ProfileApp()
    window.show()
    sys.exit(app.exec_())
