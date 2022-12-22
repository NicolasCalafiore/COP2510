# U94446501
# Nicolas Calafiore

# User is prompted to give an input file name and output file name
# File is read using the input given. All contents of the file are copied and assigned to one variable
# That variable is then split into an Array with each element containing one letter
# Each element of that array is then processed through a for-loop. Each element is compared to the dictionary, changed to its appropriated key, and then added to
# a new arraylist. Once all of the elements have been processed the newly created arraylist is then processed through another for-loop which concenates each element
# back into a string. Once finished the string is then pasted to the output file.

Encrypt_Code =  {'A':')','a':'0','B':'(','b':'9','C':'*','c':'8',
        'D':'&','d':'7','E':'^','e':'6','F':'%','f':'5',
        'G':'$','g':'4','H':'#','h':'3','I':'@','i':'2',
        'J':'!','j':'1','K':'Z','k':'z','L':'Y','l':'y',
        'M':'X','m':'x','N':'W','n':'w','O':'V','o':'v',
        'P':'U','p':'u','Q':'T','q':'t','R':'S','r':'s',
        'S':'R','s':'r','T':'Q','t':'q','U':'P','u':'p',
        'V':'O','v':'o','W':'N','w':'n','X':'M','x':'m',
        'Y':'L','y':'l','Z':'K','z':'k','!':'J','1':'j',
        '@':'I','2':'i','#':'H','3':'h','$':'G','4':'g',
        '%':'F','5':'f','^':'E','6':'e','&':'D','7':'d',
        '*':'C','8':'c','(':'B','9':'b',')':'A','0':'a',
        ':':',',',':':','?':'.','.':'?','<':'>','>':'<',
        "'":'"','"':"'",'+':'-','-':'+','=':';',';':'=',
        '{':'[','[':'{','}':']',']':'}', ' ' : ' '}

def encrypt(string):
        characters = []
        encryptedCharacters = []

        for letter in lines:
                characters.append(letter)

        for element in characters:
                replacement = Encrypt_Code.get(element)
                encryptedCharacters.append(replacement)
        print(encryptedCharacters)

        allContent = ''
        for element in encryptedCharacters:
                if (str(element) != 'None'):
                        allContent = allContent + str(element)
                else:
                        allContent = allContent + "\n"

        return allContent





inFileName = str(input("Enter the name of your input file"))
outFileName = str(input("Enter the name of your output file"))

outputContent = ''

lines = ''
with open(inFileName + '.txt') as f:
    lines = f.read()

    EncryptedContent = encrypt(lines)

f = open(outFileName + ".txt", "a")
f.write(str(EncryptedContent))
f.close()



