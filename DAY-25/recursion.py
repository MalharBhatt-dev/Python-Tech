#RECURSION : It is a process of calling the function by itself until the termination condition becomes true.
#? SYNTAX :
# without return value:
#* def fname (args):
#*     if termination_cond:
#*         return
#?     fname(args) -->recursive call
#* fname(values)

#with return value:
#* def fname(args):
#*     if termination_cond:
#*         return
#?     return fname(args) -->recursive call
#* fname(fname(values))

# if we want to store the output then we have to use with return value syntax and in the case of if we just want to print the value then we have to use the syntax without return value.

#? steps to onvert any of the while loop program into recursion.
# step1: Initialization of all of the required variables of looping should be done  in function declaration.
# step2 : The termination condition should be written exactly opposite to the looping condition in the format of if statement.
# step3 : Return the total result inside the termination condition.
# step4 : Logic of the program should be kept as it is.
# step5 : Updation of the looping variable should be done in rrecursive call.
# 
#? sign | opposite sign
#   >   |   <=
#   <   |   >=
#   >=  |   <
#   <=  |   >
#   ==  |   !=
# 
#In termination condition the looping condition sign is considered opposite. 