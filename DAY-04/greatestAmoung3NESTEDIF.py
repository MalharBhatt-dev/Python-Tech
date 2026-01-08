
#h    wap to find the greatest amoung 3 numbers using nested if....->

a = int(input('Enter the first number:'))
b = int(input('Enter the second number:'))  
c = int(input('Enter the third number:'))
if a > b:
    if a > c:
        print(f"{a} is the greatest.")
    else:
        print(f"{c} is the greatest.")
else:
    if b > c:
        print(f"{b} is the greatest.")
    else:
        print(f"{c} is the greatest.")