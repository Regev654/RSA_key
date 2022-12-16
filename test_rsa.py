import unittest
import number_theory_functions
from number_theory_functions import modular_exponent
from rsa_functions import RSA

class TestNumberTheory(unittest.TestCase):
    def test_extended_gcd(self):
        values = [(119952, 34425, 153),
                 (428848, 123075, 547)
                 ]
        for (a,b,d) in values:
            (gcd,x,y) = number_theory_functions.extended_gcd(a,b)
            self.assertEqual(d, gcd)
            self.assertEqual(gcd, a*x+b*y)

    def test_modular_inverse(self):
        values = [(17,81),
                  (50,137)
                  ]
        for (a,n) in values:
            x = number_theory_functions.modular_inverse(a,n)
            self.assertEqual(1, (a * x) % n)
            self.assertEqual((x % n), x)

        self.assertIsNone(number_theory_functions.modular_inverse(119952,34425))

class TestRSA(unittest.TestCase):
    def test_encrypt_decrypt(self):
        rsa = RSA.generate(10)
        plaintexts = [123456789, 17, 9999, 102930]
        for M in plaintexts:
            C = rsa.encrypt(M)
            MM = rsa.decrypt(C)
            self.assertEqual(M,MM)

if __name__ == '__main__':
    print("question 3")
    rsa3 = RSA.generate_from_prime(3491, 3499, 3499)
    message = rsa3.decrypt(42)
    print(f"the decrypted msg={message}")
    print(f"the encrypted msg={rsa3.encrypt(message)}")

    print("question 5")
    rsa5 = RSA.generate_from_prime(7919, 6841)
    message = 25
    encrypted = rsa5.encrypt(message)
    print(f"the encrypted msg = {encrypted}")
    print(f"the decrypted msg = {rsa5.decrypt(encrypted)}")
    print(f"the public key used = {rsa5.public_key}")
    unittest.main()