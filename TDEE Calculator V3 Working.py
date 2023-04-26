import math
import builtins

# override the input() function to convert all input strings to lowercase
def input(prompt):
    return builtins.input(prompt).lower()

def main():
    sex = input("Are you Male or Female?")
    if sex == "male":
        print(bmr_male() * tdee())    
    else:
        print(bmr_female() * tdee())

#weight in kg, height in cm
#function for male bmr
def bmr_male():
    age = float(input("What is your age?"))
    weight = float(input("What is your weight in kg?"))
    height = float(input("What is your height in cm?"))
    return 10 * weight + 6.25 * height - 5 * age + 5

#weight in kg, height in cm
#function for female bmr
def bmr_female():
    age = float(input("What is your age?"))
    weight = float(input("What is your weight in kg?"))
    height = float(input("What is your height in cm?"))
    return 10 * weight + 6.25 * height - 5 * age - 161

# asking for activity level and using if statements to choose what those options represent.
def tdee():
    activness = float(input("Choose activity level from the following.\nFor sedentary - desk job and little to no exercise enter 1.\n\
    For light - exercise 1 to 3 days per week enter 2.\nFor moderate - exercise 3 to 5 days per week enter 3.\n\
    For hard - exercise 6 to 7 days per week enter 4.\nFor extremely - daily exercise and physical job or training enter 5."))   
    if activness == 1:
        return 1 * 1.2
    elif activness == 2:
        return 1 * 1.375
    elif activness == 3:
        return 1 * 1.55
    elif activness == 4:
        return 1 * 1.725
    elif activness == 5:
        return 1 * 1.9
    
main()




      




     



    

