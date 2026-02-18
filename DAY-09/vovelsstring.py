o = "i am also present there"
out = {}

for i in o:
    if i in 'aeiouAEIOU':
        if i not in out:
            out[i] = 1
        else:    
            out[i] += 1

print(f"Desired Output: {out}") 