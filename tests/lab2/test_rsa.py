import unittest
import os
import sys
parent_dir = os.path.abspath(os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")), ".."))
sys.path.append(parent_dir)

from src.lab2.rsa import is_prime, gcd, multiplicative_inverse, encrypt, decrypt


class TestRsaCipher(unittest.TestCase):

    def test_is_prime_rsa(self):
        self.assertEqual(is_prime(2), True)
        self.assertEqual(is_prime(11), True)
        self.assertEqual(is_prime(8), False)

    def test_gcd_rsa(self):
        self.assertEqual(gcd(12, 15), 3)
        self.assertEqual(gcd(3, 7), 1)

    def test_multiplicative_inverse_rsa(self):
        self.assertEqual(multiplicative_inverse(7, 40), 23)

if __name__ == '__main__':
    unittest.main()