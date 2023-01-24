import random


class Game:
    def __init__(self):
        self.number = random.randint(1, 100)
        self.guesses = 0

    def check_guess(self, guess):
        if self.number == guess:
            return True
        elif self.number > guess:
            return 'Too Low'
        elif self.number < guess:
            return 'Too High'

    def guess_number(self):
        while True:
            guess = int(input("Enter your guess: "))
            self.guesses += 1
            result = self.check_guess(guess)
            if result == True:
                print(f'Congratulations, you guessed the number in {self.guesses} attempts')
                break
            else:
                print(result)


class AdvancedGame(Game):
    def __init__(self):
        super().__init__()
        self.hint = random.choice(['even', 'odd'])

    def check_guess(self, guess):
        if self.hint == 'even' and guess % 2 != 0:
            return 'Hint: The number is even'
        elif self.hint == 'odd' and guess % 2 == 0:
            return 'Hint: The number is odd'
        else:
            return super().check_guess(guess)


game = Game()
game.guess_number()

adv_game = AdvancedGame()
adv_game.guess_number()
