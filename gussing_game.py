# This script implements a number-guessing game using Python.

# import random


# def generate_random_number(): 
#     """ 
#     Generates a random number between 1 and 100. 
#     Returns: 
#     int: A randomly selected number. 
#     """ 

#     return random.randint(1, 100)



# def get_user_guess(): 
#     """ 
#     Prompts the user to enter a guess and validates the input. 
#     Returns: 
#     int: The user's valid guess. 
#     """

#     while True:
#         try:
#             guess = int(input("Enter your guess (beetween 1 to 100) :- "))
#             if 1 <= guess <= 100:
#                 return guess
            
#             else:
#                 print("Please enter a number beetween 1 to 100.")

#         except Exception as err:
#             print(f"Exception occur {err}.")
#             print("Please enter a vaild number.")




# def play_game(): 
#     """ 
#     Runs the number guessing game. 
#     The user attempts to guess the randomly generated number within 5 tries. 
#     """ 

#     print("\n\n#####  WLCOME TO THE NUMBER GUESSING GAME!  #####\n")
#     print("You have 5  chances to guess the number.\n")
#     randam_number = generate_random_number()
#     name = input("Please enter your Name :- ")

#     for i in range(5):
#         print(f"\nAttept {i + 1}")
#         user_number = get_user_guess()

#         if user_number == randam_number:
#             print("*\n\n****  Congratulations! You guessed the correct number.  *****")
#             print(f"       {name} You are Winner the game!!!")
#             break

#         elif user_number < randam_number:
#             print("Try a higher number.")

#         else:
#             print("Try a lower number.")

#     else:
#         print(f"\nSorry {name}!!!  You are lost the game.")



# play_game()













import random


def generate_random_number():
    """
    Generates a random number between 1 and 100.

    Returns:
        int: A randomly selected number.
    """
    return random.randint(1, 100)


def get_user_guess():
    """
    Prompts the user to enter a guess and validates the input.

    Returns:
        int: The user's valid guess.
    """
    while True:
        try:
            guess = int(input("Enter your guess (between 1 to 100): "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("❗ Please enter a number between 1 and 100.")
        except ValueError:
            print("❗ Invalid input! Please enter a valid number.")


def play_game():
    """
    Runs the number guessing game.
    The user has 5 chances to guess the correct number.
    """
    print("\n\n#####  WELCOME TO THE NUMBER GUESSING GAME!  #####\n")
    print("🎯 You have 5 chances to guess the number.\n")

    random_number = generate_random_number()
    name = input("Enter your name: ")

    for attempt in range(1, 6):
        print(f"\nAttempt {attempt} of 5")
        user_guess = get_user_guess()

        if user_guess == random_number:
            print("\n🎉🎉 Congratulations! You guessed the correct number! 🎉🎉")
            print(f"🏆 {name}, You WON the game!")
            break
        elif user_guess < random_number:
            print("🔼 Try a higher number!")
        else:
            print("🔽 Try a lower number!")
    else:
        print("\n❌ Game Over!")
        print(f"😢 Sorry {name}, you LOST the game.")
        print(f"The correct number was: {random_number}")


# Run the game
play_game()
