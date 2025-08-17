import random
import string

def generate_password(length):
    """
    Generates a random password containing uppercase letters, lowercase letters,
    digits, and special characters for the specified length.
    """
    # Define the set of characters to choose from: letters, digits, punctuation
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a password by randomly selecting characters from the pool
    password = ''.join(random.choices(characters, k=length))
    
    return password

def main():
    """
    Main function to prompt user input, generate the password, and print it.
    """
    try:
        # Prompt the user to enter the desired length of the password
        length = int(input("Enter desired password length: "))
        
        # Validate that the length is a positive integer
        if length <= 0:
            print("Length should be a positive integer.")
            return
        
        # Generate the password with the specified length
        password = generate_password(length)
        
        # Display the generated password
        print("Generated Password:", password)
    except ValueError:
        # Handle the error in case the user enters a non-integer value
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()

# Hey