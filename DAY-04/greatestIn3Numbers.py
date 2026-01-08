
#h wap to find the greatest amound the 3 numbers...-> 

a = int(input('Enter the first number:'))
b = int(input('Enter the second number:'))
c = int(input('Enter the third number:'))

if a > b and a > c:
    print(f"{a} is the greatest.")
elif b > a and b > c:
    print(f"{b} is the greatest.")
elif c > a and c > b:
    print(f"{c} is the greatest.")
else:
    print(f'All the numbers are same...')    