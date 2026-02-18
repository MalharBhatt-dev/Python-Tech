
#! WAP to print lowest Number from the list

num = [10,20,30,40,0]
min = num[0]

for i in num:
    if i <= min:
        min = i

print(f'{min} is the Lowest in the List {num}')
