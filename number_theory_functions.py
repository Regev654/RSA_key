from random import randrange, randint


def generate_random_coprime(phi_n, max_digits=10):
    """

    Parameters
    ----------
    max_digits - the generated number max length
    number - the number we want the gen

    Returns
    -------
    generate random number that (generated, number) = 1
    """
    found = False
    number = 0
    while not found:
        i = randint(2, max_digits)
        number = generate_prime(i)
        found = extended_gcd(number, phi_n)[0] == 1

    return number


def extended_gcd(a, b):
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

        if a == 0:
            return (b, 0, 1)

        r = b % a
        (gcd, newA, newB) = helper(a, r)

        x = newB - (b // a) * newA
        y = newA

        return (gcd, x, y)

    gcd, x, y = helper(a, b)
    if switch:
        return (gcd, y, x)
    return (gcd, x, y)


def modular_inverse(a, n):
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
        return n + x if x <= 0 else x
    return None


def modular_exponent(base, exponent, modulu):
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

    mod_sum = 1
    binary_exponent = bin(exponent)
    current_index = 0
    last_index = 0
    last_calc = 0
    base = base % modulu
    for i in binary_exponent[-1:1:-1]:
        number = int(i)
        if number == 0:
            current_index += 1
            continue

        if last_calc == 0:
            last_calc = (base ** (2 ** current_index)) % modulu
        else:
            new_power = (2 ** current_index) // (2 ** last_index)
            last_calc = (last_calc ** new_power) % modulu

        last_index = current_index
        current_index += 1
        mod_sum = (last_calc * mod_sum) % modulu

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
    a = randrange(1, n)
    k = 0
    d = n - 1
    while d % 2 == 0:
        k = k + 1
        d = d // 2
    x = modular_exponent(a, d, n)
    if x == 1 or x == n - 1:
        return True
    for _ in range(k):
        x = (x * x) % n
        if x == 1:
            return False
        if x == n - 1:
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
        n = randrange(10 ** (digits - 1), 10 ** digits)
        if is_prime(n):
            return n
    return None
