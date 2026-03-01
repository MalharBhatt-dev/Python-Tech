#GLobal space :
#? the area present outside  the function is called as global space.

#LOCAL SPACE:
#? the area present inside teh function is called as local space.

#GLOBAL VARIABLE:
#? the variable which is declared inside the global space or main space is called as global variable.

a= 10#global variable
def demo():
    print('Hii')

a= 10 
b =20 
def demo():
    print(a+b)
    print(a,b)
demo()
a=40
b=50
print(a,b)


#we can access a global variable inside a method area (function) and also we can modify a global variable inside the global space.
#we cannot modify a global variable inside the method area.

a= 10
b=20
#~ without global decalaration
#!UnboundLocalError: cannot access local variable 'a' where it is not associated with a value
# def demo():
#     a =a + 10
#     print(a,b)
# demo()

#~ with global declaration.
def demo():
    global a
    a =a + 10
    print(a,b)
demo()#20 20

#   In order to modify a global variable inside the method area we have to use a keyword called as global..

a=10
b=20
def demo():
    a=3
    b=4
    print(a,b)
    print('function part done!!!')

    print(a,b)
    demo()
    print(a,b)