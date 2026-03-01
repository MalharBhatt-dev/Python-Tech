#wap to extract only vowels from the string given by user..

s = input("Enter the string :")
out = ""
i = 0
while i < len(s):
    if s[i] in 'aeiouAEIOU':
        out += s[i]
    i += 1
print(f'The vowels in given string {s} : {out}')
