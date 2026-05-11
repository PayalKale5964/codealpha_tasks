# Hangman Game using Python

import random

# List of words
words = ["apple", "mango", "banana", "orange", "grapes"]

# Randomly choosing a word
word = random.choice(words)

guessed_letters = []
attempts = 6

print("===== Welcome to Hangman Game =====")

while attempts > 0:

    display = ""

    # Display guessed letters and hidden letters
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    # Check if player won
    if "_" not in display:
        print("Congratulations! You won!")
        break

    # Taking input from player
    guess = input("Guess a letter: ").lower()

    # Checking guessed letter
    if guess in word:
        print("Correct guess!")
        guessed_letters.append(guess)
    else:
        attempts -= 1
        print("Wrong guess!")
        print("Attempts left:", attempts)

# If all attempts are finished
if attempts == 0:
    print("You lost!")
    print("The word was:", word)
