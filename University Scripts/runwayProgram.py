## Nicolas Calafiore
## U94446501

## Accepts 2 variable inputs
## Applies those 2 variables to the required equation and sets it equal to final variable minimumRunwayLength
## Prints

planeAcceleration = float(input("Enter Acceleration (m/s)^2: "));
planeSpeed = float(input("Speed Amount (m/s): "));

minimumRunwayLength = (planeAcceleration*planeAcceleration) /(2*planeSpeed)

print("Minimum Runway Length: ", round(minimumRunwayLength,4))
