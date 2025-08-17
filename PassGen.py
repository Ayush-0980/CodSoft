import random
import string

def generate_password(length):
    """
    Generates a random password containing uppercase, lowercase,
    digits, and special characters for the specified length.
    """
    # Define possible characters for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Use random.choices to get 'length' number of characters
    password = ''.join(random.choices(characters, k=length))
    return password

def main():
    # Prompt the user for desired password length
    try:
        length = int(input("Enter desired password length: "))
        if length <= 0:
            print("Length should be a positive integer.")
            return
        password = generate_password(length)
        print("Generated Password:", password)
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
