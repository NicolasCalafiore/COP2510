# U94446501
# Nicolas Calafiore
# A dictionary was created containing all of the captials. A random element is returned including the state name and capital. Both are assigned to their respective
# variable. The question is then asked referencing the state variable and the input is compared to the capital variable. All are set to lowercase. For each incorrect
# match the integer variable 'wrong' is incremented by 1 else the integer variable 'correct' is incremented by 1

import random
from random import randrange

Capitals = {
    "Alabama": "Montgomery",
    "Alaska": "Juneau", "Arizona":
    "Phoenix", "Arkansas":
    "Little Rock",
    "California": "Sacramento",
    "Colorado": "Denver",
    "Connecticut": "Hartford",
    "Delaware": "Dover",
    "Florida": "Tallahassee",
    "Georgia": "Atlanta",
    "Hawaii": "Honolulu",
    "Idaho": "Boise",
    "Illinois": "Springfield",
    "Indiana": "Indianapolis",
    "Iowa": "Des Moines",
    "Kansas": "Topeka",
    "Kentucky": "Frankfort",
    "Louisiana": "Baton Rogue",
    "Maine": "Augusta",
    "Maryland": "Annapolis",
    "Massachusetts": "Boston",
    "Michigan": "Lansing",
     "Minnesota": "Saint Paul",
     "Mississippi": "Jackson",
     "Missouri": "Jefferson City",
     "Montana": "Helena",
     "Nebraska": "Lincoln",
     "Nevada": "Carson City",
     "New Hampshire": "Concord",
     "New Jersey": "Trenton",
     "New Mexico": "Santa Fe",
     "New York": "Albany",
     "North Carolina": "Raleigh",
     "North Dakota": "Bismarck",
     "Ohio": "Columbus",
     "Oklahoma": "Oklahoma City",
     "Oregon": "Salem",
     "Pennsylvania": "Harrisburg",
     "Rhode Island": "Providence",
     "South Carolina": "Columbia",
     "South Dakota": "Pierre",
     "Tennessee": "Nashville",
     "Texas": "Austin",
     "Utah": "Salt Lake City",
     "Vermont": "Montpelier",
     "Virginia": "Richmond",
     "Washington": "Olympia",
     "West Virginia": "Charleston",
     "Wisconsin": "Madison",
     "Wyoming": "Cheyenne",
}

Input = ''
wrong = 0
correct = 0
while Input.lower() != 'q':

    state, capital = random.choice(list(Capitals.items()))  ## Credit https://stackoverflow.com/questions/4859292/how-to-get-a-random-value-from-dictionary
    Input = str(input("What is the capital of " + state + "? (or enter q to quit)"))
    if(Input.lower() != str(capital).lower()):
        wrong += 1
        print("That is incorrect")
    else:
        correct += 1
        print("That is correct")

print("You had", correct, "correct responses and", wrong, "incorrect responses. ")


