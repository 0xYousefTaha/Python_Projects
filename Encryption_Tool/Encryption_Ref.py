#Refactoring Encrypption Game 

from Encryption_Tool import*
from unittest import skip

print(logo)

while True :

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))


    def encode_and_decode (direction,text,shift) :
        chiper_text =""
        if shift >26 :
            shift = shift%26

        if direction =='encode':
            for letter in text :
                if letter in alphabet :
                    shifted=alphabet.index(letter)+shift
                    letter=alphabet[shifted]    
                
                chiper_text+=letter
            print(chiper_text)

        elif direction =='decode':
            for letter in text :
                if letter in alphabet :
                    shifted=alphabet.index(letter)-shift
                    letter=alphabet[shifted]    
                chiper_text+=letter
            print(chiper_text)

        else :
            print("invalid Value!!❌")

    encode_and_decode(direction,text,shift)

    Condition = input("Do You Want to Play Again? : Yes Or No\n").lower()
    if Condition == 'yes':
        skip 
    else :
        break





























