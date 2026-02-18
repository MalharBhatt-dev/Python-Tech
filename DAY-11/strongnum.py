
#! WAP to check if a number is strong number or not

num = int(input("Enter Number: "))
sum = 0

for i in str(num):
    fact=1
    digit = int(i)
    for j in range(digit,0,-1):
        fact = fact * j
    
    sum = sum + fact

if sum == int(num) :
    print(f"{num} is Strong Number.")
else:
    print(f"{num} is not a Strong Number.")