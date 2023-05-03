import random

class Hangman:
    def __init__(self, word_list):
        self.word_list = word_list
        self.word = ""
        self.guessed_word = ""
        self.guessed_letters = []
        self.num_guesses = 6
        self.create_new_word()

    def create_new_word(self):
        self.word = random.choice(self.word_list)
        self.guessed_word = ["_"] * len(self.word)
        self.guessed_letters = []

    def guess_letter(self, letter):
        if letter in self.guessed_letters:
            return False
        
        if letter in self.word:
            for i in range(len(self.word)):
                if self.word[i] == letter:
                    self.guessed_word[i] = letter
            self.guessed_letters.append(letter)
            return True
        else:
            self.num_guesses -= 1
            self.guessed_letters.append(letter)
            return False

    def game_over(self):
        return self.num_guesses == 0 or "_" not in self.guessed_word

    def display(self):
        print(" ".join(self.guessed_word))
        print("Guessed letters: {}".format(", ".join(self.guessed_letters)))
        print("Guesses left: {}".format(self.num_guesses))

class HangmanGame:
    def __init__(self):
        self.word_list = ["apple", "banana", "cherry", "dragonfruit", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon", "mango", "nectarine", "orange", "peach", "quince", "raspberry", "strawberry", "tangerine", "ugli fruit", "watermelon"]
        self.hangman = Hangman(self.word_list)

    def run(self):
        print("Welcome to Hangman!")
        while not self.hangman.game_over():
            self.hangman.display()
            letter = input("Guess a letter: ")
            if len(letter) != 1 or not letter.isalpha():
                print("Invalid input, please try again.")
                continue
            if not self.hangman.guess_letter(letter):
                print("Incorrect!")
        if "_" not in self.hangman.guessed_word:
            print("Congratulations, you win!")
        else:
            print("Sorry, you lose. The word was {}.".format(self.hangman.word))

if __name__ == '__main__':
    game = HangmanGame()
    game.run()
