"""
Program: student_gui.py
Author: Grayson Hardin
Last date modified: 11/23/2020

The GUI down below allows the user to add a person, as well as a student. However, in order to add a student, the first and last name must be in the person database.
"""


import tkinter
import tkinter as tk
from database_and_gui_assignment.create_rows import create_person, create_student
from database_and_gui_assignment.query_database import select_all_persons, select_all_students
from database_and_gui_assignment.create_table import create_tables
from database_and_gui_assignment.connect_to_db import create_connection


class StudentGUI:
    def __init__(self):

        self.m = tkinter.Tk()
        self.m.geometry('1920x1080')
        self.m.title('Guessing Game')
        self.first_name_input = tk.Entry(self.m, width=70)
        self.last_name_input = tk.Entry(self.m, width=70)

        self.student_first_name_input = tk.Entry(self.m, width=70)
        self.student_last_name_input = tk.Entry(self.m, width=70)
        self.student_major_input = tk.Entry(self.m, width=70)
        self.student_start_date = tk.Entry(self.m, width=70)
        self.student_end_date = tk.Entry(self.m, width=70)

    def handle_database_creation(self):  # This establishes the connection with the database
        create_connection("pythonsqlite.db")
        create_tables("pythonsqlite.db")

    def add_person(self):
        conn = create_connection("pythonsqlite.db")
        with conn:
            person = (self.first_name_input.get(), self.last_name_input.get())
            try:  # Wrapped this in a try/except to handle bad input
                create_person(conn, person)
            except:
                raise Exception('Person database error')
            self.first_name_input.delete(0, tk.END)
            self.last_name_input.delete(0, tk.END)

    def add_student(self):
        conn = create_connection("pythonsqlite.db")
        with conn:
            persons = select_all_persons(conn)
            person_id = self.get_person(persons)

            try:
                student = (person_id, self.student_major_input.get(), self.student_start_date.get(), self.student_end_date.get())
                create_student(conn, student)

            except:
                raise Exception('Student database error')

            self.student_first_name_input.delete(0, tk.END)
            self.student_last_name_input.delete(0, tk.END)
            self.student_major_input.delete(0, tk.END)
            self.student_start_date.delete(0, tk.END)
            self.student_end_date.delete(0, tk.END)

    def get_person(self, persons):
        person = list(filter(lambda p: self.student_first_name_input.get() in p and self.student_last_name_input.get() in p, persons))
        if len(person) == 0:  # Raises exception if the person does not exist
            raise Exception('Error: Person does not exist in database')
        return person[0][0]

    def query_students(self):
        conn = create_connection("pythonsqlite.db")
        with conn:
            rows = select_all_students(conn)
            print(rows)
            total_rows = len(rows)
            total_columns = len(rows[0])
            self.draw_table(rows, total_columns, total_rows, 4)

    def query_persons(self):
        conn = create_connection("pythonsqlite.db")
        with conn:
            rows = select_all_persons(conn)
            total_rows = len(rows)
            total_columns = len(rows[0])
            self.draw_table(rows, total_columns, total_rows, 1)

    def draw_table(self, rows, total_columns, total_rows, column_index):  # This method draws the table
        for i in range(total_rows):
            for j in range(total_columns):
                e = tkinter.Entry(self.m, width=20, fg='black', font=('Arial', 12, 'bold'))

                e.grid(row=i, column=j + column_index)

                e.insert(tkinter.END, rows[i][j])
                e['state'] = tkinter.DISABLED

    def start_gui(self):  # This entire method draws the various buttons and messages to the screen
        create_database_button = tkinter.Button(self.m, text='Create Database and Table', width=60,
                                                command=self.handle_database_creation)
        create_database_button.grid(row=0)

        # Person Content
        create_person_button = tkinter.Button(self.m, text='Add Person', width=60, command=self.add_person)
        create_person_button.grid(row=1)
        self.first_name_input.grid(row=2)
        self.last_name_input.grid(row=3)

        view_person_table = tkinter.Button(self.m, text='View Person Table', width=60, command=self.query_persons)
        view_person_table.grid(row=10)

        # Student Content
        view_student_table = tkinter.Button(self.m, text='View Student Table', width=60, command=self.query_students)
        view_student_table.grid(row=11)

        create_student_button = tkinter.Button(self.m, text='Add Student', width=60, command=self.add_student)
        create_student_button.grid(row=4)
        self.student_first_name_input.grid(row=5)
        self.student_last_name_input.grid(row=6)
        self.student_major_input.grid(row=7)
        self.student_start_date.grid(row=8)
        self.student_end_date.grid(row=9)

        exit_button = tkinter.Button(self.m, text='Exit', width=60, command=self.m.destroy)
        exit_button.grid(row=12)
        self.m.mainloop()


if __name__ == '__main__':
    main = StudentGUI()
    main.start_gui()
