
"""
This function calculates TDEE using the Mifflin-St. Jeor Equation.

Parameters:
weight (float): Weight of the person in kilograms.
height (float): Height of the person in centimeters.
age (int): Age of the person in years.
gender (str): Gender of the person, either "male" or "female".
activity_level (float): Activity level of the person, ranging from 1.2 to 1.9.

Returns:
float: The TDEE of the person.
"""
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

def main():
    print("Welcome to the TDEE calculator!")
    while True:
        try:
            weight = float(input("Enter your weight in kilograms: "))
            if not (20 <= weight <= 250):
                raise ValueError("Invalid weight. Weight must be between 20 and 250 kilograms.")
            height = float(input("Enter your height in centimeters: "))
            if not (140 <= height <= 220):
                raise ValueError("Invalid height. Height must be between 140 and 220 centimeters.")
            age = int(input("Enter your age in years: "))
            if not (20 <= age <= 100):
                raise ValueError("Invalid age. Age must be between 20 and 100.")
            gender = input("Enter your gender (male or female): ")
            if gender.lower() not in ["male", "female"]:
                raise ValueError("Invalid gender. Gender must be either 'male' or 'female'.")
            

            while True:
                print("\nPlease select your activity level:")
                print("1 - Sedentary (little to no exercise)")
                print("2 - Light Activity (light exercise/sports 1-3 days a week)")
                print("3 - Moderate Activity (moderate exercise/sports 3-5 days a week)")
                print("4 - Very Active (hard exercise/sports 6-7 days a week)")
                print("5 - Super Active (very hard exercise/sports, physical job or training)")
                activity_level = str(input("Enter the number corresponding to your activity level (1-5): "))
                
                if activity_level not in ["1", "2", "3", "4", "5"]:
                    print("Error: Invalid input. Please enter a number between 1 and 5.")
                else:
                    if activity_level == "1":
                        activity_level = "sedentary"
                        explanation = "little to no exercise"
                    elif activity_level == "2":
                        activity_level = "lightly active"
                        explanation = "light exercise/sports 1-3 days a week"
                    elif activity_level == "3":
                        activity_level = "moderately active"
                        explanation = "moderate exercise/sports 3-5 days a week"
                    elif activity_level == "4":
                        activity_level = "very active"
                        explanation = "hard exercise/sports 6-7 days a week"
                    elif activity_level == "5":
                        activity_level = "extra active"
                        explanation = "very hard exercise/sports, physical job or training"
                    print(f"You have selected {activity_level.title()} ({explanation}).")
                    break

main()
