#! Encapsulation:
#* Encapsulation is a phenomenon of providing security to the data members by restricting their access outside the class.

#? Access Specifiers:
#* Members of the class which will inform the users whether they can be access outside the class or not.

#? Types:
#~ Public
#~ Protected
#~ Private

#& Public:
#* Members of the class that can be accesed and modify outside the class.
#todo--> By Default all the class members and object members are public.  

#& Protected:
#* The only difference between public and protected is syntax.
#? Syntax: _identifier

#& Private:
#* Data members which cannot be accessed and modified outside the class are called as private access specifiers.
#? Syntax: __identifier  

#* In the case of python we cannot access methods outside the class. 
#* In order to access and modify private members outside the class we can make use of getter and setter methods.
#* Getter method is used to access the private members whereas setter method is used to modify the private members. 

#! To access private object members:
#* objname.-classname__propertyname=new value

#! To access private class numbers:
#* cname._classname__propertyname=new value