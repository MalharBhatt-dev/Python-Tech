
#! 2. WAP TO CHECK IF A GIVEN NUMBER IS PRIME NUMBER OR NOT.

num = 17
count = 0
for i in range(2,num):
    if num % i == 0:
        count = 1
        break

if count == 1:
    print(f"{num} is not a Prime Number")
else:
    print(f"{num} is a Prime Number") 