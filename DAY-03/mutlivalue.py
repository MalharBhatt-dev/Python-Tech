
#! n = eval(input('ENTER MULTI VALUE :'))
#! if type(n) in [tuple, list, set, dict, str]:
#!     print('MULTI VALUE')
#!     print(len(n))

#& asdasd

#? n = int(input('ENTER THE NUMBER :'))
#? if n%2==0:
#?     print('EVEN')
#? else :
#?     print('ODD')


# IF THE STRING IS EQUAL TO REVERSED STRING THEN IT IS SAID TO BE PALINDROME
#? n = input('ENTER THE CHARACTER :')
#? if n == n[::-1]:
#?     print('PALINDROME')

# n = input('ENTER THE CHARACTER :')
# if n == reversed(n):
#     print('PALINDROME')

#? It is used to check whether the multiple conditions at a time.If the condition is true it will execute the block of code.
#! SYNTAX :
#* if condition1 : trb -> elif condition2 : tsb -> ... -> elif conditionn : trsb -> else fsb ...
#& EXAMPLE :
#& n = int(input('ENTER THE NUMBER :'))
#& if n>0 :
#&     print('POSITIVE')
#& elif n<0 :
#&     print('NEGATIVE')
#& else :
#&     print('ZERO')

#!wap to check if a given number is single digit or double digit or three digit or greater than that...._.->
#& n = int(input('ENTER THE NUMBER :'))
#& if n>=0 and n<=9 :
#&     print('SINGLE DIGIT')
#& elif n>=10 and n<=99 :
#&     print('DOUBLE DIGIT')
#& elif n>=100 and n<=999 :
#&     print('THREE DIGIT')
#& else :
#&     print('GREATER THAN THREE DIGIT')

#! wap to  check if the given character is uppercase or lowercase or digit or specialc character or negative number..->
n = input('ENTER THE CHARACTER :')
if n>='A' and n<='Z' :
    print('UPPERCASE')
elif n>='a' and n<='z' :
    print('LOWERCASE')
elif n>='0' and n<='9' :
    print('DIGIT')
elif n<'0' :
    print('NEGATIVE NUMBER')
else :
    print('SPECIAL CHARACTER')
