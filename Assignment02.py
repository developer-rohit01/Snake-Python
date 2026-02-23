print("Student Performance Record")

def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 40:
        return "D"
    else:
        return "Fail"

choice = "yes"

while choice == "yes":

    student = {}
    marks = []

    student["name"] = input("Enter Student Name: ")
    print("Enter Student Marks:")

    for i in range(1, 5):
        mark = float(input(f"Enter Subject {i} Marks: "))
        marks.append(mark)

    student["marks"] = marks
    student["total"] = sum(marks)
    student["average"] = student["total"] / 4
    student["grade"] = calculate_grade(student["average"])

  
    with open("student_records.txt", "a") as file:
        file.write("-----------------------------\n")
        file.write(f"Name: {student['name']}\n")
        file.write(f"Marks: {', '.join(map(str, student['marks']))}\n")
        file.write(f"Total: {student['total']}\n")
        file.write(f"Average: {round(student['average'], 2)}\n")
        file.write(f"Grade: {student['grade']}\n")
        file.write("-----------------------------\n\n")

    print("\nRecord Saved Successfully!\n")

    choice = input("Do you want to enter another student record? (yes/no): ")
    
view_choice = input("Do you want to view all records? (yes/no): ")
if view_choice == "yes":
    with open("student_records.txt", "r") as file:
        records = file.read()
        print("\nStudent Records:\n")
        print(records)

del_choice = input("Do you want to delete all records? (yes/no): ")
if del_choice == "yes":
    with open("student_records.txt", "w") as file:
        file.write("")
    print("All records have been deleted.")
    

print("Thanks for using the system.")