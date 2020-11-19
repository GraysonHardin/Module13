from random import randint
class NumberGuesser:
    def __init__(self):
        self.answer = 0
        self.guessed_answer = []

    def generate_answer(self):
        self.answer = randint(1, 10)

    def add_guess(self, guess):
        self.guessed_answer.append(guess)
