
#! Input = "this is a test this is simple"
#! Output = {'this':2, 'is':2, 'a':1, 'test':1, 'simple':1}

sent = "this is a test this is simple"
input = sent.split()
out={}

for i in input:
    if i not in out:
        out[i] = 1
    else:
        out[i] = out[i] + 1

print(f"Desired Output: {out}")