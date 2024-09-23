import random

class RockPaperScissors:
    def __init__(self):
        self.choices = ['rock','paper','scissors']
        self.user_score=0
        self.computer_score=0

    def user_choice(self):
        choice=input("Choose rock,paper,or scissors: ").lower()
        while choice not in self.choices:
            print("Invalid choice. Please try again.")
            choice=input("Choose rock, paper, or scissors: ").lower()
        return choice

    def computer_choice(self):
        return random.choice(self.choices)

    def determine_winner(self, user, computer):
        if user==computer:
            return "It's a tie!"
        elif (user=='rock' and computer=='scissors') or \
             (user=='scissors' and computer=='paper') or \
             (user=='paper'and computer=='rock'):
            self.user_score+=1
            return "You win!"
        else:
            self.computer_score += 1
            return "You lose!"

    def display_scores(self):
        print(f"\nScores:\nYou: {self.user_score}\nComputer: {self.computer_score}\n")

    def play_again(self):
        choice=input("Do you want to play again? (yes/no): ").lower()
        return choice in ['yes','y']

    def play_game(self):
        print("Welcome to Rock-Paper-Scissors!")
        while True:
            user=self.user_choice()
            computer=self.computer_choice()
            print(f"\nYou chose: {user}\nComputer chose: {computer}")

            result=self.determine_winner(user, computer)
            print(result)

            self.display_scores()

            if not self.play_again():
                print("Thanks for playing! Goodbye!")
                break

if __name__ =="__main__":
    game=RockPaperScissors()
    game.play_game()
