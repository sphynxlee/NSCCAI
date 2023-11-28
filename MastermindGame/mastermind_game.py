import random

def generate_code():
    colors = ["Black", "White", "Red", "Blue", "Green", "Yellow"]
    secret_code = []
    for i in range(6):
        secret_code.append(random.choice(colors))
    return secret_code

def notify_user(secret_code, guess):
    perfect_match = 0
    right_colors = 0

    # find out how many perfect matches and right colors
    for i in range(6):
        if guess[i] == secret_code[i]:
            perfect_match += 1

    # find out how many right colors
    for i in range(6):
        right_colors += min(secret_code.count(guess[i]), guess.count(guess[i]))

    # find out how many right colors are not perfect matches
    right_colors -= perfect_match

    return perfect_match, right_colors


def play_game():
    secret_code = generate_code()
    attempts = 15
    print("Welcome to Mastermind! You have 15 attempts to guess the secret code.")
    while attempts > 0:
        guess = input("Enter your guess (comma-separated colors): ").split(", ")

        # Convert each color to lowercase
        guess_lower = [color.lower() for color in guess]

        # Convert secret_code to lowercase
        secret_code_lower = [color.lower() for color in secret_code]

        # Check if the user guessed the secret code
        if guess_lower == secret_code_lower:
            print("Congratulations! You guessed the secret code!")
            return

        perfect_match, right_colors = notify_user(secret_code_lower, guess_lower)
        print(f"Feedback: {perfect_match} exact matches, {right_colors} right colors")

        attempts -= 1

    print(f"Game over! The secret code was {secret_code}")

play_game()