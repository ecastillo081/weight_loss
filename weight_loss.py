import pandas as pd
from datetime import datetime

start_weight = 142.00
end_weight = 130
height = 65 #inches
age = 29
gender = 'male'
goal_date = '2024-06-01'
activity_level = 'sedentary'
workout_minutes = 15
workout_intensity = 5

# Update the weight_loss_calculator function to return a DataFrame
def weight_loss_calculator_df(start_weight, end_weight, height, age, gender, goal_date, activity_level, workout_minutes,
                              workout_intensity):
    # activity multipliers
    activity_multipliers = {
        "sedentary": 1.2,
        "light": 1.375,
        "moderate": 1.55,
        "active": 1.725,
    }

    # height to centimeters and weight to kilograms
    height_cm = height * 2.54  # inches to cm
    start_weight_kg = start_weight / 2.205  # lbs to kg

    # calc BMR using Mifflin-St Jeor formula
    if gender == "male":
        BMR = 10 * start_weight_kg + 6.25 * height_cm - 5 * age + 5
    else:
        BMR = 10 * start_weight_kg + 6.25 * height_cm - 5 * age - 161

    # adj based on activity level
    daily_calorie_needs = BMR * activity_multipliers[activity_level]

    # calorie burn on stair master
    calories_burned_per_minute = workout_intensity * (start_weight / 2.205) * 0.0175
    workout_calories = calories_burned_per_minute * workout_minutes

    # daily calorie goal
    daily_calorie_goal = daily_calorie_needs - (500 + workout_calories)

    # weight loss goal and weekly weight loss
    total_weight_loss = start_weight - end_weight
    days_to_goal = (datetime.strptime(goal_date, "%Y-%m-%d") - datetime.now()).days
    weekly_weight_loss = total_weight_loss / (days_to_goal / 7)

    data = {
        "Metric": ["BMR", "Daily Calorie Needs", "Workout Calories Burned", "Daily Calorie Goal",
                   "Total Weight Loss Goal", "Weekly Weight Loss Target", "Days to Goal"],
        "Value": [BMR, daily_calorie_needs, workout_calories, daily_calorie_goal, total_weight_loss, weekly_weight_loss,
                  days_to_goal]
    }

    return pd.DataFrame(data)


# Calculate weight loss plan
df_weight_loss = weight_loss_calculator_df(start_weight, end_weight, height, age, gender, goal_date, activity_level,
                                       workout_minutes, workout_intensity)

print(df_weight_loss)
