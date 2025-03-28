# 🧩 Exercise 2: Custom number guessing function

# Write a function called guess_number(secret) that:

# Uses a while loop to let the user guess

# Ends the loop when they get it right

# Gives a hint: "Too high" / "Too low"

secretNumber = int(23)
def guessNumber():
    while(True):
        secret = int(input("Enter your guessing number: "))
        if(secret == secretNumber):
           print("🎉 Won.!!")
        elif(secret > secretNumber):
            print("📈 Too high")
        else:
            print("📉 Too Low")


print(guessNumber())