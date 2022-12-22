## Nicolas Calafiore
## U94446501
##
## Assigned 3 variables the base unit of each ingrediant for one cookie
## Accepted 1 input determining the amount of cookies to be made
## multiplied each base ingrediant for 1 cookie by the input
## rounded and printed.


oneSugar = float(.03125); ## Necessary amount to make 1 cookie
oneButter = float(1/48);
oneFlour = float(2.75/48);

cookieAmount = int(input("Enter Amount of Cookies: "))

print("\nRecipe for ", cookieAmount, " cookie(s): ")
print(round(oneSugar * cookieAmount,2), " cup(s) of sugar")
print(round(oneButter * cookieAmount,2), " cup(s) of butter")
print(round(oneFlour * cookieAmount,2), " cup(s) of flour")
