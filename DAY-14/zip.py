
#! whenever we want to iterate over multiple collection at once, we can make use of zip function zip()

#~ Syntax: for var1,var2,..varn in zip(coln1,coln2,...colnn)

#* In the case of zip() function if length of the collections are different then zip function execution depends on length of the shortest/smallest collection

students = ['Dhruv','Smit','Rahul','Kuldeep','Yashraj Sir']
marks = [99, 32, 57, 78]
coll = [1,2,3]

d = {}

for i,j,k in zip(students,marks,coll):
    print(i,j,k)
    d[i]=j

print(d)