#Make dictionary store 5 student with marks then print the name of student with less than 60 marks


stud ={
    "Rohan": 85,
    "Arjun": 55,
    "Priya": 72,
    "Moana": 98,
    "Vikram": 45
}


student = {}

n = int(input("How many entries? "))

for i in range(n):
    print("Student: ", i+1)
    key = input("Enter name: ")
    value = int(input("Enter marks: ")) 
    student[key] = value

print(student)


# print("Students with marks less than 60:")
# for c, marks in student.items():
#     if marks < 60:
#         print(c)

#without enhanced for loop
print("Students with marks less than 60:")
for c in stud:
    if [c] < 60:
        print(c)  

        
    