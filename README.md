🎯 Python Number Guessing Game

A fun, interactive, and beginner-friendly Python project where the computer randomly selects a number between **1 and 100**, and the player must guess it with guided hints.

🚀 Features

* 🔢 Random number generation
* ✔️ Validates user input
* 📉 Too-Low / Too-High hints
* 🧮 Attempt counter
* 🔁 Play-again option
* 🧑‍💻 Clean & readable Python code
* 🐍 Works on any Python 3 setup

 📚 How the Game Works

1. The computer picks a random number between **1–100**
2. You enter guesses
3. The game gives hints:

   * 📉 **Too Low**
   * 📈 **Too High**
4. When correct, you see total attempts
5. You choose whether to play again
 🧩 **Source Code**

```python
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
```

---
 📦 **Requirements**

* Python **3.6+**
* No third-party libraries needed

 ▶️ **How to Run the Program**

```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
python guessing_game.py
```

---

 🏷️ **License**

This project is open-source and free for learning and educational use.

---
 🙌 **Contributions**

Pull requests are welcome.
--------------------------------------------------[ANOOP]

