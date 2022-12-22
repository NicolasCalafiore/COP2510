#U94446501
#Nicolas Calafiore
#Program calls the show menu function and depending on the input refers to the respective method for each equation. The input is verified and looped if
#invalid. The program then asks for the length. Looped until valid. Main method then calls the respective method and passes the required length
#Once the sequence is calculated the sequence is returned and is printed.



userInput = ''

def showMenu():
    print('Welcome to the number sequence generator program!')
    print('Here are your choices:')
    print('1-Centered Pentagonal Sequence')
    print('2-Centered Heptagonal Sequence')
    print('3-Centered Hendecagonal Sequence')
    
def pentagonalEquation(length):
    sequence = []
    n = 1
    while n <= length:
        currentElement = ((5*n**2) - 5*n + 2)/2
        sequence.append(currentElement)
        n += 1
    return sequence

    
def heptagonalEquation(length):
    sequence = []
    n = 1
    while n <= length:
        currentElement = (7*n**2-7*n+2)/2
        sequence.append(currentElement)
        n += 1
    return sequence


def hendecagonalEquation(length):
    sequence = []
    n = 1
    while n <= length:
        currentElement = (11*n**2-11*n+2)/2
        sequence.append(currentElement)
        n += 1
    return sequence

def __mainMethod__():
    userInput = ''
    while userInput != 'no':
        showMenu()
        userInput = int(input('Enter your choice (1-3):'))
        while(userInput > 3 or userInput < 1):
            print('Invalid Entry. Re-enter your choice (1 - 3):')
            userInput = int(input())
        setLength = int(input('Enter the number of values for the list (>=3):'))
        while(setLength < 3):
            setLength = int(input('Invalid Entry. Re-enter the number of values for the list (>=3):'))
        
        if(userInput == 1):
           sequence = pentagonalEquation(setLength)
           print(f'Heres a list containing the first {setLength} numbers of the centered pentagonal sequence:', sequence)
        
        elif(userInput == 2):
           sequence = heptagonalEquation(setLength)

           print(f'Heres a list containing the first {setLength} numbers of the centered heptagonal sequence:', sequence)

        elif(userInput == 3):
           sequence = hendecagonalEquation(setLength)
           print(f'Heres a list containing the first {setLength} numbers of the centered hendecagonal sequence:', sequence)

           
        else:
            print('An Error Occured')
            
        userInput = input('Would you like to run the program again? Enter yes or no:')
        print('\n')
        userInput.lower()

    print('Thanks for using the program! Goodbye!')



__mainMethod__()






















       
        
