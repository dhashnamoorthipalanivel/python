#  Write a program to find the factorial of a number.

number = int(input("Enter the Number: "))
count = 1
for i in range(1,number+1):
    count = count*i
print("Factorial value is: ",count)