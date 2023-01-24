import random
import os


def select_word():
    """
    A function that returns a random word from a list of words
    """
    words = ["python", "programming", "language", "computer", "science"]
    return random.choice(words)


def play_game(word):
    """
    A function that takes in a word and starts a game where the player needs to guess the word
    """
    # variable to store the number of guesses
    guesses = 0
    # variable to store the letters that have been guessed
    letters_guessed = []
    # variable to store the current state of the word (initially all underscores)
    word_state = ["_"] * len(word)
    while "_" in word_state:
        # increment the number of guesses
        guesses += 1
        # output the current state of the word
        print(" ".join(word_state))
        # get the player's guess
        guess = input("Guess a letter: ").lower()
        # check if the guess is valid
        if guess in letters_guessed:
            print("You already guessed that letter. Try again.")
        elif not guess.isalpha() or len(guess) != 1:
            print("Invalid guess. Please enter a single letter.")
        else:
            # update the letters_guessed and word_state lists
            letters_guessed.append(guess)
            for i, letter in enumerate(word):
                if guess == letter:
                    word_state[i] = letter
    # output a message if the player wins
    print("Congratulations! You guessed the word '{}' in {} guesses.".format(word, guesses))
    # save the game results to a file
    try:
        with open("game_results.txt", "w") as file:
            file.write("Word: {}\n".format(word))
            file.write("Guesses: {}\n".format(guesses))
            file.write("Letters Guessed: {}\n".format(letters_guessed))
    except:
        print("An error occurred while saving the game results.")


# Main Program
word = select_word()
print("Let's play a game! Guess the word.")
play_game(word)
