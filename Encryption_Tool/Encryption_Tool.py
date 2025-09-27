
from ast import Or
from turtle import back, circle
from unittest import skip
from encryption_attached import*
print(logo)
import os
   
game = True
while  game  :
    
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    

 #TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.


    def encrypt (text,shift) :
        chiper_text =""
        for letter in text :


            if shift > 26 :
                shift = shift%26

            if letter in alphabet:
                shifted=alphabet.index(letter)+shift
                letter=alphabet[shifted]    
                chiper_text+=letter
            else:
                chiper_text+=letter
            
        print(chiper_text)



    def decode (text,shift) :
        chiper_text =""
        for letter in text :
             if letter in alphabet:
                shifted=alphabet.index(letter)-shift
                letter=alphabet[shifted]    
                chiper_text+=letter
             else:
                chiper_text+=letter
        print(chiper_text)


    if direction =='encode' :
        encrypt(text,shift)
    elif direction =='decode':
        decode(text,shift)

    
    if input("Do You want to Try again !:").lower() ==  "yes" :
        game = True
        print("Let's Try again ")
    else :
        game = False 
        os.system('cls')






















