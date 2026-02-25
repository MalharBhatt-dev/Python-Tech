# types of arguments
#? positional arguments
#? defualt arguments
#? keyword arguments
#? variable length arguments

#~ Positional Arguments:
#* the arguments which are created in function declaration are called as Paoditional arguments.

#NOTE : It is compulsory to pass the value.
#NOTE : Follow the same order.

# def add(a,b):
#     print(a+b)
# add(10,20)

#* In the above example , a , b are positional arguments and passing value from them is compulsory.

#~ Default Arguments:
#* default arguments are present in the function declaration and if the user passes the value for default argument it will take that value but if the user doesnot pass the value it will take the default value.
#* In the case of default argument it should be always followed by positional arguments earlier.

# def info(name,m_num , mailid,alt_m_num=None):
#     print(name)
#     print(m_num)
#     print(mailid)
#     print(alt_m_num)

# info('yash',1234,'ayhs@gmail.com')
# info('de vansh',4567,'de vasnh@gmail.com',7896)

#~ Keyword Arguments:
#* passing the key-value pair as the value to the arguments.they are present in function call.

#Keyword argument:

# def pack(**d):
#     print(type(d))
#     print(d)
# pack(a=10,b='20',c=30,d='40')