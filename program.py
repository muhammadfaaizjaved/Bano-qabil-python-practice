def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"
def get_user_input():
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))
    return x, y
def display_menu():
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter choice (1/2/3/4): ")
    return choice
def perform_calculation(choice, x, y):
    if choice == '1':
        result = add(x, y)
        operation = "Addition"
    elif choice == '2':
        result = subtract(x, y)
        operation = "Subtraction"
    elif choice == '3':
        result = multiply(x, y)
        operation = "Multiplication"
    elif choice == '4':
        result = divide(x, y)
        operation = "Division"
    else:
        result = "Invalid input"
        operation = ""

    return result, operation
def display_result(result, operation):
    if operation:
        print(f"{operation} result: {result}")
    else:
        print(result)
def main():
    choice = display_menu()
    x, y = get_user_input()
    result, operation = perform_calculation(choice, x, y)
    display_result(result, operation)

if __name__ == "__main__":
    main()
