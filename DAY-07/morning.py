c='PyTH@1!2'
upper=0
lower=0
digit=0
special=0
i=0
str = ""
while i<len(c):
    if 'A'<=c[i]<='Z':
        upper+=1
    elif 'a'<=c[i]<'z':
        lower+=1
    elif '0'<=c[i]<='9':
        digit+=1
    else:
        special+=1
    i+=1


# str = lower+upper+digit+special


print(f'upper = {upper}')
print(f'lower = {lower}')
print(f'digit = {digit}')
print(f'special = {special}')

#WAP to find the sum of digits of a number::eg: input - 145 output = 1+4+5 = 10