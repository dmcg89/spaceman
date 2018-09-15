import requests
import random
import re
import spacemandrawing

# word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
# response = requests.get(word_site)
# words = response.content.splitlines()
# random_word = random.choice(words)
# slicelength = len(random_word)
guessed_letters = []



def chooseWord():
    word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
    response = requests.get(word_site)
    words = response.content.splitlines()
    random_word = random.choice(words)
    slicelength = len(random_word)
    global secret_word
    secret_word = (str(random_word))[2:slicelength + 2]
    global word_length
    word_length = len(secret_word)

def correctGuesses(word_length):
    global empty_guess
    empty_guess = "_ "
    global correct_guess
    correct_guess = []
    for i in range(0, word_length):
        correct_guess.append(empty_guess)

def user_input(guessed_letters):
    while True:
        global guess_letter
        guess_letter = input("Guess a letter: ").lower()
        if len(guess_letter) > 1 or len(guess_letter) == 0:
            print("Greater than 1 character, Try again")
        elif guess_letter.isalpha() == False:
            print("You didnt guess a letter!")
        elif guess_letter in guessed_letters:
            print("You already guessed that letter")
        else:
            guessed_letters.append(guess_letter)
            return guessed_letters
            return guess_letter
            break

def print_current(correct, guessed):
    print("" .join(correct))
    print(", " .join(guessed))

chooseWord()
correctGuesses(word_length)

print("I'm thinking of a", word_length ,"letter word.")
#
i = 0
while i < 8:
    user_input(guessed_letters)
    indicesForCorrectGuesses = [m.start() for m in re.finditer(guess_letter, secret_word)]
    if indicesForCorrectGuesses == []:
        print("You guessed wrong!")
        print_current(correct_guess, guessed_letters)
        spacemandrawing.drawSpaceMan(i)
        i += 1
    else:
        for j in indicesForCorrectGuesses:
            correct_guess[j] = guess_letter
        if empty_guess in correct_guess:
            print("You guessed right!")
            print_current(correct_guess, guessed_letters)
        else:
            print("You win!")
            print("" .join(correct_guess))
            break
    if i == 7:
        print("You lose!  Loser!")
        print(secret_word)
        break
