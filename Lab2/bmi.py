def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight / (height * height)
    print("BMI = " + str(round(bmi, 2)))
    
    if bmi < 18.5:
        classification = "Under Weight"
    elif 18.5 <= bmi <= 25.0:
        classification = "Normal Weight"
    else:
        classification = "Over Weight"
    
    print("Weight Classification: " + classification)
    return bmi

calculate_bmi(weight=57, height=1.73)