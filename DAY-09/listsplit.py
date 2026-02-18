
#! s = ['Python.py','pro1.html','prog3.py','goggle.com']
#! out = ['py','html','py','com']

s = ['Python.py','pro1.html','prog3.py','goggle.com']
out = []

for i in s:
    out.append(i.split('.')[1])

print(f"Output: {out}")