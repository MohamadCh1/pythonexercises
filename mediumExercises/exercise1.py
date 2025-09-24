# Write a Python program to find three numbers from an array such that the sum of three numbers equal to zero. 
# Input : [-1,0,1,2,-1,-4] Output : [[-1, -1, 2], [-1, 0, 1]] Note : Find the unique triplets in the array.

#Solution
#accept duplicate
def findSumZero(data: list):
    data.sort()
    result =set()
    for num1 in data:
        for num2 in data:
            for num3 in data:
                if (num1+num2+num3==0):
                    temp=tuple(sorted([num1,num2,num3]))
                    if(temp not in result):
                        result.add(tuple(temp))
    return result
print(findSumZero([-1,0,1,2,-1,-4]))
#No duplicate
def findSumZeroNoDuplicate(data: list):
    result =set()
    n=len(data)
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if (data[i]+data[j]+data[k]==0):
                    temp=tuple(sorted([data[i],data[j],data[k]]))
                    if(temp not in result):
                        result.add(temp)
    return result
print(findSumZeroNoDuplicate([-1,0,1,2,-1,-4]))