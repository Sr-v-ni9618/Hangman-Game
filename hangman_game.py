import random

print("WELCOME TO HANGMAN GAME")

words = ["grape","rabbit","blue","school","flower"]
word = random.choice(words)
guessed = []
attempts = 6

while attempts > 0 :
    for letter in word:
        if letter in guessed:
            print(letter,end=" ")
        else :
            print("_",end=" ")
    print()

    guess = input("guess the letter:").lower()

    if guess in guessed:
        print("you already guess this letter")

    elif guess in word:
        print("correct guess")
        guessed.append(guess)

    else:
        print("Wrong guess")
        attempts = attempts - 1
        guessed.append(guess)
    print("Attempts left:",attempts)

    win = True
    for letter in word:
        if letter not in guessed:
            win = False
    if win:
        print("Congratulations you win")
        break

if attempts == 0:
    print("GAME OVER")
    print("The correct word :",word)
print("Thanks for playing")
