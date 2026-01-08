
#h smallest amount 4 numbers using only elif...->



a = int(input('Enter the first number:'))
b = int(input('Enter the second number:'))
c = int(input('Enter the third number:'))
d = int(input('Enter the fourth number:'))
if a < b and a < c and a < d:
    print(f"{a} is the smallest.")
elif b < a and b < c and b < d:
    print(f"{b} is the smallest.")
elif c < a and c < b and c < d:
    print(f"{c} is the smallest.")
elif d < a and d < b and d < c:
    print(f"{d} is the smallest.")
else:
    print(f'All the numbers are same...')    