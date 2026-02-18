
#! input = 'aaabbaabcc'
#! out = 'a3b2a2b1c2'

input = 'aaabbaabcc'
out = ''
counter = 1

for i in range(len(input)-1):

    current = input[i]
    next = input[i+1]

    if current == next:
        counter += 1

    else:
        out = out + current + str(counter)
        counter = 1

out = out + input[-1] + str(counter)
print(out)