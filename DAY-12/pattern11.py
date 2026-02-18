
#! 1        
#! 1 2      
#! 2 3 4    
#! 4 5 6 7  
#! 8 9 10 11

n=5
start=1

for i in range(1,n+1):
    for j in range(1,i+1):
        print(f'{start}',end=' ')
        start = start + 1
    start -=1
    print()



print('---------------------------')
#! 65            
#! 66 67         
#! 68 69 70      
#! 71 72 73 74   
#! 75 76 77 78 79

n1=5
start1=65

for i in range(1,n1+1):
    for j in range(1,i+1):
        print(f'{start1}',end=' ')
        start1 = start1 + 1
    print()


print('---------------------------')
#! A        
#! B C      
#! D E F    
#! G H I J  
#! K L M N O

n2=5
character1 = 'A'
start2=ord(character1)

for i in range(1,n+1):
    for j in range(1,i+1):
        print(f'{chr(start2)}',end=' ')
        start2 = start2 + 1
    print()


print('---------------------------')
#! A        
#! B C      
#! D E F    
#! G H I J  
#! K L M N O

n3=5
character2 = 'A'
start3=ord(character2)

for i in range(1,n+1):
    for j in range(1,i+1):
        print(f'{chr(start3)}',end=' ')
        start3 = start3 + 1
    start3 = start3 - 1
    print()

print('---------------------------')
#! D        
#! D H      
#! D H R    
#! D H R U  
#! D H R U V

n=5
name = 'DHRUV'

for i in range(0,len(name)):
    for j in range(0,len(name)):
        if i>=j:
            print(name[j],end=' ')
    print()




print('---------------------------')
#! 1 2 3 4 5
#! 1 2 3 4  
#! 1 2 3    
#! 1 2      
#! 1        

n = 5
start = 1

for i in range(1,n+1):
    for j in range(1,n+1):
        if i<=j:
            print(start, end=' ')
            start = start + 1
    start = 1 
    print()

for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()


#! A B C D E
#!   B C D E
#!     C D E
#!       D E
#!         E


n = 5
char = 'A'
start5 = ord(char)

for i in range(1,n+1):
    for j in range(1,n+1):
        if i <= j:
            print(chr(start5), end=' ')
            start5 = start5 + 1
        else:
            print(f' ', end=' ')
    start5 = ord(char) + i 
    print()