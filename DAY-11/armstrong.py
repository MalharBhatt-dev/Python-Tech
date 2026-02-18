
#! WAP to check if the number is Armstrong Number or not

num = int(input("Enter Number: "))
sum = 0
length = len(str(num))

for i in str(num):
    digit = int(i)
    sum = sum + (digit**length)

if num == sum:
    print(f"{num} is a Armstrong Number")
else:
    print(f"{num} is not a Armstrong Number")

