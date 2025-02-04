from math import sqrt
#Note that question states that the function recieves an integer > 1 therefore checking beforehand is not necessary.

def is_prime(positive_int):
    for i in range(2, int(sqrt(positive_int)) + 1):
        if positive_int % i == 0:
            return False

    return True

print('is_prime(2)', is_prime(2))

def greatest_common_divisor(a, b):
    while b:
        a , b = b, a % b
    return a

def are_relatively_prime(int1 , int2):
    if greatest_common_divisor(int1, int2) == 1:
        return True
    else:
        return False

print('are relatively_prime(48 , 17)', are_relatively_prime(48, 17))
print('are relatively_prime(48 , 18)', are_relatively_prime(48, 18))

'''
from math import gcd
def are_relatively_prime(int1,int2):
    if gdc(int1 , int2) == 1:
        return True
    else:
        return False
'''
'''
def primes(int1):
    prime_check_list = []
    for i in range(2, int1 + 1):
        if i % 2 != 0 or i == 2:
            prime_check_list.append(i)
    for possible_prime in prime_check_list:
        if not is_prime(possible_prime):
            prime_check_list.remove(possible_prime)
    return prime_check_list
    
#This is heavily inneficient because first im adding everything except even numbers and 2 to the list and then removing them to get primes,
it is better to just store the prime number sin the list in the first pass.
'''
def primes(int1):
    prime_list = []
    for i in range(2 , int1 +1):
        if is_prime(i):
            prime_list.append(i)
    return prime_list

print('primes(20)',primes(12))

def prime_decomposition(int1):
    prime_list = primes(int1)
    return prime_list
print(prime_decomposition(10))








<<<<<<< HEAD
def is_prime(p_int):
    for i in range sqrt.(p_int)

=======
>>>>>>> 232ed018a53ca1b17d4601f41f9852ed51240f6a
    