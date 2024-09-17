import random
import string

def create_password(size, include_specials=True,include_uppercase=True,include_digits=True):
    if size <= 0:
        return "Error: Size must be greater than 0."

    char_set=''
    if include_uppercase:
        char_set+=string.ascii_uppercase
    if include_specials:
        char_set+=string.punctuation
    if include_digits:
        char_set+=string.digits
    char_set +=string.ascii_lowercase

    if not char_set:
        return "Error: No characters available for password generation."
    password=''.join(random.choice(char_set) for _ in range(size))
    return password

def main():
    print("Welcome to the Enhanced Password Generator!")
    
    while True:
        try:
            size=int(input("Specify the desired length of the password: "))
            if size <=0:
                print("Error: Length must be a positive integer. Please try again.")
                continue

            specials=input("Include special characters (yes/no)? ").strip().lower()
            if specials not in ('yes','no'):
                print("Error: Invalid response. Please enter 'yes'or'no'.")
                continue
            include_specials=specials=='yes'
            uppercase=input("Include uppercase letters (yes/no)? ").strip().lower()
            if uppercase not in ('yes','no'):
                print("Error: Invalid response. Please enter'yes'or'no'.")
                continue
            include_uppercase=uppercase =='yes'
            digits = input("Include digits (yes/no)? ").strip().lower()
            if digits not in('yes','no'):
                print("Error: Invalid response. Please enter 'yes'or'no'.")
                continue
            include_digits=digits=='yes'
            pwd=create_password(size, include_specials,include_uppercase,include_digits)
            print(f"Generated Password:{pwd}")
            retry=input("Would you like to generate another password? (yes/no): ").strip().lower()
            if retry!='yes':
                print("Thank you for using the Enhanced Password Generator. Goodbye!")
                break
        
        except ValueError:
            print("Error: Invalid input. Please enter a valid number for the length.")

if __name__=="__main__":
    main()
