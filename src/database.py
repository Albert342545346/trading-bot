

import sqlite3 as sql


def create():
    db = sql.connect("databse.db")
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
    db = sql.connect("databse.db")
    cursor = db.cursor()
    
    cursor.execute(f"""
            INSERT INTO data(date, value) VALUES('{date}', {value})
        """
    )
    
    db.commit()
    db.close()
    


if __name__=="__main__":
    create()