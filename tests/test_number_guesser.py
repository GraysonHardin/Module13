import unittest
from unittest.mock import patch
from gui_assignment.number_guesser import NumberGuesser


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.guesser = NumberGuesser()

    def tearDown(self):
        del self.guesser

    def test_init_values(self):
        self.assertEqual(self.guesser.answer, 0)
        self.assertEqual(self.guesser.guessed_answer, [])

    def test_reset_values(self):
        self.guesser.guessed_answer.append(5)
        self.guesser.answer = 4
        self.guesser.reset_values()
        self.assertEqual(self.guesser.answer, 0)
        self.assertEqual(self.guesser.guessed_answer, [])

    @patch('gui_assignment.number_guesser.randint')
    def test_generate_answer(self, mock_randint):
        mock_randint.return_value = 3
        guesser = NumberGuesser()
        guesser.generate_answer()

        self.assertEqual(guesser.answer, 3)

    def test_add_guess(self):
        self.guesser.add_guess(guess=5)
        self.assertEqual(self.guesser.guessed_answer, [5])

    def test_add_guess_validate_value_error(self):
        with self.assertRaises(ValueError):
            self.guesser.add_guess(guess='Bad input')
            self.assertEqual(self.guesser.guessed_answer, [])


if __name__ == '__main__':
    unittest.main()
