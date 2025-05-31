# multiplication_table.py

def generate_multiplication_table():
    """
    Prompts the user for a number and prints its multiplication table
    from 1 to 10 using a for loop.
    """
    try:
        # Prompt the user to input a number
        number_str = input("Enter a number to see its multiplication table: ")

        # Convert the input string to an integer
        number = int(number_str)

        print(f"\nMultiplication table for {number}:")
        # Use a for loop to iterate from 1 to 10
        for i in range(1, 11):  # range(1, 11) includes 1 and goes up to (but not including) 11
            # Calculate the product
            product = number * i
            # Print each line of the multiplication table in the specified format
            print(f"{number} * {i} = {product}")

    except ValueError:
        # Handle cases where the user enters non-integer input
        print("Invalid input. Please enter a whole number.")
    except Exception as e:
        # Catch any other unexpected errors
        print(f"An unexpected error occurred: {e}")

# Run the function to generate the multiplication table
if __name__ == "__main__":
    generate_multiplication_table()
