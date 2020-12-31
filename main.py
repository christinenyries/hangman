import random
import words


def get_random_word():
    return random.choice(words.word_list)


def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
        r"""
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / \
                   -
                """,
        # head, torso, both arms, and one leg
        r"""
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / 
                   -
                """,
        # head, torso, and both arms
        r"""
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |      
                   -
                """,
        # head, torso, and one arm
        r"""
                   --------
                   |      |
                   |      O
                   |     \|
                   |      |
                   |     
                   -
                """,
        # head and full torso
        r"""
                   --------
                   |      |
                   |      O
                   |      |
                   |      | 
                   |     
                   -
                """,
        # head and partial torso
        r"""
                   --------
                   |      |
                   |      O
                   |      |
                   |      
                   |     
                   -
                """,
        # head
        r"""
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
        # initial empty state
        r"""
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """,
    ]
    print(stages[tries])


def display_prev_guesses(*, letters, words):
    print(f"{'GUESSED LETTERS':16}:", ", ".join(letters) if letters else "None")
    print(f"{'GUESSED WORDS':16}:", ", ".join(words) if words else "None")


def is_valid_guess(guess):
    return len(guess) > 0 and guess.isalpha()


def play(word):
    word = word.upper()

    # String that represents word completion.
    # A character in `word` is
    #   hidden if not guessed in dash (-)
    #   shown if guessed in uppercase letters (A_Z)
    # Are all dashes initially.
    word_completion = "-" * len(word)

    guessed = False

    guessed_letters = []
    guessed_words = []

    tries = 7
    while not guessed and tries > 0:
        display_hangman(tries)
        print(word_completion)
        display_prev_guesses(letters=guessed_letters, words=guessed_words)
        guess = input("Guess a letter or word: ").upper()
        if not is_valid_guess(guess):
            print("That's an invalid guess. Are you sure that's a letter or word?")
            continue
        elif len(guess) == 1:  # a letter
            if guess in guessed_letters:
                print("Ooops, you already guessed that letter.")
                continue

            if guess not in word:
                print(f"{guess} is not in the word.")
            else:
                print(f"Yup, {guess} is in the word!")

                # Update `word_completion`
                for i, letter in enumerate(word):
                    if letter == guess:
                        word_completion = (
                            word_completion[:i] + guess + word_completion[i + 1 :]
                        )

                # Check if player already guessed all letters
                if word_completion.isalpha():
                    guessed = True
                    continue

            guessed_letters.append(guess)
        else:  # a word
            if guess in guessed_words:
                print("Ooops, you already guessed that word.")
                continue

            if guess != word:
                print(f"{guess} is not the word")
                guessed_words.append(guess)
            else:
                print(f"Yup, {guess} is the word")
                guessed = True
                continue

        tries -= 1
    if guessed and tries >= 0:
        print("Congrats! You have beaten this game.")
    else:
        print("Sorry, you ran out of tries. Please don't lose hope and try again.")
        print(f"The correct word is {word}.")


if __name__ == "__main__":
    play(get_random_word())
    while input("Want to play again? (Y/N) ").upper() == "Y":
        play(get_random_word())