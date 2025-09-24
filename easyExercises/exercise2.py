# Ask the user for a number. 
# Depending on whether the number is even or odd, print out an appropriate message to the user.
# Hint: how does an even / odd number react differently when divided by 2?

# Extras:

# If the number is a multiple of 4, print out a different message. 
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). 
# If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

#Solution
num = int(input("What is the number you want to check if it is even or odd?"))
num2 = int(input("By which number you want to check if it can be divided by it?"))
if (num%2==0):
    print("The number is even!")
else:
    print("The number is odd!")
if(num%num2==0):
    print(f"The number {num} is a multiple of {num2}")
else:
    print(f"The number {num} isn't a multiple of {num2}")
