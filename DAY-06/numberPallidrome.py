
#h wap to check if a given number is pallidrome or not..

n = int(input('Enter a number:'))
out=0
temp = n
while n>0:
    ld = n%10
    out = out*10 + ld
    n=n//10
if temp == out:
    print(f'{temp} is a pallidrome number.')
else:
    print(f'{temp} is not a pallidrome number.')