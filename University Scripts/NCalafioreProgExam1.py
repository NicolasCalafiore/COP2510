## Nicolas Calafiore
## U94446501

## Asks for input to assign to the temperature variable. Loops until valid
## Asks for input to assign to the humidity variable. Loops until valid
## Creates a variable that represents the heat index. Variable is equal to equation given using the constants given and variables inputted.
## Prints the heat index and utilizes 4 if statments to determine which line to print respective of the heat index



temperature = int(input("Enter the temperature (between 80F and 112F inclusive:"))
while temperature < 80 or temperature > 112:
    temperature = int(input("Invalid Entry: Enter the temperature (between 80F and 112F inclusive):"))
humidity = int(input("Enter the humidity as a percentage (between 40 to 100 inclusive):"))
while humidity < 40 or humidity > 100:
    humidity = int(input("Invalid Entry: Enter the humidity as a percentage (between 40 to 100 inclusive):"))
    
heatIndex = float((-42.379) + (2.04901523 * temperature) + (10.14333127 * humidity) + (-0.22475541*temperature*humidity) + ((-6.83783 * 10**-3)*temperature**2) + ((-5.481717 * 10**-2)*humidity**2) + ((1.22874 * 10**-3)*(temperature**2)*humidity) + ((8.5282 * 10**-4)*temperature*humidity**2) + (-1.99 * 10**-6)*(temperature**2)*humidity**2)
print("The 'feels like temperature is", round(heatIndex, 1), "F")

if(heatIndex >= 80 and heatIndex < 90):
    print("Caution: fatigue is possible with prolonged exposure and activity.", end='')
    print(" Continuing activity could result in heat cramps")
    
if(heatIndex >= 90 and heatIndex < 105):
    print("Extreme caution: heat cramps and heat exhaustion are possible.", end='')
    print(" Continuing activity could result in heat stroke")

if(heatIndex >= 105 and heatIndex < 130):
    print("Danger: heat cramps and heat exhaustion are likely; heat stroke is probable with continued activity", end='')
    print(" probable with continued activity")

if(heatIndex >= 130):
    print("Extreme danger: heat stroke is imminent")
