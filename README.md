
# Guessing-number-game
Guessing number game

In the python version 3.10.6 the below defined guessing number game is created.

Algorithm:

Using random.randint, the random library is loaded to produce a random number(rand_num) between 1 and 100.

Untill the user correctly guesses the number or exits the game, the guessing_number_game() function begins a loop that will run indefinitely.

The user is given the option to quit by typing "q" or entering a number between 1 and 100. The loop continues and the user is notified once more if the input is not a number or "q."

The loop is interrupted and the game is over if the user types "q."

The 'try' block tries to convert the user's input into an integer if they enter a number. The loop continues if the input cannot be transformed, and the user is once more notified.

One more guess is added to the total.

A warning noting that the user's guess was too low is shown if it is lower than the random number (rand_num).

A warning stating that the guess was excessive is presented if the user's guess is higher than the random number (rand_num).

If the user's guess matches the random number (rand_num), a message stating that the user correctly predicted the number and number of attempts is displayed, and the loop is broken.

The game is over.

Github repository link: https://github.com/Surath916/Subramanian_3123808









