import random

def rockpaperscissors():
    """Plays a 5-round game of Rock, Paper, Scissors with the user and compares scores."""

    print("Welcome to Rock, Paper, Scissors!")
    print("Here are the rules:")
    print("- Rock beats Scissors")
    print("- Scissors beats Paper")
    print("- Paper beats Rock")

    user_score = 0
    computer_score = 0  # Initialize computer score
    choices = ["rock", "paper", "scissors"]

    for i in range(1, 6):
        print(f"\nLevel {i}")
        while True:
            user_input = input("Enter your choice: (rock, paper, or scissors): ").lower()
            if user_input in choices:
                break
            else:
                print("Invalid choice. Please try again.")

        computer_input = random.choice(choices)
        print(f"You chose: {user_input}")
        print(f"The computer chose: {computer_input}")

        if user_input == computer_input:
            print("It's a tie!")
        elif (user_input == "rock" and computer_input == "scissors") or \
             (user_input == "paper" and computer_input == "rock") or \
             (user_input == "scissors" and computer_input == "paper"):
            print("You win!")
            user_score += 1
        else:
            print("You lose!")
            computer_score += 1 #Increment computer score

    print(f"\nGame Over!")
    print(f"Your final score: {user_score}/5")
    print(f"Computer's final score: {computer_score}/5")

    if user_score > computer_score: # Compare scores
        print("You are the overall winner!")
    elif user_score < computer_score:
        print("The computer is the overall winner!")
    else:
        print("It's an overall tie!")


# Start the game
rockpaperscissors()
play_again = input("Do you want to play again? (yes/no): ").lower()
if play_again == "yes":
    rockpaperscissors()
else:
    print("Thanks for playing!")
