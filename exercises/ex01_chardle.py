"""EX01 -Chardle - A cute step toward Wordle."""
__author__ = "730522786"

word: str = input("Enter a 5-character word: ")
if len(word) < 5:
    print("Error: Word must contain 5 characters")
    exit()
if len(word) > 5:
    print("Error: Word must contain 5 characters")
    exit()
guess: str = input("Enter a single character: ")
if len(guess) != 1:
    print("Error: Character must be a single character.")
    quit()
count: int = 0
print("Searching for " + guess + " in " + word)
if guess == word[0]:
    print(guess + " found at index 0")
    count = (count + 1)
if guess == word[1]:
    print(guess + " found at index 1")
    count = (count + 1)
if guess == word[2]:
    print(guess + " found at index 2")
    count = (count + 1)
if guess == word[3]:
    print(guess + " found at index 3")
    count = (count + 1)
if guess == word[4]:
    print(guess + " found at index 4")
    count = (count + 1)
if count == 1:
    print(str(count) + " instance of " + guess + " found in " + word)
if count > 1:
    print(str(count) + " instances of " + guess + " found in " + word)
if count == 0:
    print("No instances of " + guess + " in " + word)
