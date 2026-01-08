
#h wap to check if the numbe is by 3 and 5 print 'FIZZBUZZ
#h if divisible by only 3 print 'FIZZ'
#h if divisible by only 5 print 'BUZZ'

num = int(input('Enter the number:'))
if num % 3 == 0 and num % 5 == 0:
    print('FIZZBUZZ')
elif num % 3 == 0:
    print('FIZZ')
elif num % 5 == 0:
    print('BUZZ')
else:
    print('The number is not divisible by 3 and 5 both.')