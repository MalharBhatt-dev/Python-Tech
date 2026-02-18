

#h wap to check is a given number  is perfect number or not using for loop.

n = int(input("Enter the number :"))
sum = 0
for i in range (1 , n):
    if n%i==0:
        sum += i
if (sum == n):
    print(f'{n} is Perfect Number.')
else:
    print(f'{n} is not a Perfect Number.')



