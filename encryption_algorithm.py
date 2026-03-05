"""
Filename: encryption_algorithm.py
Author:   Ian Rodrigues Kmiliauskis (iankmiliauskis1604@gmail.com)
Created:  03-04-2026
Description: This script performs Encryption and 
			 Decryption based what the user wants
"""

import datetime

# The S-BOX is our "Secret Decoder Ring" for Step 3
# It provides 'Confusion' by swapping one character for another
S_BOX = {
    '0': 'f', '1': 'e', '2': 'd', '3': 'c', '4': 'b', '5': 'a', '6': '9', '7': '8',
    '8': '7', '9': '6', 'a': '5', 'b': '4', 'c': '3', 'd': '2', 'e': '1', 'f': '0'
}

# The Inverse S-BOX is for Decrypting (swapping them back)
INV_S_BOX = {}
for key in S_BOX:
    value = S_BOX[key]
    INV_S_BOX[value] = key

# Your team names as a constant string
# Ian Aaaron Jacob Austin Will 
TEAM_NAMES = "IANAARONJACOBAUSTINWILL"

def get_binary_from_text(text):
    """Converts standard text into a long string of 0s and 1s."""
    binary_result = ""
    for character in text:
        ascii_number = ord(character)
        bits = format(ascii_number, '08b')
        binary_result = binary_result + bits
    return binary_result

def get_text_from_binary(binary_string):
    """Converts a long string of 0s and 1s back into readable text."""
    text_result = ""
    # Process 8 bits at a time (one byte)
    for i in range(0, len(binary_string), 8):
        byte_chunk = binary_string[i : i + 8]
        ascii_value = int(byte_chunk, 2)
        character = chr(ascii_value)
        text_result = text_result + character
    return text_result

def encrypt(plaintext, user_key, manual_time=None):
    if plaintext == "":
        return ""

    # --- STEP 0: Prepare Time and Keys ---
    if manual_time is None:
        current_time = datetime.datetime.now()
        timestamp = current_time.strftime("%d%m%Y%H%M%S")
    else:
        timestamp = manual_time

    # Convert everything to binary strings
    plaintext_bin = get_binary_from_text(plaintext)
    user_key_bin = get_binary_from_text(user_key)
    team_names_bin = get_binary_from_text(TEAM_NAMES)
    
    full_key_stream = user_key_bin + team_names_bin

    # --- STEP 1: XOR (Mixing) ---
    # We mix the plaintext bits with our key bits
    xor_result = ""
    for i in range(len(plaintext_bin)):
        bit_from_text = plaintext_bin[i]
        # We use the modulo (%) operator to repeat the key if it's shorter than the text
        bit_from_key = full_key_stream[i % len(full_key_stream)]
        
        if bit_from_text == bit_from_key:
            xor_result = xor_result + "0"
        else:
            xor_result = xor_result + "1"

    # --- STEP 2: Circular Shift (Diffusion) ---
    # We look at the last two digits of the seconds to decide the shift
    seconds_string = timestamp[-2:]
    shift_amount = int(seconds_string) % 8
    
    # Move the bits to the left
    left_part = xor_result[shift_amount:]
    right_part = xor_result[:shift_amount]
    shifted_bin = left_part + right_part

    # --- STEP 3: S-Box Substitution (Confusion) ---
    # First, convert binary to a Hexadecimal number string
    integer_value = int(shifted_bin, 2)
    hex_string = hex(integer_value)
    # Remove the '0x' from the start
    clean_hex = hex_string[2:]
    
    final_output = ""
    for char in clean_hex:
        # Swap the hex character using our S_BOX table
        if char in S_BOX:
            substituted_char = S_BOX[char]
            final_output = final_output + substituted_char
        else:
            final_output = final_output + char

    # We return the timestamp and the secret data together
    return timestamp + "|" + final_output

def decrypt(cipher_package, user_key):
    if "|" not in cipher_package:
        return "Error: Invalid format"

    # Split the package back into the Time and the Encrypted Data
    parts = cipher_package.split("|")
    timestamp = parts[0]
    encrypted_hex = parts[1]

    # --- REVERSE STEP 3: Undo S-Box ---
    reversed_hex = ""
    for char in encrypted_hex:
        if char in INV_S_BOX:
            original_hex_char = INV_S_BOX[char]
            reversed_hex = reversed_hex + original_hex_char
        else:
            reversed_hex = reversed_hex + char

    # Convert Hex back to Binary
    integer_val = int(reversed_hex, 16)
    binary_str = bin(integer_val)[2:]
    # Make sure we have leading zeros so the length is correct (multiple of 8)
    padding_needed = (len(encrypted_hex) * 4)
    binary_str = binary_str.zfill(padding_needed)

    # --- REVERSE STEP 2: Undo Shift ---
    seconds_string = timestamp[-2:]
    shift_amount = int(seconds_string) % 8
    
    # To undo a left shift, we shift right (or shift by length - amount)
    # This is effectively moving the bits back to their original spots
    right_part = binary_str[-shift_amount:]
    left_part = binary_str[:-shift_amount]
    original_bin = right_part + left_part

    # --- REVERSE STEP 1: Undo XOR ---
    # XOR is its own inverse! Doing it again with the same key unlocks it.
    user_key_bin = get_binary_from_text(user_key)
    team_names_bin = get_binary_from_text(TEAM_NAMES)
    full_key_stream = user_key_bin + team_names_bin
    
    decrypted_bin = ""
    for i in range(len(original_bin)):
        bit_from_data = original_bin[i]
        bit_from_key = full_key_stream[i % len(full_key_stream)]
        
        if bit_from_data == bit_from_key:
            decrypted_bin = decrypted_bin + "0"
        else:
            decrypted_bin = decrypted_bin + "1"

    # Convert binary back to English characters
    final_text = get_text_from_binary(decrypted_bin)
    return final_text

# --- Simple Menu ---
print("--- Team Hex Cipher ---")
mode = input("Type 'E' to encrypt or 'D' to decrypt: ")
key = input("Enter your 8-character key: ")

if mode.upper() == 'E':
    msg = input("Enter message: ")
    result = encrypt(msg, key)
    print("Encrypted Result: " + result)
else:
    msg = input("Paste the Encrypted Result: ")
    result = decrypt(msg, key)
    print("Decrypted Message: " + result)
