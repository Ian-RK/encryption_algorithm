"""
Filename: test_cypher.py
Author:   Ian Rodrigues Kmiliauskis (iankmiliauskis1604@gmail.com)
Created:  03-04-2026
Description: This script is just a unit test for the 
             encryption_algorithm.py python code
"""

import unittest
# We import our functions from the main file
from encryption_algorithm import encrypt, decrypt

class TestTeamHexCipher(unittest.TestCase):

    def setUp(self):
        """This runs before every test to set up the data."""
        self.my_secret_key = "12345678" # Our 64-bit (8 character) key
        self.message = "SECRET123"
        # We use a fixed time so the 'Shift' is always the same for the test
        self.test_time = "03042026154856" 

    def test_full_cycle(self):
        """Check if encrypting then decrypting gives the original message back."""
        # 1. Encrypt the message
        encrypted_data = encrypt(self.message, self.my_secret_key, self.test_time)
        
        # 2. Decrypt it back
        decrypted_result = decrypt(encrypted_data, self.my_secret_key)
        
        # 3. Compare
        self.assertEqual(self.message, decrypted_result)

    def test_wrong_key_fails(self):
        """Check that a different key results in total gibberish."""
        encrypted_data = encrypt(self.message, self.my_secret_key, self.test_time)
        
        wrong_key = "87654321"
        decrypted_result = decrypt(encrypted_data, wrong_key)
        
        # The result should NOT be our original message
        self.assertNotEqual(self.message, decrypted_result)

    def test_time_sensitivity(self):
        """Check that the same message encrypted at different times looks different."""
        time_one = "03042026154801" # 01 seconds
        time_two = "03042026154802" # 02 seconds
        
        output_one = encrypt(self.message, self.my_secret_key, time_one)
        output_two = encrypt(self.message, self.my_secret_key, time_two)
        
        self.assertNotEqual(output_one, output_two)

if __name__ == '__main__':
    unittest.main()
    