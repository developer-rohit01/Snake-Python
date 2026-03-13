print("Student Performance Record System")


def calculate_total(marks):
    return sum(marks)

def calculate_average(total, subjects):
    return total / subjects

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

    print("Enter Marks of 4 Subjects:")

    for i in range(1,5):
        mark = float(input(f"Enter Subject {i} Marks: "))
        marks.append(mark)

    student["marks"] = marks


    student["total"] = calculate_total(marks)
    student["average"] = calculate_average(student["total"],4)
    student["grade"] = calculate_grade(student["average"])


    with open("student_records.txt","a") as file:

        file.write("---------------\n")
        file.write(f"Name: {student['name']}\n")
        file.write(f"Marks: {student['marks']}\n")
        file.write(f"Total: {student['total']}\n")
        file.write(f"Average: {round(student['average'],2)}\n")
        file.write(f"Grade: {student['grade']}\n")
        file.write("---------------\n\n")

    print("\nRecord Saved Successfully!\n")

    choice = input("Enter another student? (yes/no): ")


view = input("Do you want to view all records? (yes/no): ")

if view == "yes":
    with open("student_records.txt","r") as file:
        print("\nStored Records:\n")
        print(file.read())

print("Program Finished.")