#in order to modify local variable inside the nest function we have to use a keyword 'non-local' inside the nested fucntion...

a=10
b=20
def demo():
    c= 30
    def demo_inside():
        nonlocal c
        global a,b
        c=40
        print(a,b,c)
    demo_inside()

demo()

#! all in while loop..


#wap to print fibonnaci series upto n.

