import unittest
import number_theory_functions
from number_theory_functions import modular_exponent
from number_theory_functions import extended_gcd
from number_theory_functions import modular_inverse
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
    print("\n\nquesion 1")
    extended_gcd_result = extended_gcd(911, 7879)
    print(f'is 911, 7879 coprime? {extended_gcd_result[0] == 1}')
    print(f'911, 7879 linear combination: 1 = {extended_gcd_result[1]}*911 + {extended_gcd_result[2]}*7879')
    print(f'911, 7879 linear combination, multiplied: 1,000,000 = {1000000*extended_gcd_result[1]}*911 + {1000000*extended_gcd_result[2]}*7879')


    print("\n\nquestion 2")
    print(f'phi(1000): {400}')
    exponent_result = modular_exponent(7896543, 74365753, 400)
    print(f'7896543^74365753 mod 400: {exponent_result}')
    result = modular_exponent(456457, exponent_result, 1000)
    print(f'456457^{exponent_result} mod 1000 {result}')
    print(f'the hundreds number is {result//100}')


    print("\n\nquestion 3")
    rsa3 = RSA.generate_from_prime(3491, 3499, 3499)
    message = rsa3.decrypt(42)
    print(f"the decrypted msg={message}")
    print(f"the encrypted msg={rsa3.encrypt(message)}")

    print('\n\nquestion 4')
    extended_gcd_result = extended_gcd(984, 11)
    print(f'is 984, 11 coprime? {extended_gcd_result[0] == 1}')
    print(f'phi(991): {984}')
    print(f'd = {modular_inverse(11,984)}')


    print("\n\nquestion 5")
    rsa5 = RSA.generate_from_prime(7919, 6841, 4091)
    message = 25
    encrypted = rsa5.encrypt(message)
    print(f"the encrypted msg = {encrypted}")
    print(f"the decrypted msg = {rsa5.decrypt(encrypted)}")
    print(f"the public key used = {rsa5.public_key}")
    unittest.main()