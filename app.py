# It is printing a welcome message
print("Welcome to my Python program!")

# Acquiring input from user
hours = input("How many hours did you study today? ")

# Convert input to a number and perform the weekly calculation
hours = float(hours)
weekly_hours = hours * 7

# Display the final weekly study hour estimate
print(f"You are on track to study {weekly_hours} hours this week.")

# Start error handling to catch and manage invalid input
try:
    hours = float(hours)
except ValueError:
    print("Please enter a valid number.")
    exit()
