# 
# 
# 
# 


from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtCore import pyqtSignal
import sys

# импорт файла с базой данных 
from database import *



class LoginPage(QWidget):
    page = pyqtSignal()
    
    def __init__(self):
        '''
        
        '''

        super().__init__()
    
        self.title:str = "Login"
        self.windowSize:tuple = (100, 100, 300, 150)
        
        # подключаемся к базе данных пользователей
        createUsers()
        self.initHead()
        self.initUI()
    
    def initHead(self):
        '''
        
        '''
        
        self.setWindowTitle(self.title)
        self.setGeometry(*self.windowSize)

    
    def initUI(self):
        '''
        
        '''

        # логин
        self.username_label = QLabel("Имя пользователя:")
        self.username_input = QLineEdit()
        
        # пароль
        self.password_label = QLabel("Пароль:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)

        # конпка авторизации
        self.login_button = QPushButton("Войти")
        self.login_button.clicked.connect(self.auth)
        
        # конпка регистрации
        self.register_button = QPushButton("Зарегистрироваться")
        self.register_button.clicked.connect(self.reg)

        # создание слоя, на котором все будет раполагаться
        layout = QVBoxLayout()
        
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        
        layout.addWidget(self.login_button)
        layout.addWidget(self.register_button)

        self.setLayout(layout)

    def auth(self):
        '''
        
        '''
        # Реализуйте здесь проверку авторизации
        username = self.username_input.text()
        password = self.password_input.text()

        if username in getUsers() and password==getPassword(username):
            QMessageBox.information(self, "Успех", "Вы успешно авторизовались!")
            # переходим на другое окно - ДОМ
            self.page.emit()
        else:
            QMessageBox.warning(self, "Ошибка", "Неверное имя пользователя или пароль.")

    def reg(self):
        '''
        
        '''
        
        # Реализуйте здесь процесс регистрации
        username = self.username_input.text()
        password = self.password_input.text()
        
        if addNewUser(username, password)=="Success":
            QMessageBox.information(self, "Успешно", "Вы успешно зарегистрировались!")
            # переходим на другое окно - ДОМ
            self.page.emit()
        else:
            QMessageBox.information(self, "Ошибка", "Пользователь с таким логином уже есть.")

        




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginPage(None)
    window.show()
    sys.exit(app.exec_())

