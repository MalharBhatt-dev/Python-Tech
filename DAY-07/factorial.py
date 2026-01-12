
#h Wap to find the factorial of the numbers

n = int(input("Enter a number: "))
temp = n
factorial = 1
while temp > 0:
    factorial = factorial * temp
    temp -= 1
print(f"The factorial of {n} is {factorial}")
