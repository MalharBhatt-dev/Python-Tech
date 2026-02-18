#----------------------------------------------
#! d = [{'tesla':{'model':'x','color':'red'}},
#!      {'audi':{'model':'y','color':'black'}}]

d = [{'tesla':{'model':'x','color':'red'}},
    {'audi':{'model':'y','color':'black'}}]

out = []

for i in d: #
    for j in i:  # i = {'tesla':{'model'.....}}
        out.append(i[j])

print(out)


