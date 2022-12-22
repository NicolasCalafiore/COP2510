# Nicolas Calafiore
# U94446501
# Program generates a random number 0 to 101 (exclusive)
# Continuously asks for input and will only break while-loop if guessed correctly or the guess amount goes over 10.
# The value of the guessed number influences which feedback you get (too high or too low)


import random

generatedNumber = random.randrange(101)
print(generatedNumber)
guessAmount = 1;
feedbackString = ''

number = int(input("Enter a number between 1 and 100 (inclusive):"))

while number is not generatedNumber and guessAmount is not 10:

    if number < 0 or number > 100:
        feedbackString = "Really? Enter another guess between 1 to 100:"
        
    elif number > generatedNumber:
       feedbackString = "Too high. Enter another guess:"

    elif number < generatedNumber:
        feedbackString = "Too low. Enter another guess:"

    number = int(input(feedbackString))
    
    guessAmount += 1

if guessAmount < 11:
    print(f"You guessed it right!! You got it in {guessAmount} guesses!")
else:
    print(f"Sorry, the number was {generatedNumber}")
