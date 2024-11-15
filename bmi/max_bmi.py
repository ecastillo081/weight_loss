from bmi.bmi_calculator import height_m
# Max BMI
max_bmi = 24.9

# calc max weight in kilograms
max_weight_kg = max_bmi * (height_m ** 2)

# Convert weight to pounds
max_weight_lbs = max_weight_kg / 0.4536

# calc pounds to lose
pounds_to_lose = 150 - max_weight_lbs

print(max_weight_lbs)
print(pounds_to_lose)
