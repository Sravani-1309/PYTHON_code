import random

def get_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == 1 and computer == 3) or \
         (user == 2 and computer == 1) or \
         (user == 3 and computer == 2):
        return "user"
    else:
        return "computer"

def play_game():
    options = {1: "Rock", 2: "Paper", 3: "Scissors"}
    user_score = 0
    computer_score = 0

    while True:
        print("\nChoose an option:")
        print("1. Rock\n2. Paper\n3. Scissors")
        
        try:
            user_choice = int(input("Enter the number of your choice: "))
            if user_choice not in options:
                print("Invalid choice! Please enter 1, 2, or 3.")
                continue
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        computer_choice = random.randint(1, 3)
        print(f"\nYou chose: {options[user_choice]}")
        print(f"Computer chose: {options[computer_choice]}")
        
        winner = get_winner(user_choice, computer_choice)
        
        if winner == "user":
            print("You win this round! 🎉")
            user_score += 1
        elif winner == "computer":
            print("Computer wins this round! 😢")
            computer_score += 1
        else:
            print("It's a tie!")

        # Display scores
        print(f"\nScore: You - {user_score} | Computer - {computer_score}")

        # Ask user if they want to play again
        while True:
            print("\nDo you want to play again?")
            print("1. Yes\n2. No")
            try:
                play_again = int(input("Enter 1 for Yes or 2 for No: "))
                if play_again == 1:
                    break
                elif play_again == 2:
                    print(f"\nFinal Score: You - {user_score} | Computer - {computer_score}")
                    print("Thanks for playing! Goodbye!")
                    return
                else:
                    print("Invalid choice! Please enter 1 or 2.")
            except ValueError:
                print("Invalid input! Please enter a number.")

if __name__ == "__main__":
    print(" Welcome to Rock, Paper, Scissors (Number Version)!")
    play_game()
