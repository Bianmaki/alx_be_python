# daily_reminder.py

def daily_reminder():
    """
    Prompts the user for a single task, its priority, and time sensitivity,
    then provides a customized reminder using conditional statements and match-case.
    """
    # 1. Prompt for User Input
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower() # Convert to lowercase for consistent matching
    time_bound_input = input("Is it time-bound? (yes/no): ").lower() # Convert to lowercase for consistent checking

    # Initialize the base reminder message
    reminder_message = ""
    
    # 2. Process the Task Based on Priority using Match Case
    match priority:
        case "high":
            reminder_message = f"Reminder: '{task}' is a high priority task"
        case "medium":
            reminder_message = f"Note: '{task}' is a medium priority task"
        case "low":
            reminder_message = f"Note: '{task}' is a low priority task"
        case _:
            # Handle invalid priority input
            print("Invalid priority level entered. Please choose 'high', 'medium', or 'low'.")
            return # Exit the function if priority is invalid

    # 3. Modify the reminder based on time sensitivity using an if statement
    if time_bound_input == "yes":
        # Add the immediate attention phrase for time-bound tasks
        reminder_message += " that requires immediate attention today!"
    elif time_bound_input == "no":
        # For non-time-bound low priority tasks, add a specific suggestion
        if priority == "low":
            reminder_message += ". Consider completing it when you have free time."
        else:
            # For non-time-bound high/medium tasks, just a general completion note
            reminder_message += ". You can plan to complete it today."
    else:
        # Handle invalid time-bound input
        print("Invalid input for time-bound. Please answer 'yes' or 'no'.")
        return # Exit the function if time-bound input is invalid

    # 4. Provide a Customized Reminder
    print(reminder_message)

# Run the daily reminder script
if __name__ == "__main__":
    daily_reminder()
