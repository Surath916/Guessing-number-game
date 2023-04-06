# Guess the number game
#importing random library
import random

def guessing_number_game():
# generating random number between 1 to 100
    rand_num = random.randint(1, 100)
    num_of_guesses = 0
#ask the user to enter a number or q to quit
    while True:
        guess = input("Guess a number between 1 and 100, or 'q' to quit: ")
# check if user entered q
        if guess == 'q':
            print("You gave up. The number was", rand_num)
            break
#convert the guessed number to integer
        try:
            guess = int(guess)
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 100, 'q' to quit.")
            continue
#increment of the guess counter
        num_of_guesses += 1
#check if the guess is correct
        if guess < rand_num:
            print("Too low.")
        elif guess > rand_num:
            print("Too high.")
        else:
            print("You guessed it in", num_of_guesses, "guesses.")
            break

guessing_number_game()






