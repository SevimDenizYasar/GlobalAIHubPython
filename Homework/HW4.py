class Hangman:
    
    def __init__(self, secret, hint, life):
        self.secret = secret
        self.hint = hint
        self.life = life
        self.chosen = []

    def play(self):
        
        self.gui()

        while self.life > 0:
            secret_letters = [letter for letter in self.secret.lower()]

            if set(self.chosen) == set(secret_letters):
                print("Congratulations, you've finished the game!!")
                break
            
            for s in secret_letters:
                if s in self.chosen:
                    print(s)
                else:
                    print('*')

            letter = input('Guess a letter: ')

            if letter in secret_letters:
                self.chosen.append(letter)
            else:
                self.life -= 1
                print(f'You have {self.life} attempts left.')

    def gui(self):
        print('**************************************************')
        print('Welcome to hangman game..')
        print(f'You have a total of {self.life} lives in the game.')
        print(f'Your hint for the specified sentence: {self.hint}.')
        print("Don't forget to enter the 'space' key for spaces between words.")
        print('**************************************************')


game = Hangman('Python', 'Bir programlama dili', 5)
game.play()