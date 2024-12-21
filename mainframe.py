import tkinter as tk
from tkinter import ttk
import semesterquery
import coursequery
import studentsquery
import classquery
import schedulequeries
import initqueries

class CourseScheduler(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Course Scheduler")
        self.geometry("1000x600")

        # Add title at the top
        title_label = ttk.Label(self, text="Course Scheduler", font=("Helvetica", 16))
        title_label.pack(pady=10)

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill='both')

        self.create_admin_tab()
        self.create_student_tab()

    def create_admin_tab(self):
        admin_frame = ttk.Frame(self.notebook)
        self.notebook.add(admin_frame, text='Admin')

        admin_notebook = ttk.Notebook(admin_frame)
        admin_notebook.pack(expand=True, fill='both')

        self.add_admin_tabs(admin_notebook)

    def create_student_tab(self):
        student_frame = ttk.Frame(self.notebook)
        self.notebook.add(student_frame, text='Student')

        # Add Student ID TextBox and Validate Button
        student_id_label = ttk.Label(student_frame, text="Student ID:")
        student_id_label.pack(pady=(20, 5), padx=20)

        self.student_id_entry = ttk.Entry(student_frame)
        self.student_id_entry.pack(pady=5, padx=20)

        validate_button = ttk.Button(student_frame, text="Validate", command=self.validate_student_id)
        validate_button.pack(pady=(5, 20), padx=20)

        self.student_notebook = ttk.Notebook(student_frame)
        self.student_notebook.pack(expand=True, fill='both')

    def validate_student_id(self):
        student_id = self.student_id_entry.get()
        if student_id in studentsquery.get_student_ids():
            for widget in self.student_notebook.winfo_children():
                widget.destroy()
            self.add_student_tabs(self.student_notebook)

    def add_admin_tabs(self, admin_notebook):
        self.create_add_semester_tab(admin_notebook)
        self.create_add_course_tab(admin_notebook)
        self.create_add_student_tab(admin_notebook)
        self.create_add_class_tab(admin_notebook)

    def add_student_tabs(self, student_notebook):
        self.create_display_classes_tab(student_notebook)
        self.create_schedule_classes_tab(student_notebook)
        self.create_display_student_schedule_tab(student_notebook)
        self.create_drop_class_tab(student_notebook)

    def create_add_semester_tab(self, notebook):
        frame = ttk.Frame(notebook)
        notebook.add(frame, text="Add Semester")

        # Label for Semester Name
        label = ttk.Label(frame, text="Semester Name:")
        label.pack(pady=(20, 5), padx=20)

        # TextBox for entering Semester Name
        self.semester_entry = ttk.Entry(frame)
        self.semester_entry.pack(pady=5, padx=20)

        # Enter Button
        button = ttk.Button(frame, text="Enter", command=self.handle_enter)
        button.pack(pady=(5, 20), padx=20)

    def handle_enter(self):
        semester_name = self.semester_entry.get()
        if semester_name:
            semesterquery.insert_semester(semester_name)  # Call the add_semester function from semesterquery.py
            self.semester_entry.delete(0, tk.END)

    def create_add_course_tab(self, notebook):
        frame = ttk.Frame(notebook)
        notebook.add(frame, text="Add Course")

        # Label for Course Code
        course_code_label = ttk.Label(frame, text="Course Code:")
        course_code_label.pack(pady=(20, 5), padx=20)

        # TextBox for entering Course Code
        self.course_code_entry = ttk.Entry(frame)
        self.course_code_entry.pack(pady=5, padx=20)

        # Label for Course Description
        course_description_label = ttk.Label(frame, text="Course Description:")
        course_description_label.pack(pady=(20, 5), padx=20)

        # TextBox for entering Course Description
        self.course_description_entry = tk.Text(frame, height=2, width=40)
        self.course_description_entry.pack(pady=5, padx=20)

        # Enter Button
        button = ttk.Button(frame, text="Enter", command=self.handle_course_enter)
        button.pack(pady=(5, 20), padx=20)

    def handle_course_enter(self):
        course_code = self.course_code_entry.get()
        course_description = self.course_description_entry.get("1.0", tk.END).strip()
        if course_code and course_description:
            coursequery.insert_course(course_code, course_description)  # Call the insert_course function from entryqueries.py
            self.course_code_entry.delete(0, tk.END)
            self.course_description_entry.delete("1.0", tk.END)

    def create_add_student_tab(self, notebook):
        frame = ttk.Frame(notebook)
        notebook.add(frame, text="Add Student")

        # Label for Student ID
        student_id_label = ttk.Label(frame, text="Student ID:")
        student_id_label.pack(pady=(20, 5), padx=20)

        # TextBox for entering Student ID
        self.admin_student_id_entry = ttk.Entry(frame)
        self.admin_student_id_entry.pack(pady=5, padx=20)

        # Label for First Name
        first_name_label = ttk.Label(frame, text="First Name:")
        first_name_label.pack(pady=(20, 5), padx=20)

        # TextBox for entering First Name
        self.first_name_entry = ttk.Entry(frame)
        self.first_name_entry.pack(pady=5, padx=20)

        # Label for Last Name
        last_name_label = ttk.Label(frame, text="Last Name:")
        last_name_label.pack(pady=(20, 5), padx=20)

        # TextBox for entering Last Name
        self.last_name_entry = ttk.Entry(frame)
        self.last_name_entry.pack(pady=5, padx=20)

        # Enter Button
        button = ttk.Button(frame, text="Enter", command=self.handle_student_enter)
        button.pack(pady=(5, 20), padx=20)

    def handle_student_enter(self):
        student_id = self.admin_student_id_entry.get()
        print("Student ID: ", student_id)
        first_name = self.first_name_entry.get()
        print("First Name: ", first_name)
        last_name = self.last_name_entry.get()
        print("Last Name: ", last_name)
        if student_id and first_name and last_name:
            studentsquery.insert_student(student_id, first_name, last_name)  # Call the insert_student function from entryqueries.py
            self.student_id_entry.delete(0, tk.END)
            self.first_name_entry.delete(0, tk.END)
            self.last_name_entry.delete(0, tk.END)

    def create_add_class_tab(self, notebook):
        frame = ttk.Frame(notebook)
        notebook.add(frame, text="Add Class")

        # Label for Semesters
        semester_label = ttk.Label(frame, text="Select Semester:")
        semester_label.pack(pady=(20, 5), padx=20)

        # Dropdown for selecting Semester
        self.selected_semester = tk.StringVar()
        self.semester_menu = ttk.Combobox(frame, textvariable=self.selected_semester)
        self.semester_menu.pack(pady=5, padx=20)

        # Label for Courses
        course_label = ttk.Label(frame, text="Select Course:")
        course_label.pack(pady=(20, 5), padx=20)

        # Dropdown for selecting Course
        self.selected_course = tk.StringVar()
        self.course_menu = ttk.Combobox(frame, textvariable=self.selected_course)
        self.course_menu.pack(pady=5, padx=20)

        # Label for Seats
        seats_label = ttk.Label(frame, text="Seats:")
        seats_label.pack(pady=(20, 5), padx=20)

        # Spinbox for entering Seats
        self.seats_spinbox = tk.Spinbox(frame, from_=0, to=300)
        self.seats_spinbox.pack(pady=5, padx=20)

        # Enter Button
        button = ttk.Button(frame, text="Enter", command=self.handle_class_enter)
        button.pack(pady=(5, 20), padx=20)

        # Bind the tab click event to reload dropdown values
        notebook.bind("<<NotebookTabChanged>>", self.on_tab_changed)

    def on_tab_changed(self, event):
        tab = event.widget.tab(event.widget.index("current"))["text"]
        if tab == "Add Class":
            self.reload_dropdown_values()

    def reload_dropdown_values(self):
        self.semester_menu['values'] = semesterquery.get_semesters()
        self.course_menu['values'] = coursequery.get_courses()

    def handle_class_enter(self):
        semester = self.selected_semester.get()
        course = self.selected_course.get()
        seats = self.seats_spinbox.get()
        if semester and course and seats:
            classquery.insert_class(semester, course, seats)  # Call the insert_class function from classquery.py
            self.semester_menu.set('')
            self.course_menu.set('')
            self.seats_spinbox.delete(0, tk.END)
            self.seats_spinbox.insert(0, '0')

    def create_display_classes_tab(self, notebook):
        frame = ttk.Frame(notebook)
        notebook.add(frame, text="Display Classes")

        # Label for Semesters
        semester_label = ttk.Label(frame, text="Select Semester:")
        semester_label.pack(pady=(20, 5), padx=20)

        # Dropdown for selecting Semester
        self.selected_display_semester = tk.StringVar()
        self.display_semester_menu = ttk.Combobox(frame, textvariable=self.selected_display_semester)
        self.display_semester_menu.pack(pady=5, padx=20)

        # Button to display classes
        button = ttk.Button(frame, text="Display Classes", command=self.handle_display_classes)
        button.pack(pady=(5, 20), padx=20)

        # Treeview widget to display classes as a table
        self.classes_tree = ttk.Treeview(frame, columns=("Course", "Description", "Seats"), show='headings')
        self.classes_tree.heading("Course", text="Course")
        self.classes_tree.heading("Description", text="Description")
        self.classes_tree.heading("Seats", text="Seats")
        self.classes_tree.pack(pady=5, padx=20)

        # Reload the values for semester dropdown
        self.reload_display_semester_values()

    def reload_display_semester_values(self):
        self.display_semester_menu['values'] = semesterquery.get_semesters()

    def handle_display_classes(self):
        semester = self.selected_display_semester.get()
        if semester:
            classes = classquery.get_classes_by_semester(semester)  # Call the get_classes_by_semester function from classquery.py
            course_descriptions = coursequery.get_course_descriptions()
            for i in self.classes_tree.get_children():
                self.classes_tree.delete(i)
            for cls in classes:
                self.classes_tree.insert("", "end", values=(cls[0], course_descriptions[cls[0]], cls[1]))

    def create_schedule_classes_tab(self, notebook):
        frame = ttk.Frame(notebook)
        notebook.add(frame, text="Schedule Classes")

        # Label for Semesters
        semester_label = ttk.Label(frame, text="Select Semester:")
        semester_label.pack(pady=(20, 5), padx=20)

        # Dropdown for selecting Semester
        self.selected_schedule_semester = tk.StringVar()
        self.schedule_semester_menu = ttk.Combobox(frame, textvariable=self.selected_schedule_semester)
        self.schedule_semester_menu.pack(pady=5, padx=20)
        self.schedule_semester_menu.bind("<<ComboboxSelected>>", self.update_schedule_courses)

        # Label for Courses
        course_label = ttk.Label(frame, text="Select Course:")
        course_label.pack(pady=(20, 5), padx=20)

        # Dropdown for selecting Course
        self.selected_schedule_course = tk.StringVar()
        self.schedule_course_menu = ttk.Combobox(frame, textvariable=self.selected_schedule_course)
        self.schedule_course_menu.pack(pady=5, padx=20)

        # Enter Button
        button = ttk.Button(frame, text="Enter", command=self.handle_schedule_enter)
        button.pack(pady=(5, 20), padx=20)

        # Reload the values for semester dropdown
        self.reload_schedule_semester_values()

    def handle_schedule_enter(self):
        student_id = self.student_id_entry.get()
        semester = self.selected_schedule_semester.get()
        course = self.selected_schedule_course.get()
        if student_id and semester and course:
            schedulequeries.insert_schedule(student_id, semester, course)  # Call the insert_schedule function from schedulequeries.py

    def reload_schedule_semester_values(self):
        self.schedule_semester_menu['values'] = semesterquery.get_semesters()
        self.schedule_course_menu.set('')  # Clear the course selection

    def update_schedule_courses(self, event):
        semester = self.selected_schedule_semester.get()
        if semester:
            courses = classquery.get_classes_by_semester(semester)  # Call the get_courses_by_semester function from classquery.py
            self.schedule_course_menu['values'] = [course[0] for course in courses]
            self.schedule_course_menu.set('')  # Clear the course selection

    def create_display_student_schedule_tab(self, notebook):
        frame = ttk.Frame(notebook)
        notebook.add(frame, text="Display Student Schedule")

        # Button to display schedule
        button = ttk.Button(frame, text="Display Schedule", command=self.handle_display_student_schedule)
        button.pack(pady=(20, 20), padx=20)

        # Treeview widget to display schedule as a table
        self.schedule_tree = ttk.Treeview(frame, columns=("Semester", "Course"), show='headings')
        self.schedule_tree.heading("Semester", text="Semester")
        self.schedule_tree.heading("Course", text="Course")
        self.schedule_tree.pack(pady=5, padx=20)

    def handle_display_student_schedule(self):
        student_id = self.student_id_entry.get()
        if student_id:
            schedule = schedulequeries.get_schedule_for_student(student_id)  # Call the get_schedule function from schedulequeries.py
            for i in self.schedule_tree.get_children():
                self.schedule_tree.delete(i)
            for cls in schedule:
                self.schedule_tree.insert("", "end", values=(cls[0], cls[1]))

    def create_drop_class_tab(self, notebook):
        frame = ttk.Frame(notebook)
        notebook.add(frame, text="Drop Class")

        # Label for Semesters
        semester_label = ttk.Label(frame, text="Select Semester:")
        semester_label.pack(pady=(20, 5), padx=20)

        # Dropdown for selecting Semester
        self.selected_drop_semester = tk.StringVar()
        self.drop_semester_menu = ttk.Combobox(frame, textvariable=self.selected_drop_semester)
        self.drop_semester_menu.pack(pady=5, padx=20)
        self.drop_semester_menu.bind("<<ComboboxSelected>>", self.update_drop_courses)

        # Label for Courses
        course_label = ttk.Label(frame, text="Select Course:")
        course_label.pack(pady=(20, 5), padx=20)

        # Dropdown for selecting Course
        self.selected_drop_course = tk.StringVar()
        self.drop_course_menu = ttk.Combobox(frame, textvariable=self.selected_drop_course)
        self.drop_course_menu.pack(pady=5, padx=20)

        # Enter Button
        button = ttk.Button(frame, text="Enter", command=self.handle_drop_enter)
        button.pack(pady=(5, 20), padx=20)

        # Reload the values for semester dropdown
        self.reload_drop_semester_values()

    def handle_drop_enter(self):
        student_id = self.student_id_entry.get()
        semester = self.selected_drop_semester.get()
        course = self.selected_drop_course.get()
        if student_id and semester and course:
            schedulequeries.drop_class(student_id, semester, course)

    def reload_drop_semester_values(self):
        self.drop_semester_menu['values'] = semesterquery.get_semesters()
        self.drop_course_menu.set('')  # Clear the course selection

    def update_drop_courses(self, event):
        semester = self.selected_drop_semester.get()
        if semester:
            courses = classquery.get_classes_by_semester(semester)  # Call the get_classes_by_semester function from classquery.py
            self.drop_course_menu['values'] = [course[0] for course in courses]
            self.drop_course_menu.set('')  # Clear the course selection

if __name__ == "__main__":
    initqueries.init_all()
    app = CourseScheduler()
    app.mainloop()