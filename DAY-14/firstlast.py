
s = 'example on for loop'
inputstr = s.split()
print(inputstr)
out = ''

for i in inputstr:
    first = i[0]
    last = i[len(i)-1]
    out = out + first + last + ' '

print(out) 
