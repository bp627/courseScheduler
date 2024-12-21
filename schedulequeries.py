import sqlite3

def check_schedule_table():
    connection = sqlite3.connect('schedule.db')
    cursor = connection.cursor()
    
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='schedule'")
    table_exists = cursor.fetchone()
    
    connection.close()
    
    return table_exists is None

def init_schedulequery():
    connection = sqlite3.connect('schedule.db')
    cursor = connection.cursor()
    # Create the schedule table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS schedule (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id TEXT NOT NULL,
            semester TEXT NOT NULL,
            course_id TEXT NOT NULL,
            FOREIGN KEY(student_id) REFERENCES students(student_id),
            FOREIGN KEY(semester) REFERENCES semester(semester),
            FOREIGN KEY(course_id) REFERENCES course(course_id)
        )
    ''')
    
    connection.commit()
    connection.close()

def insert_schedule(student_id, semester, course_id):
    try:
        conn = sqlite3.connect('schedule.db')
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO schedule (student_id, semester, course_id) VALUES (?, ?, ?)
        ''', (student_id, semester, course_id,))
        
        conn.commit()
        print("Schedule inserted successfully.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()

def get_schedule_for_student(student_id):
    try:
        conn = sqlite3.connect('schedule.db')
        cursor = conn.cursor()
        
        cursor.execute("SELECT semester, course_id FROM schedule WHERE student_id=?", (student_id,))
        schedule = [(semester, course_id) for semester, course_id in cursor.fetchall()]
        
        return schedule
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()

def drop_class(student_id, semester, course_id):
    try:
        conn = sqlite3.connect('schedule.db')
        cursor = conn.cursor()
        
        cursor.execute("DELETE FROM schedule WHERE student_id=? AND semester=? AND course_id=?", (student_id, semester, course_id))
        
        conn.commit()
        print("Class dropped successfully.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()