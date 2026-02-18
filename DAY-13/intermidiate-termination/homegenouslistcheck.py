
#! WAP to check if the given list is homogeneous or not

l1 = list(input("Enter Elements of List:"))
check = type(l1[0])

for i in l1:
    if type(i) != check:
        print(f'{l1} is a Heterogenous List.')
        break
else:
    print(f"{l1} is a Homogenous List")
