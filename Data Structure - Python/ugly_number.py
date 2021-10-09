# Python3 code to find nth ugly number
 
# This function divides a by greatest
# divisible power of b
 
 
def maxDivide(a, b):
    while a % b == 0:
        a = a / b
    return a
 
# Function to check if a number
# is ugly or not
def isUgly(no):
    no = maxDivide(no, 2)
    no = maxDivide(no, 3)
    no = maxDivide(no, 5)
    return 1 if no == 1 else 0
 
# Function to get the nth ugly number
def getNthUglyNo(n):
    i = 1
     
    # ugly number count
    count = 1 
 
    # Check for all integers untill
    # ugly count becomes n
    while n > count:
        i += 1
        if isUgly(i):
            count += 1
    return i
 
 
# Driver code
num=int(input())
no = getNthUglyNo(num)
print(num ,"th ugly no. is ", no)
 
