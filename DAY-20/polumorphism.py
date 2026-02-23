
#!poly means many.
#!morph means forms

#it is a process of allowing a method or operator to perform more than one type of functionality.
# in the case of addition operator it behaves in a different manner for single value data type and multi value data type.
#in the case of single value data type it will perform in general addition where as in the case of multi value data type it will perform concatenation.

#polymorphism can be achieved in python in 2 ways:
#  1.Method Overloading.
#  2.Operator Overloading.

#* 1.Method overloading : It is a phenomenon of allowing a method to perform more than one type of functionality.
#* Python doesnot support for methodOverloading.If we try to perform method overloading then also it will perform Mthod OverRiding.

#!Example  1:
def demo():
    return 'First demo'
def demo(a):
    return a,'Second demo'
def demo(a,b):
    return a,b,'third demo'
#print(demo())-->error
print(demo(1,2))

#!Example 2:
a=10
a=20
print(a)

#! Example 3:
class sample:

    @staticmethod
    def demo():
        return 'First demo'
    backup1 = demo
    @staticmethod
    def demo(a):
        return a,'Second demo'
    backup2 = demo
    @staticmethod
    def demo(a,b):
        return a,b,'third demo'
    
print(sample.backup1)
print(sample.backup2(1))
print(demo(1,2))


# !monkey_patching : it is process of storing address of the method in a variable so that using that variable we can execute that particular.
# difference method overloading and method overriding.:

# METHOD OVER LOADING:
# --Occurs in the same class 
# --In the case of method overloading , the method name is same but the arguments are different.

# Method Overriding:
# --method overriding occurs between two class (parent and child class).
# --In the case of method riding , The method name is same and arguments are also same.

#!Create a class animal which has a method sound . create 2 child classes dog and cat overriding the sound method of the parent class.
class animal:
    @staticmethod
    def sound():
        print('makes a sound.')

class dog(animal):
    @staticmethod
    def sound():
        print('barks')

class cat(animal):
    @staticmethod
    def sound():
        print('meow')

dog.sound()
cat.sound()
animal.sound()

#!Operator Overloadind : allowing an operator to work for objects of user-defined class is called as Operator Overloading.

#! Magic method / Dunder Method : In order to allow the operators to work for objects of user defined class , it is necessary to implement magic method.
#there is no need to call magic method explicitly.
# also remember that a magic method always start with __(double underscore) and ends with __ (double underscore)
#example __add__() is used to perform addition operation.
#__init__() is used to initialize object members.
