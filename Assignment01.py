print("Welcome to My Grading System")
choice = 'yes'
while choice == 'yes':
    student = input("Enter Student name: ")
    firstMarks = float(input("Enter first marks: "))
    secondMarks =float(input("Enter second marks: "))
    thirdMarks = float(input("Enter third marks: "))
    totalmarks = firstMarks + secondMarks + thirdMarks
    avg = totalmarks / 3
    
    print("Total Marks: ",totalmarks)
   
    print("Average: ",round(avg,2))
    
    
    if avg >= 90:
      print("Grade: A")
    elif avg >= 75 and avg < 90:
      print("Grade: B")
    elif avg >= 60 and avg < 75:
      print("Grade: C")
    elif avg >=40  and avg < 60:
      print("Grade: D")
    else:
      print("Fail")
    choice = input("Do you want to do it again yes/no: ")
print("Thanks for Using")