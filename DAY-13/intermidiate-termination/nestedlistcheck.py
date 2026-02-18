
#! WAP to check the given list is containing nested list or not

l = [1,2,3,4,5,[23,24,25],[11,22]]

for i in l:
    if type(i) == list:
        print('It is having Nested List')
        break
else:
    print('It is not a Nested List')
