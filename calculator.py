def sum_value(q,w):
    return q+w

def sub_value(q,w):
    return q-w

def mult_value(q,w):
    return q*w

def div_value(q,w):
    if w!= 0:
        return q/w
    else:
        return "Error: Cannot divide by zero."

def get_number_input(prompt_message):
    while True:
        try:
            return float(input(prompt_message))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def simple_calculator():
    print("Welcome to the Basic Calculator!")
    print("Choose an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        operation=input("Select an operation (1/2/3/4): ")

        if operation in ('1','2','3','4'):
            first_number = get_number_input("Enter the first number: ")
            second_number = get_number_input("Enter the second number: ")

            if operation=='1':
                result=sum_value(first_number,second_number)
                print(f"Result:{result}")
            elif operation=='2':
                result =sub_value(first_number,second_number)
                print(f"Result:{result}")
            elif operation=='3':
                result = mult_value(first_number,second_number)
                print(f"Result:{result}")
            elif operation =='4':
                result=div_value(first_number,second_number)
                print(f"Result:{result}")
            
            continue_calculating=input("Would you like to perform another calculation? (yes/no): ").strip().lower()
            if continue_calculating!='yes':
                print("Thank you for using the calculator. Goodbye!")
                break
        else:
            print("Invalid operation. Please select a valid option.")

if __name__=="__main__":
    simple_calculator()
