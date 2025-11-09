# -------------------------------------------------------
# Name: Anant Yadav
# Date: 08 November 2025
# Project: Daily Calorie Tracker CLI
# -------------------------------------------------------

import datetime

print("\n===========================================")
print("       DAILY CALORIE TRACKER APP 😋")
print("===========================================\n")

# Task 2: Input & Data Collection
meal_names = []
meal_calories = []

num_meals = int(input("How many meals do you want to add today? "))

for i in range(num_meals):
    print(f"\nMeal {i+1}")
    meal_name = input("Enter meal name: ")
    meal_calorie = float(input("Enter calorie amount: "))
    
    meal_names.append(meal_name)
    meal_calories.append(meal_calorie)

# Task 3: Calorie Calculations
total_calories = sum(meal_calories)
average_calories = total_calories / len(meal_calories)

daily_limit = float(input("\nEnter your daily calorie limit: "))

# Task 4: Exceed Limit Warning System
print("\n-------------------------------------------")
if total_calories > daily_limit:
    print("⚠️ WARNING: You have exceeded your daily calorie limit!")
else:
    print("✅ Good job! You're within your calorie limit!")
print("-------------------------------------------")

# Task 5: Summary Table Output
print("\n======= TODAY'S CALORIE REPORT =======\n")
print("Meal Name\tCalories")
print("-------------------------------------")

for i in range(len(meal_names)):
    print(f"{meal_names[i]}\t\t{meal_calories[i]}")

print("-------------------------------------")
print(f"Total:\t\t{total_calories}")
print(f"Average:\t{average_calories:.2f}")
print("-------------------------------------\n")

# Bonus Task 6: Save Session Log to File
save_choice = input("Do you want to save this report to a file? (yes/no): ").lower()

if save_choice == "yes":
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    filename = "calorie_log.txt"
    
    with open(filename, "a") as file:
        file.write("\n===========================================\n")
        file.write(f"Date & Time: {timestamp}\n")
        file.write("MEAL LOG:\n")
        
        for i in range(len(meal_names)):
            file.write(f"{meal_names[i]} - {meal_calories[i]} Calories\n")
        
        file.write("-------------------------------------------\n")
        file.write(f"Total Calories: {total_calories}\n")
        file.write(f"Average Calories: {average_calories:.2f}\n")
        file.write(f"Daily Limit: {daily_limit}\n")
        
        if total_calories > daily_limit:
            file.write("Status: Exceeded Limit ⚠️\n")
        else:
            file.write("Status: Within Limit ✅\n")
        file.write("===========================================\n")
    
    print(f"\n✅ Report saved successfully in '{filename}'!")
else:
    print("\nReport not saved.")

print("\nThank you for using Calorie Tracker! Stay healthy! 💪😄\n")
