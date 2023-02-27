import logging
import math

# Logging setup
logging.basicConfig(filename="calculator.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# Menu
print("Calculator Menu")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Square root")
print("6. Exit")

# Input from user
choice = int(input("Enter your choice: "))

# Addition
if choice == 1:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    sum = a + b
    print("Sum =", sum)
    logger.info("Addition: {} + {} = {}".format(a, b, sum))

# Subtraction
elif choice == 2:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    diff = a - b
    print("Difference =", diff)
    logger.info("Subtraction: {} - {} = {}".format(a, b, diff))

# Multiplication
elif choice == 3:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    product = a * b
    print("Product =", product)
    logger.info("Multiplication: {} * {} = {}".format(a, b, product))

# Division
elif choice == 4:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    if b == 0:
        print("Division by zero is not allowed.")
    else:
        div = a / b
        print("Quotient =", div)
        logger.info("Division: {} / {} = {}".format(a, b, div))

# Square root
elif choice == 5:
    a = int(input("Enter number: "))
    sqrt = math.sqrt(a)
    print("Square root =", sqrt)
    logger.info("Square root: sqrt({}) = {}".format(a, sqrt))

# Exit
elif choice == 6:
    logger.info("Exiting the calculator.")
    exit()

# Invalid choice
else:
    print("Invalid choice.")
    logger.info("Invalid choice.")