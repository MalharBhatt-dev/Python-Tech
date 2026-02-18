
input = 'my name is dhruv'
out = ''

for j in range(0,len(input)) :
    
    if j == 0:
        out = out + chr(ord(input[j]) - 32)
    elif input[j-1] == ' ':
        out = out +  chr(ord(input[j]) - 32)
    else:
        out = out + input[j]

print(out)