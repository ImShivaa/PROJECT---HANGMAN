import random

def hangman_game():
    # TO GET USERNAME
    username = input("Enter your name: ")
    print(f"Welcome to Hangman Game, Let's Go..., {username}!")

    # LIST OF WORDS
    words = ["python", "shiva", "hangman", "developer", "codetech"]
    word = random.choice(words)
    guessed = ["_"] * len(word)
    attempts = 6

    # ASCII ART FROM WEBSITE
    hangman_art = [
        """
          ------
          |    |
          |
          |
          |
          |
        ========
        """,
        """
          ------
          |    |
          |    O
          |
          |
          |
        ========
        """,
        """
          ------
          |    |
          |    O
          |    |
          |
          |
        ========
        """,
        """
          ------
          |    |
          |    O
          |   /|
          |
          |
        ========
        """,
        """
          ------
          |    |
          |    O
          |   /|\\
          |
          |
        ========
        """,
        """
          ------
          |    |
          |    O
          |   /|\\
          |   /
          |
        ========
        """,
        """
          ------
          |    |
          |    O
          |   /|\\
          |   / \\
          |
        ========
        """
    ]

    while attempts > 0:
        print(hangman_art[6 - attempts])
        print("Word:", " ".join(guessed))
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please guess a single letter.")
            continue

        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    guessed[i] = guess
        else:
            attempts -= 1
            print("Wrong guess!")

        if "_" not in guessed:
            print(f"Congratulations, {username}! You Saved the Hang Man Successfully..! \nYou guessed the word: {word}")
            return

    print(hangman_art[-1])
    print(f"Sorry, {username}. You lost! \nThe word was: {word}")
    print("Thank you for playing Hangman Game!")

hangman_game()
