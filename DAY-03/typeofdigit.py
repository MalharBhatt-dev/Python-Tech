
#! WAP To check if the given digit is single digit or double digit or triple digit or greater than that

n = int(input('ENTER THE NUMBER: '))

if 0 <= n <= 9:
    print(f'{n} is a Single Digit Number')

elif 10 <= n <= 99:
    print(f'{n} is a Double Digit Number')

elif 100 <= n <= 999:
    print(f'{n} is a Triple Digit Number')

elif 1000 <= n:
    print(f'{n} is a greater or equal to 1000')

else:
    print(f'{n} is a negative number')


