#Author:Brijith
import random
print("WELCOME TO HANGMAN !")
num 0
words = ["hacker","bounty","random"]
secret_word = random.choice(words)
display_word = []
for letter in secret_word:
    display_word += "_"
print(display_word)

game_over = False
while not game_over:
    guess = input("Guess a letter:").lower()
    for position in range(len(secret_word)):
        letter = secret_word[position]
        if letter == guess:
            display_word[position] = letter
    if guess not in secret_word:
        num +=1
        gusses_left = 5 - num
        print(f"You have {gusses_left} gusses left !")
        if num >= 5:
            print("You Lose !")
            game_over = True
    print(display_word)

    if "_" not in display_word:
        print("You Win !")
        game_over = True
