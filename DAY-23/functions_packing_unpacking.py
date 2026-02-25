#? packing function: It is a phenomenon of grouping the individuals values in the form of collections to provide security.
#*type:
#Tuple/Single packing
#Dictionary/Double packing

#?sigle packing / tuple packing:::
#It is phenomenon of grouping the individual values in the form of tupple collection to provide seurity..

#! Syntax:
# def fname(*args):
#     fanme(val1,val2,val3,...valn)
#?example :
# def pack(*args):
#     print(type(args))
#     print(args)
# pack(10,20,30,40,50)

#? Double packinf / Dictionary packing:
#It is a phenomenon of grouping the individual key-value pair in the form of dictionary to provide security.
#! syntax:
# def fname(**kwargs):
#     fname(k1=v1,k2=v2,..,kn=vn)

# def dictpacking(**kwargs):
#     return kwargs
# print(dictpacking(a1=15,b1=20))

#NOTE : Key should follow rules of identifiers.
#NOTE : Key should be of string data type only.
#NOTE : Key shouldn't enclose with quotes but values must be enclosed with quotes if it is string.


#! UNPACKING :
# the phenomenon of dividing the collection and storing each and every value present in the collection to a unique variable.
#! syntax:
# def fname(var1,var2,..,varn):
#     SB
#     fname(*collection)

#? def unpack(a,b,c):
#?    print(a,b,c)

#(unpack(*'Hii'))
#? H i i
#(unpack(*[12,34,5]))
#? 12 34 5
#(unpack(*{12,34,5}))
#? 34 12 5
#(unpack(*{'a':12,'b':34,'c':5}))
#? a b c
