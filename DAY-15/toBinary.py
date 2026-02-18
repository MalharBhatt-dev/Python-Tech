
#! WAP to convert int to binary.

n = 10
out = ''

while n>=1: 
    temp = n % 2 
    out = str(temp) + out 
    n = n // 2

print(int(out)) 

