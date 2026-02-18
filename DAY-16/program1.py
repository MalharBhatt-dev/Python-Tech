
#! 1. WAP TO CHECK IF A GIVEN LIST IS HOMOGENOUS OR HETEROGENOUS.

l = [1,2,3,4,5,6.5]
typeof = type(l[0])

for i in l:
    if typeof != type(i):
        print(f'{l} is a Heterogenous List')
        break

else:
    print(f"{l} is a Homogenous List")
