# TDEE Calculator

def calculate_tdee(gender, age, weight, height, activity_level):
    # Convert weight from pounds to kilograms
    weight = weight / 2.205

    # Convert height from inches to meters
    height = height / 39.37

    if gender == "male":
        bmr = 88.362 + (13.397 * weight) + (4.799 * height * 100) - (5.677 * age)
    elif gender == "female":
        bmr = 447.593 + (9.247 * weight) + (3.098 * height * 100) - (4.330 * age)

    if activity_level == "sedentary":
        tdee = bmr * 1.2
    elif activity_level == "lightly active":
        tdee = bmr * 1.375
    elif activity_level == "moderately active":
        tdee = bmr * 1.55
    elif activity_level == "very active":
        tdee = bmr * 1.725
    elif activity_level == "extra active":
        tdee = bmr * 1.9

    return tdee

print("Welcome to the TDEE calculator!")

# Prompt user for gender
while True:
    gender = input("Please enter your gender (M/F): ").upper()
    if gender not in ["M", "F"]:
        print("Error: Invalid input. Please enter either M or F.")
    else:
        break

# Prompt user for age
while True:
    try:
        age = int(input("Please enter your age: "))
        if age <= 0 or age > 150:
            print("Error: Invalid age. Please enter a valid age between 1 and 150.")
        else:
            break
    except ValueError:
        print("Error: Invalid input. Please enter a valid age.")

# Prompt user for weight
while True:
    try:
        weight = float(input("Please enter your weight in pounds: "))
        if weight <= 0 or weight > 1500:
            print("Error: Invalid weight. Please enter a valid weight between 1 and 1500 pounds.")
        else:
            break
    except ValueError:
        print("Error: Invalid input. Please enter a valid weight.")

# Prompt user for height
while True:
    try:
        height_in = int(input("Please enter your height in inches: "))
        if height_in <= 0 or height_in > 120:
            print("Error: Invalid height. Please enter a valid height between 1 and 120 inches.")
        else:
            # Convert height from inches to centimeters
            height_cm = height_in * 2.54
            break
    except ValueError:
        print("Error: Invalid input. Please enter a valid height in inches.")

# Prompt user for activity level
while True:
    print("\nPlease select your activity level:")
    print("1. Sedentary (little or no exercise)")
    print("2. Lightly active (light exercise/sports 1-3 days a week)")
    print("3. Moderately active (moderate exercise/sports 3-5 days a week)")
    print("4. Very active (hard exercise/sports 6-7 days a week)")
