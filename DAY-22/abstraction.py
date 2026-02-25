#abstraction:
#It is a process of hiding the implementation from the user by allowing them for using the functionality only.

#concrete class:
#a class which doesnot consists of any of the abstract method is called as concrete class.

#abstract class:
#a class which consists of atleast one abstract method is called as abstract class.

#? from abc import ABC,abstractmethod

#where abc = abstract base classess
#      ABC = abstract class
#      abstractmethod = abstract method

#Abstract method : a method which as only fucntion declaration but not defination is called as abstract method.

#? class c_name:
#?    @abstractmethod
# ?   def m_name(args):
#  ?      pss

#creation of abstract class and anstrat method..:>
#*code

from abc import ABC,abstractmethod
class parent(ABC):
    @staticmethod
    def wakeup():
        print('I am from parent class')
    
    @abstractmethod
    def income():
        pass

class child(parent):
    @staticmethod
    def income():
        print('I only earn 20k.')

ob1 = child.wakeup()
c1 = child()

#create class vehicle which a abstract class and implements a abstract method that is type of vehicle inside itself also create 2 subclasses car and truck which implements the abract in their own way..

class vehicle(ABC):

    @abstractmethod
    def vehicle_type():
        pass

class car(vehicle):

    @staticmethod
    def vehicle_type():
        print('This is car.')

class truck(vehicle):

    @staticmethod
    def vehicle_type():
        print('This is truck.')

c1 = car()
c1.vehicle_type()

t1 = truck()
t1.vehicle_type()