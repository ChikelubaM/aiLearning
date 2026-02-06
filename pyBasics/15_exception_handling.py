# 1. Write a Python program that takes a numeric grade from the user (between 0 and 100), and prints the corresponding letter grade:
# 90–100 → A
# 80–89  → B
# 70–79  → C
# 60–69  → D
# <60    → F

# 2. Your program should handle the following exceptions:
# If the user enters a non-numeric value, catch the ValueError and display a user-friendly message.
# If the user enters a number outside the valid range (0 to 100), raise a ValueError yourself with a custom message.

# 3. Use the try–except–else–finally structure:
#
# try: Attempt to parse the input and compute the letter grade.
# except: Handle conversion errors and invalid ranges.
# else: Print the final grade if everything was successful.
# finally: Print a goodbye message like "Thank you for using the Grade Calculator. Goodbye!" no matter what.


# SOLUTION

# STEP 1: Input
user_input = input("Enter your grade: ")

try:
    grade = float(user_input)

    # STEP 2: The guard clause
    if grade < 0 or grade > 100:
        raise ValueError("Grade must be between 0 and 100")
    # STEP 3: The Waterfall Logic
except ValueError:
    print("Invalid input. Enter a numeric value")

else:
    if grade >= 90:
        print(f"Your grade: {grade} is A")
    elif grade >= 80:
        print(f"Your grade:  {grade} is B")
    elif grade >= 70:
        print(f"Your grade:  {grade} is C")
    elif grade >= 60:
        print(f"Your grade:  {grade} is D")
    else :
        print(f"Your grade:  {grade} is F")
# STEP 4: The Safety Net (For none numeric input)
finally:
    print("Thank you for using the Grade Calculator. Goodbye!")



