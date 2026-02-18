

#h wap input = "HoLIdaY" & output = "hOliDAy"

input = "HoLIdaY"
# output = "hOliDAy"
output = ""

for i in input :
    if 'A'<=i<='Z':
        output  = output + i.lower()
    elif 'a'<=i<='z':
        output = output + i.upper()
print(output)