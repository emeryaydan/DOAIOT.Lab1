def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight / (height * height)
    print("BMI = " + str(round(bmi, 2)))
    return bmi

calculate_bmi(weight=57, height=1.73)