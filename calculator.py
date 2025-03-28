# 🧩 Exercise 3: Create a simple calculator

# Write a function called calculator that:

# Takes 3 parameters: num1, num2, operator (like "+", "-", "*", "/")

# Uses if/elif/else to perform the operation

# Returns the result

def calculator(num1,num2,operation):
    if(operation == "+"):
        return num1+num2
    elif(operation == "-"):
        return num1 - num2
    elif(operation == "*"):
        return num1*num2
    elif(operation == "/"):
        return num1/num2
    else:
        print("Enter valid operations")

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Enter the operation: ")
print("Answer is :",calculator(num1,num2,operation))