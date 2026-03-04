"""
Filename: test_cypher.py
Author:   Ian Rodrigues Kmiliauskis (iankmiliauskis1604@gmail.com)
Created:  03-04-2026
Description: This script is just a unit test for the 
             encryption_algorithm.py python code
"""

import unittest
from encryption_algorithm import encrypt, decrypt

class TestTeamHexCipher(unittest.TestCase):

    def setUp(self):
        self.key = "12345678" # 64-bit key (8 bytes)
        self.plaintext = "HELLO TEAM"
        self.fixed_time = "03042026154856"

    def test_encryption_decryption_cycle(self):
        """Tests if decrypting an encrypted message returns the original."""
        ciphertext = encrypt(self.plaintext, self.key, self.fixed_time)
        decrypted_text = decrypt(ciphertext, self.key, self.fixed_time)
        self.assertEqual(self.plaintext, decrypted_text)

    def test_wrong_key_fails(self):
        """Tests that a wrong key does not produce the original plaintext."""
        ciphertext = encrypt(self.plaintext, self.key, self.fixed_time)
        wrong_key = "87654321"
        decrypted_text = decrypt(ciphertext, wrong_key, self.fixed_time)
        self.assertNotEqual(self.plaintext, decrypted_text)

    def test_empty_string(self):
        """Ensures the algorithm handles empty input gracefully."""
        ciphertext = encrypt("", self.key, self.fixed_time)
        self.assertEqual(decrypt(ciphertext, self.key, self.fixed_time), "")

if __name__ == '__main__':
    unittest.main()
