# the arguments which are present in function delaration and we can pass one to n number of arguments are called as variable arguments.
def pack(*t , **d):
    print(type(t))
    print(t)
    print(type(d))
    print(d)

pack(10,20,30,40,50,a=10,b=20,c=30,d=40)