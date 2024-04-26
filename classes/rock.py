import random

class RockPaperScissors:
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors']
        self.user_score = 0
        self.computer_score = 0

    def get_computer_choice(self):
        return random.choice(self.choices)

    def get_user_choice(self):
        choice = input("Choose rock, paper, or scissors: ").lower()
        while choice not in self.choices:
            print("Invalid choice.")
            choice = input("Choose rock, paper, or scissors: ").lower()
        return choice

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "tie"
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            self.user_score += 1
            return "You win"
        else:
            self.computer_score += 1
            return "Computer wins"

    def play_game(self):
        while True:
            user_choice = self.get_user_choice()
            computer_choice = self.get_computer_choice()
            print(f"Computer chose {computer_choice}.")
            result = self.determine_winner(user_choice, computer_choice)
            print(result)
            print(f"Score: You {self.user_score} - Computer {self.computer_score}")
            
            play_again = input("Play again? (yes/no): ").lower()
            if play_again != 'yes':
                break

if __name__ == "__main__":
    game = RockPaperScissors()
    game.play_game()
