
#! WAP to print Armstrong Numbers upto N:
#^ Strong: Sum of factorial of numbers
#^ Armstrong: Sum of digits with power of its length

num = int(input("Enter Limit: "))
out=[]
for i in range (1,num+1):

    sum = 0
    power = len(str(i))

    for j in str(i):
        digit = int(j)
        sum = sum + (digit**power)

    if i == sum:
        out.append(i)

print(f"Armstrong Numbers upto {num} are: {out}")
