#Bmi calculator
def bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

# Main program
print("=== BMI Calculator ===")
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

bmi = bmi(weight, height)
category = bmi_category(bmi)

print(f"Your BMI is: {bmi:.2f}")
print(f"BMI Category: {category}")