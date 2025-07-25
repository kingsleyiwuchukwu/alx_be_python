# This script will ask the user for a single task, its priority level, and if it is time-sensitive.
# The program will then provide a customized reminder for that task, demonstrating control flow and loops without relying on data structures to store multiple tasks.


# # Prompt the user for task details
# task = input("Enter your task: ")
# priority = input("Priority (high/medium/low): ").lower()
# time_bound = input("Is it time-bound? (yes/no): ").lower()

# # Process the task based on priority using match case
# match priority:
#     case 'high':
#         reminder = f"Reminder: '{task}' is a {priority} priority task."
#     case 'medium':
#         reminder = f"Reminder: '{task}' is a {priority} priority task."
#     case 'low':
#         reminder = f"Reminder: '{task}' is a {priority} priority task."
#     case _:
#         reminder = f"Reminder: '{task}' has an unknown priority level."

# daily_reminder.py

# Prompt the user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process and print the reminder directly
match priority:
    case 'high' | 'medium' | 'low':
        if time_bound == 'yes':
            print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
        elif time_bound == 'no' and priority == 'low':
            print(f"Reminder: '{task}' is a low priority task. Consider completing it when you have free time.")
        else:
            print(f"Reminder: '{task}' is a {priority} priority task.")
    case _:
        print(f"Reminder: '{task}' has an unknown priority level.")


# # Check time sensitivity
# if time_bound == 'yes':
#     reminder += " that requires immediate attention today!"
# elif time_bound == 'no' and priority == 'low':
#     reminder += " Consider completing it when you have free time."

# # Print the final reminder
# print(reminder)
