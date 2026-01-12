
#h wap to reverse a number...->
n = int(input('Enter a number:'))
out=0
while n>0:
    ld = n%10
    out = out*10 + ld
    n=n//10
print(f'Actual number is : {n}')
print(f'Reversed number is: {out}')
