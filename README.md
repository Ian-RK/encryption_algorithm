# Encryption_Algorithm (64-Bit Custom Encryption)

## 📌 Project Overview
The **Encryption_Algorithm** is a custom-designed symmetric encryption algorithm developed as a cryptographic exercise. It uses a 64-bit key and a multi-layered approach to ensure data security through **Confusion** and **Diffusion**.

This project demonstrates **Test-Driven Development (TDD)** by including a comprehensive suite of unit tests to verify the integrity of the encryption and decryption cycles.

## 🛠 How the Algorithm Works
The encryption process follows a unique 3-step pipeline:

1.  **Bitwise XOR (Key Mixing):** The plaintext is converted to binary and XORed with a combination of the user-provided 64-bit key and a static "Team Name" string. This ensures the key space is unique to this implementation.
2.  **Temporal Circular Shift (Diffusion):** The algorithm captures a 14-digit timestamp at the moment of execution. The last two digits of the seconds are used to perform a circular bit-shift, ensuring that the same message encrypted at different times results in different ciphertexts.
3.  **S-Box Substitution (Confusion):** The shifted binary is converted to Hexadecimal and passed through a non-linear S-Box (Substitution Box) to break mathematical patterns and prevent linear cryptanalysis.

## 📁 File Structure
* `encryption_algorithm.py`: The main algorithm containing the encryption/decryption logic and a CLI menu.
* `test_cipher.py`: Unit tests using Python's `unittest` framework.
* `.gitignore`: Prevents temporary Python files from being uploaded.

## 🚀 Getting Started

### Prerequisites
* Python 3.x installed on your machine.
* VS Code (recommended).

### Running the Cipher
1. Open your terminal.
2. Run the main script:
   ```bash
   python encryption_algorithm.py