
#& Inheritance the properties from single parent class to multiple child classes is called as heirarchical level inheritance..
#* class pc :
#~ -------
#~ ---- CB
#~ -------
#! class cc1(pc):
#~ -------
#~ ---- CB
#~ -------
#! class cc2(pc):
#~ -------
#~ ---- CB
#~ -------
#~ |
#~ |
#~ |
#! class ccN(pc):
#~ -------
#~ ---- CB
#~ -------


#h Create class C,D,B which is inheriting the propereties from common class A along with that create properties for each class.

class Parent :
    surname = 'BHATT'
    address = 'AHMEDABAD'

class Son(Parent):
    name = 'Malhar'
    clg = 'indus'

class Daughter(Parent):
    name = 'Krisha'
    sch = 'DGS'

print(Son.surname)
print(Daughter.address) 

