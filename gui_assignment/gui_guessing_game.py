"""
Program: gui_guessing_game.py
Author: Grayson Hardin
Last date modified: 11/23/2020

This is a standard guessing game that is available in GUI format. There are 10 guessing options and when the user guesses the right number, it will display a message. Once the game is complete, it will instantly restart.
"""

import tkinter
from gui_assignment.number_guesser import NumberGuesser
from tkinter import messagebox as mb
from functools import partial

number_guesser = NumberGuesser()

m = tkinter.Tk()
m.geometry('400x400')
m.title('Guessing Game')


def handle_gui_reset():  # Upon winning, this resets and draws the game again.
    number_guesser.reset_values()
    draw_options()
    number_guesser.generate_answer()


def draw_options():  # Draws buttons 1-MAX
    for i in range(1, 11):
        button = tkinter.Button(m, text=f'Number {i}', width=60)
        if i == 10:
            button = tkinter.Button(m, text='MAX', width=60)

        button['command'] = partial(handle_guess_numbers, i, button)
        button.grid(row=i + 1)


def handle_guess_numbers(guess, button):  # If the button is guessed correctly, it will add the guess to the list and display a winning message.
    number_guesser.add_guess(guess)
    if number_guesser.answer in number_guesser.guessed_answer:
        mb.showinfo(title="Congrats!", message="You won!")
        handle_gui_reset()
    else:
        button['state'] = tkinter.DISABLED


start_button = tkinter.Button(m, text='Start Game', width=60, command=handle_gui_reset)
start_button.grid(row=1)

exit_button = tkinter.Button(m, text='Exit', width=60, command=m.destroy)
exit_button.grid(row=12)

m.mainloop()
