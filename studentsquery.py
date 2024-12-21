import sqlite3

def check_student_table():
    connection = sqlite3.connect('students.db')
    cursor = connection.cursor()
    
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='students'")
    table_exists = cursor.fetchone()
    
    connection.close()
    
    return table_exists is None

def init_studentquery():
    connection = sqlite3.connect('students.db')
    cursor = connection.cursor()

    # Create the students table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id TEXT NOT NULL UNIQUE,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL
        )
    ''')
    
    connection.commit()
    connection.close()

def insert_student(student_id, first_name, last_name):
    try:
        conn = sqlite3.connect('students.db')
        cursor = conn.cursor()
        
        cursor.execute("INSERT INTO students (student_id, first_name, last_name) VALUES (?, ?, ?)", (student_id, first_name, last_name,))
        
        conn.commit()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()

def get_student_ids():
    try:
        conn = sqlite3.connect('students.db')
        cursor = conn.cursor()
        
        cursor.execute("SELECT student_id FROM students")
        student_ids = [student_id[0] for student_id in cursor.fetchall()]
        
        return student_ids
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()