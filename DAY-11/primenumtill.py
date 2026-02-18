
#! WAP to print all prime numbers upto N

limit = int(input("Enter the Limit: "))


out=[]

for i in range(2,limit+1):
    div=1
    for j in range(2,i):
        if i % j == 0:
            div = div+1
    if div == 1:
        out.append(i)

print(f"Prime Numbers between 2 and {limit} are: {out}")