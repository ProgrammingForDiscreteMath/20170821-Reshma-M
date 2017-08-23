from __future__ import division
import math

# Create a list with the first ten triangular numbers
# (see https://oeis.org/A000217)

L = [int((i*(i+1))/2) for i in range(1,11)]

# Create a function to test if a number is prime
def is_prime(n):
    """
    Test if ``n`` is a prime.
    """
    if n <= 1:
        return False
    if (n == 2 or n == 3):
        return True
        
    if (n%2 == 0 or n%3 == 0):
        return False
    
    i = 5
    j = 2
    
    while i <= math.sqrt(n):
        if n%i == 0:
            return False
        i += j
        j = 6 - j
    
    return True

# Tests
# is_prime(2033) == False
# is_prime(2039) == True

# Create a function which returns a list of the first ten prime numbers
# greater than or equal to n

def next_ten_primes(n):
    """
    Return the list of the first ten prime numbers greate than or equal to n

    
    """
    count = 0
    p = []
    num_check = n
    while count < 10:
        if is_prime(num_check) == True:
            count += 1
            p.append(num_check)
        num_check += 1
            
    return p

# Tests
# next_ten_primes(2033) == [2039, 2053, 2063, 2069, 2081, 2083, 2087, 2089, 2099, 2111]
# next_ten_primes(2039) == [2039, 2053, 2063, 2069, 2081, 2083, 2087, 2089, 2099, 2111]






