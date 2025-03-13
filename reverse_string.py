# Write a program to reverse a string.

string = str(input("Enter the string word: "))
reverse_str = ""
for word in string:
    reverse_str = word+ reverse_str  
print(reverse_str, "This is reverse string")

