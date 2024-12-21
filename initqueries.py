import semesterquery
import coursequery
import studentsquery
import classquery
import schedulequeries

def init_all():
    if coursequery.check_course_table():
        coursequery.init_coursequery()
    if semesterquery.check_semester_table():
        semesterquery.init_semesterquery()
    if studentsquery.check_student_table():
        studentsquery.init_studentquery()
    if classquery.check_class_table():
        classquery.init_classquery()
    if schedulequeries.check_schedule_table():
        schedulequeries.init_schedulequery()

if __name__ == "__main__":
    try:
        init_all()
    except Exception as e:
        print(f"An error occurred: {e}")
    else:
        print("All tables initialized successfully.")
