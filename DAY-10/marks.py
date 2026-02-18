
#! WAP to find the highest marks and how many students got them.

marks = {'Anuradha':85, 'Baburao':90, 'Totlasheth':92, 'Shyam':92}
# output: Highest Marks= 92
# Students = ['Totlasheth','Shyam']

maxmarks = 0
students = []

for i in marks:
    if marks[i] >= maxmarks:
        maxmarks = marks[i]

for i in marks:
    if marks[i] ==  maxmarks:
        students.append(i)
        
print(f"Highest Marks: {maxmarks}")
print(f"Students: {students}")

    
