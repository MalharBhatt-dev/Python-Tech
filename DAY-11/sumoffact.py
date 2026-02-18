
#! WAP to print sum of factorial of numbers upto n

num = int(input("Enter Number: "))
sum = 0

for i in range(1,num+1):
    fact=1

    for j in range(i,0,-1):
        fact = fact * j
    
    sum = sum + fact

print(f"{sum} is the sum of factorial for {num}")