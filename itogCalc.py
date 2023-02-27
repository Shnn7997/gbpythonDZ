import logging

# Set logging
logging.basicConfig(filename='calculator.log', level=logging.INFO)

# Create menu
def menu():
    print("1. Add two rational numbers")
    print("2. Subtract two rational numbers")
    print("3. Multiply two rational numbers")
    print("4. Divide two rational numbers")
    print("5. Add two complex numbers")
    print("6. Subtract two complex numbers")
    print("7. Multiply two complex numbers")
    print("8. Divide two complex numbers")
    print("9. Quit")

# Add two rational numbers
def add_rational_numbers(num1, num2):
    logging.info("Add two rational numbers: {} + {}".format(num1, num2))
    return num1 + num2

# Subtract two rational numbers
def subtract_rational_numbers(num1, num2):
    logging.info("Subtract two rational numbers: {} - {}".format(num1, num2))
    return num1 - num2

# Multiply two rational numbers
def multiply_rational_numbers(num1, num2):
    logging.info("Multiply two rational numbers: {} * {}".format(num1, num2))
    return num1 * num2

# Divide two rational numbers
def divide_rational_numbers(num1, num2):
    logging.info("Divide two rational numbers: {} / {}".format(num1, num2))
    return num1 / num2

# Add two complex numbers
def add_complex_numbers(num1, num2):
    logging.info("Add two complex numbers: {} + {}".format(num1, num2))
    return num1 + num2

# Subtract two complex numbers
def subtract_complex_numbers(num1, num2):
    logging.info("Subtract two complex numbers: {} - {}".format(num1, num2))
    return num1 - num2

# Multiply two complex numbers
def multiply_complex_numbers(num1, num2):
    logging.info("Multiply two complex numbers: {} * {}".format(num1, num2))
    return num1 * num2

# Divide two complex numbers
def divide_complex_numbers(num1, num2):
    logging.info("Divide two complex numbers: {} / {}".format(num1, num2))
    return num1 / num2

# Quit
def quit():
    logging.info("Quit")
    exit()

# Main
if __name__ == "__main__":
    menu()
    choice = input("Enter your choice: ")
    if choice == '1':
        num1 = int(input("Enter first rational number: "))
        num2 = int(input("Enter second rational number: "))
        print(add_rational_numbers(num1, num2))
    elif choice == '2':
        num1 = int(input("Enter first rational number: "))
        num2 = int(input("Enter second rational number: "))
        print(subtract_rational_numbers(num1, num2))
    elif choice == '3':
        num1 = int(input("Enter first rational number: "))
        num2 = int(input("Enter second rational number: "))
        print(multiply_rational_numbers(num1, num2))
    elif choice == '4':
        num1 = int(input("Enter first rational number: "))
        num2 = int(input("Enter second rational number: "))
        print(divide_rational_numbers(num1, num2))
    elif choice == '5':
        num1 = complex(input("Enter first complex number: "))
        num2 = complex(input("Enter second complex number: "))
        print(add_complex_numbers(num1, num2))
    elif choice == '6':
        num1 = complex(input("Enter first complex number: "))
        num2 = complex(input("Enter second complex number: "))
        print(subtract_complex_numbers(num1, num2))
    elif choice == '7':
        num1 = complex(input("Enter first complex number: "))
        num2 = complex(input("Enter second complex number: "))
        print(multiply_complex_numbers(num1, num2))
    elif choice == '8':
        num1 = complex(input("Enter first complex number: "))
        num2 = complex(input("Enter second complex number: "))
        print(divide_complex_numbers(num1, num2))
    elif choice == '9':
        quit()
    else:
        print("Invalid Input")