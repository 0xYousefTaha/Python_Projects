#=================================Password Generators ==================================#
import random
logo= """
   ___              __    __              _     ___                          _                 
  / _ \__ _ ___ ___/ / /\ \ \___  _ __ __| |   / _ \___ _ __   ___ _ __ __ _| |_ ___  _ __ ___ 
 / /_)/ _` / __/ __\ \/  \/ / _ \| '__/ _` |  / /_\/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__/ __|
/ ___/ (_| \__ \__ \\\  /\  / (_) | | | (_| | / /_\\\  __/ | | |  __/ | | (_| | || (_) | |  \__ \\
\/    \__,_|___/___/ \/  \/ \___/|_|  \__,_| \____/\___|_| |_|\___|_|  \__,_|\__\___/|_|  |___/
                                                                                               
"""
print(logo)

letters =\
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
'l', 'm', 'n', 'o', 'p','q', 'r', 's', 't', 'u', 'v', 'w', 'x',
'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 
'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


#Randomly Choice From Existing items.

password =[]

for _ in range (nr_letters):
    password.append(random.choice(letters))
    

for _ in range(nr_symbols) :
    password.append(random.choice(symbols))

for _ in range(nr_numbers) :
    password.append(random.choice(numbers))


#====================================Second Level Random The Position of (l,s,n) =====#

number_of_password = nr_letters + nr_numbers + nr_symbols

Final_password=''

for _ in range(number_of_password) :
    Final_password+=random.choice(password)

print(f"You New Password is :\n [{Final_password}]")
































