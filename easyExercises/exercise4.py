# Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest)
# and another number.
# The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.

#Solution
def isPresent(data: list, num: int):
    for number in data:        
        if (num==number):
            return True 
        elif(num<number):
            return False
    return False 
print(isPresent([5,10,15,20,25,30,45],46))