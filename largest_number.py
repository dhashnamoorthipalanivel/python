# 🧩 Exercise 1: Find the largest number from a list

# 🎯 Goal: Create a function called find_largest that loops through a list and returns the largest number.

def find_largest(number):
    largest = number[0]
    for num in number:
        if(num > largest):
            largest = num
    return largest 

print(find_largest([1,2,3,5,6]))