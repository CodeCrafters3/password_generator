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
        
password_length = get_password_length()
all_characters = string.ascii_letters + string.digits + string.punctuation
password = []

for index in range(password_length):
    selected_characters = random.choice(all_characters)
    password.append(selected_characters)

generated_password = "".join(password)
print(f"Your password: \n {generated_password}")
