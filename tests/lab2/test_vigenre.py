import unittest
import random
import string
import os
import sys
parent_dir = os.path.abspath(os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")), ".."))
sys.path.append(parent_dir)

from src.lab2.vigenre import encrypt_vigenere, decrypt_vigenere

class TestVigenreCipher(unittest.TestCase):

    def test_randomized(self):
        kwlen = random.randint(4, 24)
        keyword = ''.join(random.choice(string.ascii_letters) for _ in range(kwlen))
        plaintext = ''.join(random.choice(string.ascii_letters + ' -,') for _ in range(64))
        ciphertext = encrypt_vigenere(plaintext, keyword)
        self.assertEqual(plaintext, decrypt_vigenere(ciphertext, keyword))

    # def test_encrypt_vigenre(self):
    #     self.assertEqual(encrypt_vigenere("PYTHON", "A"), 'PYTHON')
    #     self.assertEqual(encrypt_vigenere("python", 'a'), 'python')
    #     self.assertEqual(encrypt_vigenere("ATTACKATDAWN", "LEMON"), 'AQCATZDPPMTLJZ')

    # def test_decrypt_vigenre(self):
    #     self.assertEqual(decrypt_vigenere("PYTHON", 'A'), 'PYTHON')
    #     self.assertEqual(decrypt_vigenere("python", 'a'), 'python')
    #     self.assertEqual(decrypt_vigenere("LXFOPVEFRNHR", "Lemon"), 'ATTACKATDAWN')

if __name__ == '__main__':
    unittest.main()