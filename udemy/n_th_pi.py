'''
Input: n (numbers of decimal in pi you want to see)
output: The pi number with all the decimal points up to the n-th
'''
import math
#print(math.pi)
# From math.pi, 15 decimals are provided
n = int(input('How many digits of pi do you want to see? '))
while n > 15:
    n = int(input('Your choice exeeds number of digits. Please provide new choice with n <=15'))
#print(f'{math.pi}','.nf')

pi = math.pi
#print(float("{:.nf}".format(math.pi)))
print(pi)