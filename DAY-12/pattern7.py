
#! 1 1 1 1 0
#! 1 1 1 0 2
#! 1 1 0 2 2
#! 1 0 2 2 2
#! 0 2 2 2 2

n=5

for i in range(1,n+1):
    for j in range(1,n+1):
        if i+j < n+1:
            print('1',end=' ')
        elif i+j == n+1:
            print('0', end=' ')
        else:
            print('2', end=' ')
    print()