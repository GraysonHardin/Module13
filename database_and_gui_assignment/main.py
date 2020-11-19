import tkinter
import tkinter as tk
from gui_assignment.number_guesser import NumberGuesser
from tkinter import messagebox as mb
from functools import partial
from database_and_gui_assignment.create_rows import create_person, create_connection
from database_and_gui_assignment.query_database import select_all_persons
from database_and_gui_assignment.connect_to_db import create_and_close_connection
from database_and_gui_assignment.create_table import create_tables

m = tkinter.Tk()
m.geometry('1280x720')
m.title('Guessing Game')
first_name_input = tk.Entry(m, width=70)
last_name_input = tk.Entry(m,  width=70)


def handle_database_creation():
    create_connection("pythonsqlite.db")
    create_tables("pythonsqlite.db")


def add_person():
    conn = create_connection("pythonsqlite.db")
    with conn:
        person = (first_name_input.get(), last_name_input.get())
        create_person(conn, person)

        first_name_input.delete(0, tk.END)
        last_name_input.delete(0, tk.END)


def query_persons():
     conn = create_connection("pythonsqlite.db")
     with conn:
        rows = select_all_persons(conn)
        total_rows = len(rows)
        total_columns = len(rows[0])

        draw_table(rows, total_columns, total_rows)


def draw_table(rows, total_columns, total_rows):
    for i in range(total_rows):
        for j in range(total_columns):
            e = tkinter.Entry(m, width=20, fg='black', font=('Arial', 12, 'bold'))

            e.grid(row=i, column=j + 1)

            e.insert(tkinter.END, rows[i][j])
            e['state'] = tkinter.DISABLED


create_database_button = tkinter.Button(m, text='Create Database and Table', width=60, command=handle_database_creation)
create_database_button.grid(row=0)

create_person_button = tkinter.Button(m, text='Add Person', width=60, command=add_person)
create_person_button.grid(row=1)
first_name_input.grid(row=2)
last_name_input.grid(row=3)

view_person_table = tkinter.Button(m, text='View Person Table', width=60, command=query_persons)
view_person_table.grid(row=4)

exit_button = tkinter.Button(m, text='Exit', width=60, command=m.destroy)
exit_button.grid(row=5)
m.mainloop()
