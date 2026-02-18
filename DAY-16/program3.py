
#! 3. WAP TO CHECK IF A GIVEN NUMBER IS STRONG NUMBER OR NOT

num = 145
sum = 0 

for i in str(num):
    digit = int(i)
    fact = 1
    for j in range(digit,0,-1):
        fact = fact*j
    sum = sum + fact

if sum == num:
    print(f"{num} is a Strong Number")  
else:
    print(f"{num} is not a Strong Number") 