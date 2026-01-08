
#! WAP to check if the character is uppercase or lowercase or digit or special character

n = input('ENTER THE CHARACTER: ')

if 'A' <= n <= 'Z':
    print(f'{n} is a UPPERCASE CHARACTER')

elif 'a' <= n <= 'z':
    print(f'{n} is a LOWERCASE CHARACTER')

elif '0' <= n <= '9':
    print(f'{n} is a Number')

else:
    print(f'{n} is a Special Character')
