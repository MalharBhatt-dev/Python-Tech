
#! o = 'abcabbcba'
#! output = {'a':3, 'b':4, 'c':2}

o = input("Enter a String: ")
out = {}

for i in o:
    
    if i not in out:
        out[i] = 1
    else:    
        out[i] += 1

print(f"Desired Output: {out}") 



