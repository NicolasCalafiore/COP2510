# Nicolas Calafiore
# U94446501
# Program recieves 3 inputs (population, rate, days) and enters a loop. Within the loop the population adds the population*rate and then saves the new population for the next loop iteration and prints the respective day.
# if-elif-else is used for proper formatting of different day lengths

startPop = int(input("Starting number of organisms:"))
while startPop < 1:
    startPop = int(input("Starting number of organisms:"))  
popRate = int(input("Average daily increase (as a %):"))
while popRate < 1:
    popRate = int(input("Average daily increase (as a %):"))
popRate = popRate/100
days = int(input("Number of days to multiply:"))
while days < 1:
    days = int(input("Number of days to multiply:"))

currentDay = 1
currentPopulation = startPop

print('Day              Population')
print('--------------------------')

while currentDay <= days:
    if currentDay < 10:
        print(f"{currentDay}            ", end='')
    elif currentDay < 100:
        print(f"{currentDay}           ", end='')
    else:
        print(f"{currentDay}          ", end='')
        
    print("%0.6f" % currentPopulation)  # Credit https://stackoverflow.com/questions/1995615/how-can-i-format-a-decimal-to-always-show-2-decimal-places
    
    currentPopulation = currentPopulation + (currentPopulation * popRate)
    currentDay += 1

