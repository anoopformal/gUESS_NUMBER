import random

def play_game():
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")

    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed it in {attempts} attempts.")
            break


def main():
    while True:
        play_game()
        again = input("Do you want to play again? (yes/no): ").strip().lower()

        if again not in ("yes", "y"):
            print("Thank you for playing!")
            break


if __name__ == "__main__":
    main()
