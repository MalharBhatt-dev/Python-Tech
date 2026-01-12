#wap to check if a given number is perfect number or not..

n = int(input('Enter a number:'))
i = 1
sum = 0
while i < n:
    if n % i == 0:
        sum += i
    i+=1
if sum == n:
    print('Given number is a perfect number.')
else:
    print('Given number is not a perfect number.')