import unittest
from hangman import Hangman


class TestHangman(unittest.TestCase):

    def test_create_new_word(self):
        word_list = ["testing", "sophie", "mitchell"]
        hangman = Hangman(word_list)
        hangman.create_new_word()
        self.assertIn(hangman.word, word_list)
        self.assertEqual(hangman.guessed_word, ["_"] * len(hangman.word))

    def test_guess_letter(self):
        hangman = Hangman(["mitch"])

        result1 = hangman.guess_letter("m")
        self.assertTrue(result1)
        self.assertEqual(hangman.guessed_word, ["m", "_", "_", "_", "_"])
        self.assertEqual(hangman.guessed_letters, ["m"])
        self.assertEqual(hangman.num_guesses, 6)

        result2 = hangman.guess_letter("s")
        self.assertFalse(result2)
        self.assertEqual(hangman.guessed_word, ["m", "_", "_", "_", "_"])
        self.assertEqual(hangman.guessed_letters, ["m", "s"])
        self.assertEqual(hangman.num_guesses, 5)

    def test_game_over(self):
        hangman = Hangman(["mitch"])
        result = hangman.game_over()
        self.assertFalse(result)

        hangman.num_guesses = 0
        result = hangman.game_over()
        self.assertTrue(result)

        hangman.num_guesses = 5
        hangman.guessed_word = ["m", "i", "t", "c", "h"]
        result = hangman.game_over()
        self.assertTrue(result)

    

if __name__ == '__main__':
    unittest.main()


