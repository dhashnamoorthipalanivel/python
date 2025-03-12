# Write a program to check if a number is prime.
number = int(input("Enter your Number: "))
if(number>1):
    for i in range(2,number):
        if(number%i == 0):
            print(number," This is not a prime number")
            break
    else:
        print(number, "This is a prime Number")
else:
    print(number,"This is ivalid number")
       

