def encrypt(text,s):
    result = ""
    # transverse the plain text
    for i in range(len(text)):
        char = text[i]
        # Encrypt uppercase characters in plain text
        
        if (char.isupper()):   #isupper()check is this a uppercase word
            result += chr((ord(char) + s-65) % 26 + 65)   #ord()get ASCII value
        # Encrypt lowercase characters in plain text
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result

def decrypt(text,s):
    result = ""
    # transverse the plain text
    for i in range(len(text)):
        char = text[i]
        # decrypt uppercase characters in plain text
        
        if (char.isupper()):   #isupper()check is this a uppercase word
            result += chr((ord(char) - s-65) % 26 + 65)   #ord()get ASCII value
        # decrypt lowercase characters in plain text
        else:
            result += chr((ord(char) - s - 97) % 26 + 97)
    return result


selection=int(input("Enter 1 for encrypt , Enter 2 for decrypt : "))
text = input("Enter your word : ")
s = int(input("Enter your key : "))

if(selection==1):
    print ("Cipher: " + encrypt(text,s))
else:
    print("Plain :  " + decrypt(text,s))



