
#h combination of more than one type of inheritance  is called as hubrid inheritance.

class A :
    print('Class A') 
class B(A) :
    print('Class B') 
class C(A) :
    print('Class C') 
class D(B,C) :
    print('Class D')
O=D()
print(D.mro()) 


