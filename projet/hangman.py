from random import random
from words import words
import random
import string
from hangman_visual import lives_visual_dict


def get_valid_word(words):
    word = random.choice(words)  # randomly chooses something from the list
    while "-" in word or " " in word:
        word = random.choice(words)

    return word.upper()


def hang_man():
    word = get_valid_word(words)
    word_letter = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letter = set()

    lives = 7
    while len(word_letter) > 0 and lives > 0:
        print("The letters have already: ", " ".join(used_letter))

        word_list = [letter if letter in used_letter else "-" for letter in word]
        print(lives_visual_dict[lives])
        print("Current letter: ", " ".join(word_list))
        user_input = input().upper()
        if user_input in alphabet - used_letter:
            used_letter.add(user_input)
            if user_input in word_letter:
                word_letter.remove(user_input)
            else:
                lives -= 1
                print("your live is left ", lives)
        else:
            print("Invalid input")

    if lives == 0:
        print(lives_visual_dict[lives])
        print("You died, sorry. The word was", word)
    else:
        print("YAY! You guessed the word", word, "!!")


hang_man()
