# Write a program to count the number of vowels and consonants in a string.
text = str(input("Enter your word: "))
text_upper = text.upper()
vowel = 0
consonants = 0 
for word in text_upper:
    if("A" <= word <= "Z"):
        if(word == "A" or word == "E" or word == "I" or word == "O" or word == "U"):
            vowel +=  1
        else:
            consonants += 1

print("Vowel count is: ",vowel)
print("Consonants count is:",consonants)