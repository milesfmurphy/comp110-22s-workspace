"""An example of conditional (if-else) statements."""

SECRET: int = 3

print("I'm thinking of a number between 1-5, what is it?")
guess: int = int(input("What is your guess? "))
 
if guess == SECRET:
    print("W spam")
    print("Have a day")
else:
    print("You suck lololololol ratio div 10 noob")
    if guess > SECRET:
        print("Too high")
    else:
        print("Too low")

print("Game over.")