import sqlite3

def check_class_table():
    connection = sqlite3.connect('classes.db')
    cursor = connection.cursor()
    
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='classes'")
    table_exists = cursor.fetchone()
    
    connection.close()
    
    return table_exists is None

def init_classquery():
    connection = sqlite3.connect('classes.db')
    cursor = connection.cursor()
    
    # Create the classes table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS classes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            semester TEXT NOT NULL,
            coursecode TEXT NOT NULL,
            seats INTEGER NOT NULL,
            FOREIGN KEY (semester) REFERENCES semester(semester),
            FOREIGN KEY (coursecode) REFERENCES courses(coursecode)
        )
    ''')
    
    connection.commit()
    connection.close()

def insert_class(semester, coursecode, seats):
    try:
        conn = sqlite3.connect('classes.db')
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO classes (semester, coursecode, seats) VALUES (?, ?, ?)
        ''', (semester, coursecode, seats,))
        
        conn.commit()
        print("Class inserted successfully.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()

def get_classes_by_semester(semester):
    try:
        conn = sqlite3.connect('classes.db')
        cursor = conn.cursor()
        
        cursor.execute("SELECT coursecode, seats FROM classes WHERE semester=?", (semester,))
        classes = [(coursecode, seats) for coursecode, seats in cursor.fetchall()]
        
        return classes
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()