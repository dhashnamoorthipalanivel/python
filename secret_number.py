# Set a secret number (e.g., 7). Use a while loop to ask the user to guess it until they get it right.

secretNumber = int(7)
while(True):
    guess = int(input("Guess the secret number (between 1 and 10):"))
    if(secretNumber == guess):
        print("Correct.!! you guessed the secret number.!!")
        break
    else:
        print("Wrong guess.Try again.!")