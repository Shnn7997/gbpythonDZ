import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def complex_add(x, y):
    return x + y

def complex_subtract(x, y):
    return x - y

def complex_multiply(x, y):
    return x * y

def complex_divide(x, y):
    return x / y

def rational_add(x, y):
    return x + y

def rational_subtract(x, y):
    return x - y

def rational_multiply(x, y):
    return x * y

def rational_divide(x, y):
    return x / y

def main():
    while True:
        logger.info("Select operation:")
        logger.info("1.Add")
        logger.info("2.Subtract")
        logger.info("3.Multiply")
        logger.info("4.Divide")
        logger.info("5.Complex Add")
        logger.info("6.Complex Subtract")
        logger.info("7.Complex Multiply")
        logger.info("8.Complex Divide")
        logger.info("9.Rational Add")
        logger.info("10.Rational Subtract")
        logger.info("11.Rational Multiply")
        logger.info("12.Rational Divide")
        logger.info("13.Quit")

        choice = input("Enter choice(1/2/3/4/5/6/7/8/9/10/11/12/13):")

        if choice == '1':
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            logger.info("Result: {}".format(add(num1, num2)))

        elif choice == '2':
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            logger.info("Result: {}".format(subtract(num1, num2)))

        elif choice == '3':
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            logger.info("Result: {}".format(multiply(num1, num2)))

        elif choice == '4':
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            logger.info("Result: {}".format(divide(num1, num2)))

        elif choice == '5':
            num1 = complex(input("Enter first number: "))
            num2 = complex(input("Enter second number: "))
            logger.info("Result: {}".format(complex_add(num1, num2)))

        elif choice == '6':
            num1 = complex(input("Enter first number: "))
            num2 = complex(input("Enter second number: "))
            logger.info("Result: {}".format(complex_subtract(num1, num2)))

        elif choice == '7':
            num1 = complex(input("Enter first number: "))
            num2 = complex(input("Enter second number: "))
            logger.info("Result: {}".format(complex_multiply(num1, num2)))

        elif choice == '8':
            num1 = complex(input("Enter first number: "))
            num2 = complex(input("Enter second number: "))
            logger.info("Result: {}".format(complex_divide(num1, num2)))

        elif choice == '9':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            logger.info("Result: {}".format(rational_add(num1, num2)))

        elif choice == '10':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            logger.info("Result: {}".format(rational_subtract(num1, num2)))

        elif choice == '11':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            logger.info("Result: {}".format(rational_multiply(num1, num2)))

        elif choice == '12':
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            logger.info("Result: {}".format(rational_divide(num1, num2)))

        elif choice == '13':
            logger.info("Exiting...")
            break

        else:
            logger.info("Invalid input")

if __name__ == "__main__":
    main()