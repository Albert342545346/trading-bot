
import sqlite3 as sql


# <------------------- USERS ------------------->
def createUsers():
    '''
    
    '''
    
    db = sql.connect("database.db")
    cursor = db.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                login TEXT NOT NULL,
                password TEXT NOT NULL
            );
        """
    )
    
    db.commit()
    db.close()
    
def addNewUser(login, password):
    '''
    
    '''
    
    db = sql.connect("database.db")
    cursor = db.cursor()
    
    # получаем список зарегистривованых пользователей
    listUsers = getUsers()
    
    # если логин свободен
    if login not in listUsers:
        cursor.execute(f"""
                INSERT INTO users(login, password) VALUES('{login}', '{password}')
            """
        )
        
        db.commit()
        db.close()
        
        return "Success"
    return "Failed"


def getPassword(login):
    '''
    
    '''
    
    
    db = sql.connect("database.db")
    cursor = db.cursor()
    
    cursor.execute(f"""
            SELECT password FROM users WHERE login='{login}'
        """
    )
    
    return cursor.fetchone()[0]


def getUsers():
    '''
    
    '''
    
    db = sql.connect("database.db")
    cursor = db.cursor()
    
    cursor.execute(f"""
            SELECT login FROM users
        """
    )
    
    return [elem[0] for elem in cursor.fetchall()]



# <-------------------- GETDATA -------------------->
def createData():
    '''
    
    '''
    
    db = sql.connect("database.db")
    cursor = db.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                value REAL NOT NULL
            );
        """
    )
    
    db.commit()
    db.close()
    
    
def addNewData(date, value):
    '''
    
    '''
    
    db = sql.connect("database.db")
    cursor = db.cursor()
    
    cursor.execute(f"""
            INSERT INTO data(date, value) VALUES('{date}', {value})
        """
    )
    
    db.commit()
    db.close()
    
    



if __name__=="__main__":
    createUsers()
    createData()
    # тестовый пользователь
    addNewUser("admin", "admin")