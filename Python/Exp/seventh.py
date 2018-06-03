import math

print('---------------- OTHER MISC RESERVED WORDS ---------------')

# assert, async, await, class, continue, finally, in, lambda, None, raise, try, with, yield, 

x = None




print('---------------- FUNCTIONS THAT DO SIMPLE MATHEMATICAL ALGORITHMS ----------------')

def sumoflist(hi):
    sum = 0
    for i in range(len(hi)):
        sum = sum + hi[i]    
    return sum

print(sumoflist([1,3,3,5]))


def maxoflist(hi):
    max = 0
    for i in range(len(hi)):
        if hi[i] > hi[i-1]:
            max = hi[i]
    return max

print(maxoflist([1,342432,243923478]))
print(maxoflist([1,2,3,6,7,100,101]))


def inlist(number,thelist):
    for i in range(len(thelist)):
        if number == thelist[i]:
            isthere = True
        else:
            isthere = False
    return isthere

print(inlist(6,[1,2,3,4,6]))


def ceilinglol(number):
    return math.ceil(number)
'''
def ceilingreal(number):
    if (number - (number - 1) == )
'''
print(ceilinglol(3.4))

