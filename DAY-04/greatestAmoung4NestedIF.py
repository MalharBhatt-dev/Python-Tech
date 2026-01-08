
#h wap to find the greatest amound the 4 numbers...-> 

a = int(input('Enter the first number:'))
b = int(input('Enter the second number:'))
c = int(input('Enter the third number:'))
d = int(input('Enter the fourth number:'))

if a>=b :
    if a>=c :
        if a>=d :
            print(f"{a} is the greatest.")
        else:
            print(f"{d} is the greatest.")
    else:
        if c>=d :
            print(f"{c} is the greatest.")
        else:
            print(f"{d} is the greatest.")
else:
    if b>=c :
        if b>=d :
            print(f"{b} is the greatest.")
        else:
            print(f"{d} is the greatest.")
    else:
        if c>=d :
            print(f"{c} is the greatest.")
        else:
            print(f"{d} is the greatest.")