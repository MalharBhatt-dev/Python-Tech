
n = 5

for i in range (1,n+1):
    for s in  range(1, (n-i)+1): # 1 2 3 4
        print(' ',end=' ')
    for j in range(1,(i*2-1)+1): # 1 3 5 7 9
        print('*',end=' ')
    print()


print('_____________________________________')
n = 5

for i in range (n,0,-1):
    for s in  range(1, (n-i)+1): # 1 2 3 4
        print(' ',end=' ')
    for j in range(1, (i*2-1)+1): # 1 3 5 7 9
        print('*',end=' ')
    print()

