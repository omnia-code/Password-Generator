##========Password Generator========##
#1 generate a random password 
#2 enter your choice 
#3 exit


import random 
import string

while True:
    print("========Password Generator========")
    print("1. Generate a random password")
    print("2. Exit")
    
    choice = input("Enter your choice (1/2): ")
    
    if choice == '1':
       include_special = input("include special characters? (y/n): ").lower() == 'y'
       include_numbers = input("include numbers? (y/n): ").lower() == 'y'
       include_uppercase = input("include uppercase letters? (y/n): ").lower() == 'y'
       include_lowercase = input("include lowercase letters? (y/n): ").lower() == 'y'
       length = int(input("Enter the length of the password: "))
       if include_special:
           characters = string.ascii_letters + string.digits + string.punctuation
       else:
           characters = string.ascii_letters + string.digits
       password = ''.join(random.choice(characters) for i in range(length))
       print(f"Generated Password: {password}")
        
    elif choice == '2':
        print("goodbye!")
        break
        
    else:
        print("Invalid choice. Please try again.")