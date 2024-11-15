# Given values
weight = 144
height_feet = 5
height_inches = 4

# calc
height_total_inches = height_inches + (height_feet * 12)

weight_kg = weight * 0.4536  # converting pounds to kilograms
height_m = height_total_inches * 0.0254    # converting inches to meters

# BMI calc
bmi = weight_kg / (height_m ** 2)

print(bmi)

# overweight bmi range: BMI 25–29.9
# normal bmi range: 18.5 - 24.9

