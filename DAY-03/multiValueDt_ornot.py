#WAP to check whether the given data is multivalued or not

data = eval(input('ENTER DATA:'))

if type(data) in [list,str,tuple,set,dict]:
    print('Multi Value DT')