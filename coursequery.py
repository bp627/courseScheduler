import sqlite3

def check_course_table():
    conn = sqlite3.connect('courses.db')
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='courses'")
    table_exists = cursor.fetchone()

    conn.close()

    return table_exists is None

def init_coursequery():
    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('courses.db')

    # Create a cursor object
    cursor = conn.cursor()

    # Create a table with columns coursecode and description
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS courses (
    coursecode TEXT UNIQUE NOT NULL,
    description TEXT
    )
    ''')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

def insert_course(coursecode, description):
    try:
        conn = sqlite3.connect('courses.db')
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO courses (coursecode, description) VALUES (?, ?)
        ''', (coursecode, description,))
        
        conn.commit()
        print("Course inserted successfully.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()

def get_courses():
    try:
        conn = sqlite3.connect('courses.db')
        cursor = conn.cursor()
        
        cursor.execute("SELECT coursecode FROM courses")
        courses = [course[0] for course in cursor.fetchall()]
        
        return courses
    except sqlite3.Error as e:
        print(f"An error occurred while getting courses: {e}")
    finally:
        if conn:
            conn.close()

def get_course_descriptions():
    try:
        conn = sqlite3.connect('courses.db')
        cursor = conn.cursor()
        
        cursor.execute("SELECT coursecode, description FROM courses")
        course_descriptions = {coursecode: description for coursecode, description in cursor.fetchall()}
        
        return course_descriptions
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()
