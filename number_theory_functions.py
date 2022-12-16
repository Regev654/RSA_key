from random import randrange

def extended_gcd(a,b):
    """
    Returns the extended gcd of a and b

    Parameters
    ----------
    a : Input data.
    b : Input data.
    Returns
    -------
    (d, x, y): d = gcd(a,b) = a*x + b*y
    """
    if a == 0 and b == 0:
        return 
    
    switch = False
    if a > b:
        temp = a
        a = b
        b = temp
        switch = True
            
    def helper(a, b):
        
        if a > b:
            temp = a
            a = b
            b = temp
            
        
        if a == 0 :
            return (b, 0, 1)
        
        r = b % a
        (gcd, newA, newB) = helper(a, r)
             
            
        x = newB - (b // a) * newA
        y = newA
        
        return (gcd, x, y)
    
    gcd, x, y = helper(a, b)
    if switch:
         return(gcd, y, x)
    return (gcd, x, y)

def modular_inverse(a,n):
    """
    Returns the inverse of a modulo n if one exists

    Parameters
    ----------
    a : Input data.
    n : Input data.

    Returns
    -------
    x: such that (a*x % n) == 1 and 0 <= x < n if one exists, else None
    """
    gcd_res = extended_gcd(a, n)
    if gcd_res[0] == 1:
        x = gcd_res[1]
        return n+x if x <= 0 else x
    return None


def modular_exponent(a, d, n):
    """
    Returns a to the power of d modulo n

    Parameters
    ----------
    a : The exponential's base.
    d : The exponential's exponent.
    n : The exponential's modulus.

    Returns
    -------
    b: such that b == (a**d) % n
    """
    power = 0
    temp = 0
    a_new = a%n
    mod_sum = 1
    binary_d = bin(d)
    print(binary_d)
    for i in binary_d[-1:1:-1]:
        number = int(i)
        mod_sum*=a_new**(number*2**power)%n
        mod_sum = mod_sum%n
        power += 1
    return mod_sum
def miller_rabin(n):
    """
    Checks the primality of n using the Miller-Rabin test

    Parameters
    ----------
    n : The number to check

    Returns
    -------
    b: If n is prime, b is guaranteed to be True.
    If n is not a prime, b has a 3/4 chance at least to be False
    """
    a = randrange(1,n)
    k = 0
    d = n-1
    while d % 2 == 0:
        k = k + 1
        d = d // 2
    x = modular_exponent(a, d, n)
    if x == 1 or x == n-1:
        return True
    for _ in range(k):
        x = (x * x) % n
        if x == 1:
            return False
        if x == n-1:
            return True
    return False

def is_prime(n):
    """
    Checks the primality of n

    Parameters
    ----------
    n : The number to check

    Returns
    -------
    b: If n is prime, b is guaranteed to be True.
    If n is not a prime, b has a chance of less than 1e-10 to be True
    """
    for _ in range(10):
        if not miller_rabin(n):
            return False
    return True

def generate_prime(digits):
    for i in range(digits * 10):
        n = randrange(10**(digits-1), 10**digits)
        if is_prime(n):
            return n
    return None

print("Test 984, 11")
print(extended_gcd(984, 11))
print("Test 11, 984")
print(extended_gcd(11, 984))