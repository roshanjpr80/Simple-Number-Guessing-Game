import random
import sys
import time


def slow_print(text, delay=0.02):
    """Print text with typing animation."""
    for char in text:
        print(char, end="")
        sys.stdout.flush()
        time.sleep(delay)
    print()


def generate_random_number(level):
    """
    Generate number based on difficulty level.
    """
    ranges = {
        "1": (1, 50),
        "2": (1, 100),
        "3": (1, 200)
    }
    return random.randint(*ranges[level])


def get_attempts(level):
    """Return attempts based on difficulty."""
    attempts = {"1": 7, "2": 5, "3": 4}
    return attempts[level]


def choose_difficulty():
    """Ask user to choose difficulty level."""
    print("\nSelect Difficulty Level:")
    print("1️⃣  Easy (1–50) – 7 Attempts")
    print("2️⃣  Medium (1–100) – 5 Attempts")
    print("3️⃣  Hard (1–200) – 4 Attempts")

    while True:
        choice = input("Enter your choice (1/2/3): ")
        if choice in ["1", "2", "3"]:
            return choice
        else:
            print("❌ Invalid choice! Please choose 1, 2, or 3.")


def get_user_guess(range_limit):
    """Validate user guess input."""
    while True:
        try:
            guess = int(input(f"Enter your guess (1 to {range_limit}): "))
            if 1 <= guess <= range_limit:
                return guess
            print(f"❗ Number must be between 1 and {range_limit}.")
        except ValueError:
            print("❌ Please enter a valid number!")


def play_game():
    """Main game logic."""
    slow_print("\n🎉 WELCOME TO THE NUMBER GUESSING GAME! 🎉\n", 0.01)

    name = input("Please enter your Name: ")

    difficulty = choose_difficulty()
    range_map = {"1": 50, "2": 100, "3": 200}

    random_number = generate_random_number(difficulty)
    attempts = get_attempts(difficulty)
    max_range = range_map[difficulty]

    print(f"\n🎯 The number has been generated between 1 and {max_range}.")
    print(f"🔢 You have {attempts} attempts. Good luck, {name}!\n")

    for attempt in range(1, attempts + 1):
        print(f"Attempt {attempt}/{attempts}")
        guess = get_user_guess(max_range)

        if guess == random_number:
            slow_print("\n🎉🎉 AMAZING! You guessed the correct number! 🎉🎉", 0.01)
            slow_print(f"🏆 {name}, You WON the game!\n")
            break
        elif guess < random_number:
            print("🔼 Too low! Try a higher number.\n")
        else:
            print("🔽 Too high! Try a lower number.\n")
    else:
        print("\n❌ GAME OVER!")
        print(f"😢 Sorry {name}, the correct number was: {random_number}\n")

    # Ask for replay
    again = input("🔁 Do you want to play again? (yes/no): ").lower().strip()
    if again in ["yes", "y"]:
        play_game()
    else:
        slow_print("\n💚 Thank you for playing! Goodbye!\n")


# Run the program
play_game()
