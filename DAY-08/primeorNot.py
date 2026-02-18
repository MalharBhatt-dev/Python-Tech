

#h wap to check if a given number is prime or not..

n = 5
count = 0
for i in range(2,n):
    if (n%i==0):
        count+=1
if(count>0):
    print(f'{n} is not a prime number.')
else:
    print(f'{n} is a prime number.')
