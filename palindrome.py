#  Write a program to check if a string is a palindrome.
string = str(input("Enter the string word:"))
reverse_str = ""
for word in string:
    reverse_str = word+ reverse_str  
if(string != reverse_str):
    print("This is not palindrome word")
else:
    print("This is palindrome word")
