import tkinter
import tkinter as tk
from database_and_gui_assignment.create_rows import create_person, create_student
from database_and_gui_assignment.query_database import select_all_persons, select_all_students
from database_and_gui_assignment.create_table import create_tables
from database_and_gui_assignment.connect_to_db import create_connection

m = tkinter.Tk()
m.geometry('1920x1080')
m.title('Guessing Game')
first_name_input = tk.Entry(m, width=70)
last_name_input = tk.Entry(m, width=70)

student_first_name_input = tk.Entry(m, width=70)
student_last_name_input = tk.Entry(m, width=70)
student_major_input = tk.Entry(m, width=70)



def handle_database_creation():
    create_connection("pythonsqlite.db")
    create_tables("pythonsqlite.db")


def add_person():
    conn = create_connection("pythonsqlite.db")
    with conn:
        person = (first_name_input.get(), last_name_input.get())
        create_person(conn, person)
        # add try and except
        first_name_input.delete(0, tk.END)
        last_name_input.delete(0, tk.END)


def add_student():
    conn = create_connection("pythonsqlite.db")
    with conn:
        persons = select_all_persons(conn)

        person = list(
            filter(lambda person: student_first_name_input.get() in person and student_last_name_input.get() in person,
                   persons))
        person_id = person[0][0]
        student = (person_id, student_major_input.get(), '2020-11-20', '2021-11-1')
        try:
            create_student(conn, student)
        except:
            raise Exception('Student database error')


        student_first_name_input.delete(0, tk.END)
        student_last_name_input.delete(0, tk.END)
        student_major_input.delete(0, tk.END)


def query_students():
    conn = create_connection("pythonsqlite.db")
    with conn:
        rows = select_all_students(conn)
        print(rows)
        total_rows = len(rows)
        total_columns = len(rows[0])
        draw_table(rows, total_columns, total_rows, 4)


def query_persons():
    conn = create_connection("pythonsqlite.db")
    with conn:
        rows = select_all_persons(conn)
        total_rows = len(rows)
        total_columns = len(rows[0])
        draw_table(rows, total_columns, total_rows, 1)


def draw_table(rows, total_columns, total_rows, column_index):
    for i in range(total_rows):
        for j in range(total_columns):
            e = tkinter.Entry(m, width=20, fg='black', font=('Arial', 12, 'bold'))

            e.grid(row=i, column=j + column_index)

            e.insert(tkinter.END, rows[i][j])
            e['state'] = tkinter.DISABLED


create_database_button = tkinter.Button(m, text='Create Database and Table', width=60, command=handle_database_creation)
create_database_button.grid(row=0)

# Person content
create_person_button = tkinter.Button(m, text='Add Person', width=60, command=add_person)
create_person_button.grid(row=1)
first_name_input.grid(row=2)
last_name_input.grid(row=3)

view_person_table = tkinter.Button(m, text='View Person Table', width=60, command=query_persons)
view_person_table.grid(row=8)

view_student_table = tkinter.Button(m, text='View Student Table', width=60, command=query_students)
view_student_table.grid(row=9)

create_student_button = tkinter.Button(m, text='Add Student', width=60, command=add_student)
create_student_button.grid(row=4)
student_first_name_input.grid(row=5)
student_last_name_input.grid(row=6)
student_major_input.grid(row=7)

exit_button = tkinter.Button(m, text='Exit', width=60, command=m.destroy)
exit_button.grid(row=10)
m.mainloop()
