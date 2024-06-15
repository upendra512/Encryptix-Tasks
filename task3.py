# PASSWORD GENERATOR
import random
import string

def generate_password(length):
    # Define the character sets using string constants
    characters = string.printable
    password=[]
    for i in range(length):
        random_char = random.choice(characters)
        password.append(random_char)

    password = ''.join(password)
    return(password)

def main():
    print("Welcome to the Password Generator")
    # Prompt user for the desired length of the password
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Please enter a positive number.")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")
    
    # Generate the password
    password1 = generate_password(length)

    # Display the generated password
    print(f"Generated Password: {password1}")

if __name__ == "__main__":
    main()

