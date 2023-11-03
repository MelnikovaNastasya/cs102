import unittest
import os
import sys
parent_dir = os.path.abspath(os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")), ".."))
sys.path.append(parent_dir)

from src.lab2.caesar import encrypt_caesar, decrypt_caesar


class TestCaesarCipher(unittest.TestCase):

    def test_encrypt_caesar(self):
        self.assertEqual(encrypt_caesar("HELLO"), 'KHOOR')
        self.assertEqual(encrypt_caesar("caesar"), 'fdhvdu')
        self.assertEqual(encrypt_caesar("Cipher1000-7"), 'Flskhu1000-7')
        self.assertEqual(encrypt_caesar(""), '')

    def test_decrypt_caesar(self):
        self.assertEqual(decrypt_caesar("KHOOR"), 'HELLO')
        self.assertEqual(decrypt_caesar("fdhvdu"), 'caesar')
        self.assertEqual(decrypt_caesar("Flskhu1000-7"), 'Cipher1000-7')
        self.assertEqual(decrypt_caesar(""), '')

if __name__ == '__main__':
    unittest.main()
