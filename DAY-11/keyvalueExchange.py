
#! input: {'star':10, 'byee':30, 'moon':80}
#! output: {10:'star', 30:'byee' , 80:'moon'}

input= {'star':10, 'byee':30, 'moon':80}
out={}

for i in input:
    key = input[i]
    value = i
    out[key] = value

print(out)