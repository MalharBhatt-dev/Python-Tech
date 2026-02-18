
l = ['p1.py','file2.txt','file.py','google.com','data.txt']
out={}

for i in l:
    splited = i.split('.')
    key = splited[1]
    value = splited[0]
    if key in out:
        out[key].append(value)
    else:
        out[key] = [value]

print(out)

