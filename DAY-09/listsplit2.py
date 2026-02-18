s = ['p1.py','file2.txt','file1.py','goggle.com', 'data.txt']
out = {}

for i in s:
    result = (i.split('.'))
    key = result[1]
    value = result[0]
    
    if result[1] not in out:
        out[result[1]] = [result[0]]
    else:
        out[result[1]].append(result[0])


print(f"Output: {out}")