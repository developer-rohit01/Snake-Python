#print 15 natural number and their sum using while loop and average of 15 natural number

number = 1
total_sum = 0
while number <= 15:
    print(number)
    total_sum += number
    number += 1
print(f"Sum of first 15 natural numbers is: {total_sum}")
average = total_sum / 15
print(f"Average of first 15 natural numbers is: {average}")

for i in range(1,16):
    print(i)    
    sum = sum + i
print(f"Sum of first 15 natural numbers is: {sum}")
average = sum / 15
print(f"Average of first 15 natural numbers is: {average}")


    


