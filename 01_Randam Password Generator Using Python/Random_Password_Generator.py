### Random Password Generator

import random
import string

characters = list(string.ascii_letters + string.digits + "!@#%$^&*()")

def random_pass():
    password_lenght = int(input("How Long would you like your password to be? "))
    random.shuffle(characters)
    password = []

    for i in range(password_lenght):
        password.append(random.choice(characters))
    random.shuffle(characters)
    password = "".join(password)
    print(password)

option = input("Do you want to generate a password? (Yes/No): ")
option = option.upper()

if option == "YES":
    random_pass()
elif option == "NO":
    print("Program Exit")
    quit()
else:
    print("Invalid input, please input Yes or No")
    quit()