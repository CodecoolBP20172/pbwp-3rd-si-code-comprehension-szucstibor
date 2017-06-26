# It's a guessing game.
import random  # Importing the random module

guessesTaken = 0  # Assign 0 to the guessesTaken variable

print('Hello! What is your name?')  # Asking the user for their name
myName = input()  # The program waits for user input

number = random.randint(1, 20)  # Assign the number variable to a random integer between 1 and 20
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')  # Printing the user's name and a string

while guessesTaken < 6:  # Looping the code below until guessesTaken is lower than 6
    print('Take a guess.')  # Prints for the user to take a guess
    guess = input()  # Waits for user input
    guess = int(guess)  # Converting the user input into an integer

    guessesTaken += 1  # Adding one to the guessesTaken

    if guess < number:  # Checks wether the number is lower than the random integer
        print('Your guess is too low.')  # It tells the user that the number is too low

    if guess > number:  # Checks wether the number is higher than the random integer
        print('Your guess is too high.')  # It tells the user that the number is too high

    if guess == number:  # Checks wether the number is equals to the random integer
        break  # If it returns true it breaks the loop

if guess == number:  # Checks wether the number is equals to the random integer
    guessesTaken = str(guessesTaken)  # If it returns true it converts the integer to a string
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')  # Congratulates the user
# And printing the number of guesses
if guess != number:  # Checks the number. It returns true if they aren't equal
    number = str(number)  # It converts the random integer into a string
    print('Nope. The number I was thinking of was ' + number)  # Tells the user what the random integer was
