# Write a program to find the length of a string without using built-in functions.

text = str(input("Enter your word: "))
string_length = 0
for word in text:
    string_length+=1
print(string_length, "is the string length")
