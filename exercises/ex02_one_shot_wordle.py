"""One shot."""

__author__: str = "730522786"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

secret_word: str = "python"
guess: str = input(f"What is you {len(secret_word)} guess?: ")

while len(guess) != len(secret_word):
    guess: str = input(f"That was not {len(secret_word)} letters! Try again: ")

box: str = ""
guess_chr: int = 0
guessed_chr_present = False
alt_indices: int = 0
while guess_chr < len(secret_word):
    if guess[guess_chr] == secret_word[guess_chr]:
        box = box + GREEN_BOX
    else:
        while alt_indices < len(secret_word) and guessed_chr_present is False:
            if guess[guess_chr] == secret_word[alt_indices]:
                guessed_chr_present = True
            alt_indices = alt_indices + 1
        if guessed_chr_present is True:
            box = box + YELLOW_BOX
        else:
            box = box + WHITE_BOX
    guessed_chr_present = False
    alt_indices = 0
    guess_chr = guess_chr + 1

print(box)

if len(guess) == len(secret_word):

    if guess == secret_word:
        print("Woo! You got it!")
        quit()
    if guess != secret_word:
        print("Not quite. Play again soon!")
    