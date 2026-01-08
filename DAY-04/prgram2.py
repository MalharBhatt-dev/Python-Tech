
#h wap to check if the given number is positive or negative or zero..-->

num = int(input("Enter a number: "))
if num > 0:
    print(f"{num} is a positive number.")
elif num < 0:
    print(f"{num} is a negative number.")
else:
    print("The number is zero.")
