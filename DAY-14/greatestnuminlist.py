
#! WAP to print greatest num from the list using for loop

num = [11,27,21,56,10]
max = 0

for i in num:
    if i > max:
        max = i

print(f'{max} is the maximum number in the List {num}')


