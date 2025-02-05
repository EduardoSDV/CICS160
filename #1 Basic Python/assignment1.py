from math import sqrt
#Note that question states that the function recieves an integer > 1 therefore checking beforehand is not necessary.

def is_prime(positive_int):
    if positive_int == 1:
        return False  # 1 is not a prime number

    for i in range(2, int(sqrt(positive_int)) + 1):
        if positive_int % i == 0:
            return False

    return True

#print('is_prime(2)', is_prime(1))

def greatest_common_divisor(a, b):
    while b:
        a , b = b, a % b
    return a

def are_relatively_prime(int1 , int2):
    if greatest_common_divisor(int1, int2) == 1:
        return True
    else:
        return False

#print('are relatively_prime(48 , 17)', are_relatively_prime(48, 17))
#print('are relatively_prime(48 , 18)', are_relatively_prime(48, 18))

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

#print('primes(20)',primes(12))

def prime_decomposition(n):
    primes_list = primes(n)
    factors = []

    for p in primes_list:
        while n % p == 0:
            factors.append(p)
            n = n/p

    return factors

#print('prime_decomposition(20)',prime_decomposition(9))

'''
Task 5
Write a function called has_prime_decomposition_of_size_2_and_factors_are_different, that receives as input a positive integer, and returns true iff (that means if and only if)
the decomposition of its input into prime numbers has a length of exactly 2. For example, has_prime_decomposition_of_size_2_and_factors_are_different(21)
should return True, since 21 has 3 and 7 seven as its only prime factors. has_prime_decomposition_of_size_2_and_factors_are_different (9) should return False, since it decomposes
into the same prime number twice (namely, 3). has_prime_decomposition_of_size_2_and_factors_are_different(45) should return False, since its prime number decomposition includes two
unique prime numbers, but one of them (3) is included twice. has_prime_decomposition_of_size_2_and_factors_are_different(105) should return False, since, even though its prime factors
only appear once, it has three of them. has_ prime_decomposition_of_size_2_and_factors_are_different must make use of function prime_decomposition.

(20 points)
'''

def has_prime_decomposition_of_size_2_and_factors_are_different(n):
    factors = prime_decomposition(n)
    set_factors = set(factors)
    if len(factors) == 2 and len(set_factors) == 2:
        return True
    else:
        return False

#print('has_prime_decomposition_of_size_2_and_factors_are_different',has_prime_decomposition_of_size_2_and_factors_are_different(9))