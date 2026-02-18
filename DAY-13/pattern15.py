n = 5
char = 'A'
start = ord(char)
for i in range (1,n+1):
    for s in  range(1, (n-i)+1): # 1 2 3 4
        print(' ',end=' ')
    for j in range(1,(i*2-1)+1): # 1 3 5 7 9
        print(chr(start),end=' ')
        start = start+1
    start = ord(char)
    print()