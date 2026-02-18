
#! 4. WAP TO CHECK IF A GIVEN NUMBER IS ARMSTRONG NUMBER OR NOT

num = 153
length = len(str(num))
sum = 0

for i in str(num):
    sum = sum + int(i) ** length

if sum == num:
    print(f'{num} is an ArmStrong Number')
else:
    print(f'{num} is not an ArmStrong Number')
