import requests
import random

word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
response = requests.get(word_site)
words = response.content.splitlines()
random_word = random.choice(words)
slicelength = len(random_word)

print(slicelength)
print(random_word)
# secret_word = (str(random_word))[2:slicelength + 2]

secret_word = "lololololo"


wordlength = len(secret_word)

guessed_letters = []

correct_guess = []

empty_guess = "_ "


print(secret_word)


# correct_guess = ''.join ([empty_guess * wordlength])

for i in range (0, wordlength):
    correct_guess.append(empty_guess)


# correct_guess[5] = "A"
# print(correct_guess)

print("I'm thinking of a",wordlength, "letter word.")


i = 1
while i < 10:
    while True:
        guess_letter = input("Guess a letter: ").lower()
        if len(guess_letter) > 1:
            print("Greater than 1 character, Try again")
        else:
            guessed_letters.append(guess_letter)
            print(", " .join(guessed_letters))
            break
    if secret_word.find(guess_letter) == -1:
        print("Guess again sucka!")
        i +=1
    else:
        index = secret_word.find(guess_letter)
        correct_guess[index] = guess_letter
        print(" ".join(correct_guess))
        if empty_guess in correct_guess:
            print("You got one!")
        else:
            print("You Win!")
            break
    if i == 10:
        print("GAME OVER -- LOSER!!!")
