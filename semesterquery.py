import sqlite3

def check_semester_table():
    connection = sqlite3.connect('semester.db')
    cursor = connection.cursor()
    
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='semester'")
    table_exists = cursor.fetchone()
    
    connection.close()
    
    return table_exists is None

def init_semesterquery():
    connection = sqlite3.connect('semester.db')
    cursor = connection.cursor()
    
    # Create the semester table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS semester (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            semester TEXT NOT NULL UNIQUE
        )
    ''')
    
    connection.commit()
    connection.close()

def insert_semester(semester_name):
    try:
        conn = sqlite3.connect('semester.db')
        cursor = conn.cursor()
        
        cursor.execute("INSERT INTO semester (semester) VALUES (?)", (semester_name,))
        
        conn.commit()
        print("Semester inserted successfully.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()

def get_semesters():
    try:
        conn = sqlite3.connect('semester.db')
        cursor = conn.cursor()
        
        cursor.execute("SELECT semester FROM semester")
        semesters = [semester[0] for semester in cursor.fetchall()]
        
        return semesters
    except sqlite3.Error as e:
        print(f"An error occurred getting semesters: {e}")
    finally:
        if conn:
            conn.close()