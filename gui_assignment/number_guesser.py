from random import randint


class NumberGuesser:  # This classes handles the various methods
    def __init__(self):
        self.answer = 0
        self.guessed_answer = []

    def reset_values(self):
        self.answer = 0
        self.guessed_answer = []

    def generate_answer(self):
        self.answer = randint(1, 10)

    def add_guess(self, guess):
        if isinstance(guess, int):
            self.guessed_answer.append(guess)

        else:
            raise ValueError




