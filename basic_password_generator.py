import random
import string

try:
    password_type = int(input("Choose type of password (1 - easy, 2 - medium , 3 - hard): "))
except ValueError:
    print("Please enter a number 1,2 or 3.")
    
letters = string.ascii_letters
digits = string.digits
special_characters = string.punctuation

def easy_password():
    password = []
    length = 8
    
    for x in range(length):
        random.character = random.choice(letters)
        password.append(random.character)        
    return ''.join(password)

def medium_password():
    password = []
    length = 10
    
    for x in range(length):
        random.character = random.choice(letters + digits)
        password.append(random.character)        
    return ''.join(password)

def hard_password():
    password = []
    length = 12
    
    for x in range(length):
        random.character = random.choice(letters + digits + special_characters)
        password.append(random.character)        
    return ''.join(password)

if password_type == 1:
    print(easy_password())
elif password_type == 2:
    print(medium_password())
elif password_type == 3:
    print(hard_password())
else:
    print("Please enter a number 1,2 or 3...")
