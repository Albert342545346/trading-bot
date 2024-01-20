
import sqlite3 as sql


# <-------------------- GETDATA -------------------->
def createData():
    '''
    
    '''
    
    db = sql.connect("database.db")
    cursor = db.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                date TEXT NOT NULL,
                time TEXT NOT NULL,
                price REAL NOT NULL,
                volume INTEGER NOT NULL
            );
        """
    )
    
    db.commit()
    db.close()
    
    
def addNewData(name, date, time, value):
    '''
    
    '''
    
    db = sql.connect("database.db")
    cursor = db.cursor()
    
    cursor.execute(f"""
            INSERT INTO data(name, date, time, value) VALUES('{name}', '{date}','{time}' {value})
        """
    )
    
    db.commit()
    db.close()
    
    


if __name__=="__main__":
    createData()
    