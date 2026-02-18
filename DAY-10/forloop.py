
#! WAP to ge the following Output
#! h = 'abcabacbcc'
#! out = 'a3b3c4'

h = input("Enter a sequence of String:")
out = ''

for i in h:
    if i not in out:
        counter =  str(h.count(i))
        out = out + i + counter + ' '

print(out)

