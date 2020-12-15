
# Calling a random int in the range 1-100
import random
num = random.randint(1, 100)

# Intro printed that explains the rules (user interface)
print("WELCOME")
print("THIS IS THE GUESSING GAME CHALLENGE. THE RULES ARE AS FOLLOW:")
print("GUESS THE NUMBER BETWEEN 1 AND 100.")
print("'WARM' WILL BE DISPLAYED IF YOU ARE WITHIN 10 OF THE NUMBER. 'COLD' WILL BE DISPLAYED IF YOU ARE OUT OF BOUNDS")
print("'WARMER' WILL BE DISPLAYED EACH TIME YOUR GUESS IS CLOSER THAN THE PREVIOUS. 'COLDER' WILL BE DISPLAYED IF YOUR GUESS IS FARTHER FROM THE NUMBER THAN THE LAST GUESS")

# A list that stores the guesses. zero is the placeholder because it evaluates "False"
guesses = [0]

# A while loop that asks for the player to make a guess at the begining and displays out of bounds if so
while True:
    guess = int(input('I am thinking of a number 1-100. Take a guess! >>> '))

    if guess < 1 or guess > 100:
        print('OUT OF BOUNDS! sorry, try again: ')
        continue
    break


while True:
    guess = int(input('I am thinking of a number 1-100. Take a guess'))

    if guess < 1 or guess > 100:
        print("OUT OF BOUNDS, sorry please guess again:  ")
        continue

   # here we compare the player's guess to our number
    if guess == num:
        print(
            f'congrats you guessed the correct number in only {len(guesses)} guesses!!')
        break
    # append guess to the list of guesses if incorrect
    guesses.append(guess)
    if guesses[-2]:
        if abs(num-guess) < abs(num-guesses[-2]):
            print("WARMER!")
        else:
            print("COLDER!")

    else:
        if abs(num-guess) <= 10:
            print("WARM!")
        else:
            print("COLD!")
