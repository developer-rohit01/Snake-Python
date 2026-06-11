#take user input and check for even or odd 

#



number = int(input("Enter a number: "))
snumber= int(input ("Enter another number: "))
if number % 2 == 0:
    if  number % 4==0:
        print("This number is divisible by both 2 and 4")
else:
    print("this number is not divisible by ",number ,"or ",snumber)



