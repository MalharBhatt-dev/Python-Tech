
#! WAP to check if the given data is SVDT or not

data = eval(input('ENTER DATA:'))

if type(data) in [list,str,tuple,set,dict]:
    print(f'{data} is a Multi Value Data Type')

else:
    print(f'{data} is a Single Value Data Type')