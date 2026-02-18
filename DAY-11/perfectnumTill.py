
#! WAP to print all perfect number upto N

limit = int(input("Enter the Limit: "))
out = []

for i in range(1,limit):
    sum = 0
    for j in range(1,i):
        if i % j == 0:
            sum = sum + j
    if sum == i:
        out.append(i)

print(f"Perfect Numbers upto {limit} are: {out}")