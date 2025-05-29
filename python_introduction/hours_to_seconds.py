# Define the variable for hours
hours = 2  # The number of hours to convert

# Calculate the number of seconds in the given hours
# There are 60 minutes in an hour, and 60 seconds in a minute.
# So, 1 hour = 60 * 60 = 3600 seconds.
seconds = hours * 3600

# Print the result in the specified format
# Using an f-string to easily embed variables into the output string
print(f"{hours} hour(s) is {seconds} seconds.")
