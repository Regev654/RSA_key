from _ast import Expr

from number_theory_functions import generate_prime, generate_random_coprime, modular_inverse, modular_exponent
from random import random

N_INDEX = 0
E_INDEX = 1
D_INDEX = 1

class RSA():
    def __init__(self, public_key, private_key=None):
        self.public_key = public_key
        self.private_key = private_key

    @staticmethod
    def generate(digits=10):
        """
        Creates an RSA encryption system object

        Parameters
        ----------
        digits : The number of digits N should have

        Returns
        -------
        RSA: The RSA system containing:
        * The public key (N,e)
        * The private key (N,d)
        """
        q = generate_prime(digits)
        p = generate_prime(digits)
        n = q * p
        phi_n = (q - 1) * (p - 1)

        e = generate_random_coprime(phi_n, digits)
        d = modular_inverse(e, phi_n)
        return RSA((n, e), (n, d))

    def encrypt(self, m):
        """
        Encrypts the plaintext m using the RSA system

        Parameters
        ----------
        m : The plaintext to encrypt

        Returns
        -------
        c : The encrypted ciphertext
        """
        return modular_exponent(m, self.public_key[E_INDEX], self.public_key[N_INDEX])

    def decrypt(self, c):
        """
        Decrypts the ciphertext c using the RSA system

        Parameters
        ----------
        c : The ciphertext to decrypt

        Returns
        -------
        m : The decrypted plaintext
       """
        return modular_exponent(c, self.private_key[D_INDEX], self.private_key[N_INDEX])

