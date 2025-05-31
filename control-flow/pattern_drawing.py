# pattern_drawing.py

def draw_square_pattern():
    """
    Prompts the user for a positive integer size and draws a square pattern
    of asterisks using nested loops.
    """
    while True:
        try:
            # Prompt user for the pattern size
            size_str = input("Enter the size of the pattern: ")
            size = int(size_str)

            # Validate if the input is a positive integer
            if size <= 0:
                print("Please enter a positive integer for the pattern size.")
                continue # Ask for input again

            break # Exit the loop if input is valid
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    print("\nHere is your pattern:")

    # Use a while loop to iterate through each row of the pattern
    row_count = 0
    while row_count < size:
        # Inside the while loop, use a for loop to print asterisks for the current row
        for _ in range(size): # The '_' is used as a placeholder variable when you don't need to use the loop counter itself
            print("*", end="") # Print asterisk without advancing to a new line

        # After completing each row (inner for loop finishes), print a newline character
        print()

        # Increment the row counter for the while loop
        row_count += 1

# Run the pattern drawing function
if __name__ == "__main__":
    draw_square_pattern()
