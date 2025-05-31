# match_case_calculator.py

def run_calculator():
    """
    Prompts the user for two numbers and an operation, then performs
    the calculation using a match-case statement and displays the result.
    """
    try:
        # Prompt for the first number and convert it to a float
        num1 = float(input("Enter the first number: "))

        # Prompt for the second number and convert it to a float
        num2 = float(input("Enter the second number: "))

        # Prompt for the desired operation
        operation = input("Choose the operation (+, -, *, /): ")

        result = None  # Initialize result to None

        # Use a match-case statement to perform the selected operation
        match operation:
            case '+':
                result = num1 + num2
                print(f"The result is {result}.")
            case '-':
                result = num1 - num2
                print(f"The result is {result}.")
            case '*':
                result = num1 * num2
                print(f"The result is {result}.")
            case '/':
                # Handle division by zero case
                if num2 == 0:
                    print("Cannot divide by zero.")
                else:
                    result = num1 / num2
                    print(f"The result is {result}.")
            case _:
                # Handle invalid operation input
                print("Invalid operation. Please choose from +, -, *, /.")

    except ValueError:
        # Handle cases where the user enters non-numeric input for numbers
        print("Invalid input. Please enter valid numbers.")
    except Exception as e:
        # Catch any other unexpected errors
        print(f"An unexpected error occurred: {e}")

# Run the calculator program
if __name__ == "__main__":
    run_calculator()
