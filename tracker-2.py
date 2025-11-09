# -------------------------------------------------------
# Name: Anant Yadav
# Date: 08 November 2025
# Project: GradeBook Analyzer - Python CLI
# -------------------------------------------------------

import csv
import statistics

# -----------------------------------------
# STATISTICAL FUNCTIONS (Task 3)
# -----------------------------------------
def calculate_average(marks_dict):
    return sum(marks_dict.values()) / len(marks_dict)

def calculate_median(marks_dict):
    return statistics.median(list(marks_dict.values()))

def find_max_score(marks_dict):
    return max(marks_dict, key=marks_dict.get), max(marks_dict.values())

def find_min_score(marks_dict):
    return min(marks_dict, key=marks_dict.get), min(marks_dict.values())

# -----------------------------------------
# GRADE ASSIGNMENT (Task 4)
# -----------------------------------------
def assign_grades(marks_dict):
    grades = {}
    for student, marks in marks_dict.items():
        if marks >= 90:
            grades[student] = 'A'
        elif marks >= 80:
            grades[student] = 'B'
        elif marks >= 70:
            grades[student] = 'C'
        elif marks >= 60:
            grades[student] = 'D'
        else:
            grades[student] = 'F'
    return grades

# -----------------------------------------
# DISPLAY TABLE FORMATTING (Task 6)
# -----------------------------------------
def display_results(marks_dict, grades_dict):
    print("\n========================================")
    print("          GRADEBOOK RESULTS")
    print("========================================\n")
    print(f"{'Name':<15}{'Marks':<10}{'Grade':<10}")
    print("----------------------------------------")

    for student, marks in marks_dict.items():
        print(f"{student:<15}{marks:<10}{grades_dict[student]:<10}")

    print("----------------------------------------")

# -----------------------------------------
# CSV OUTPUT (BONUS)
# -----------------------------------------
def export_results_to_csv(marks_dict, grades_dict):
    filename = "gradebook_output.csv"
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Marks", "Grade"])
        for student, marks in marks_dict.items():
            writer.writerow([student, marks, grades_dict[student]])
    print(f"\n✅ Results exported to {filename}")

# -----------------------------------------
# MAIN PROGRAM LOOP
# -----------------------------------------

print("\n========================================")
print("   Welcome to GradeBook Analyzer 📘✨")
print("========================================")

while True:
    
    print("\nChoose Input Method:")
    print("1️⃣  Manual Entry")
    print("2️⃣  Import CSV File")
    
    choice = input("Enter choice (1 or 2): ")

    marks = {}

    if choice == "1":
        num_students = int(input("\nHow many students? "))

        for i in range(num_students):
            name = input(f"Enter name of student {i+1}: ")
            marks[name] = int(input("Enter marks (0-100): "))

    elif choice == "2":
        filename = input("Enter CSV filename (example.csv): ")
        try:
            with open(filename, "r") as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    marks[row[0]] = int(row[1])
            print("\n✅ CSV Loaded Successfully!")
        except:
            print("❌ Error loading CSV. Try again!")
            continue
    else:
        print("❌ Invalid Choice! Try again.")
        continue

    # ✅ Perform Calculations
    avg = calculate_average(marks)
    median = calculate_median(marks)
    max_student, max_marks = find_max_score(marks)
    min_student, min_marks = find_min_score(marks)
    grades = assign_grades(marks)

    # ✅ Pass/Fail List (Task 5)
    passed_students = [s for s, m in marks.items() if m >= 40]
    failed_students = [s for s, m in marks.items() if m < 40]

    # ✅ Display Results
    display_results(marks, grades)

    print(f"\n📊 Class Average: {avg:.2f}")
    print(f"📈 Median Marks: {median}")
    print(f"🏅 Top Scorer: {max_student} ({max_marks})")
    print(f"⚠️ Lowest Score: {min_student} ({min_marks})")

    # ✅ Grade Distribution
    print("\n------ Grade Distribution ------")
    for grade in ['A', 'B', 'C', 'D', 'F']:
        count = list(grades.values()).count(grade)
        print(f"{grade}: {count}")

    print("\n✅ Passed Students:", passed_students)
    print("❌ Failed Students:", failed_students)

    # ✅ Bonus CSV Export
    export = input("\nDo you want to export results to CSV? (yes/no): ").lower()
    if export == "yes":
        export_results_to_csv(marks, grades)

    # ✅ Loop Menu
    repeat = input("\nDo you want to analyze again? (yes/no): ").lower()
    if repeat != "yes":
        print("\n✨ Thanks for using GradeBook Analyzer! Byeee! 😄✨\n")
        break
