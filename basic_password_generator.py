import random
import string

def get_password_length():
    while True:
        try:
            length = int(input("Choose length of password:")) 
            if length > 0:
                return length
            else:
                print("Length must be a positive integer.")
        except ValueError:
            print("Please enter a valid integer.")

def generate_password(length):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = []
    
    for index in range(length):
        selected_character = random.choice(all_characters)
        password.append(selected_character)
        
    return "".join(password)

password_length = get_password_length()
generated_password = generate_password(password_length)

print(f"Your password: \n {generated_password}")