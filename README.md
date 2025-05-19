# 🔐 Vigenère Cipher Attack Simulation

## 🌟 Overview

### 🟠 
With the advancement of digital security techniques, understanding the fundamentals of classical encryption has become essential. The Vigenère cipher, once considered unbreakable, represents a milestone in the history of symmetric cryptography. However, it can be broken using modern techniques such as frequency analysis and the calculation of the index of coincidence.

### 🧩 
This project was developed with two main objectives:
1. To create a complete system that allows the encryption and decryption of messages using the Vigenère cipher.
2. To simulate a real attack on Vigenère-encrypted messages, demonstrating its vulnerability—especially when applied to short messages or those with predictable patterns.

### ⚙️ 
- A `Vigenere` module was implemented to handle the logic of encryption and decryption using the cipher.
- A second module, `VigenereAttack`, was created to carry out the frequency analysis attack, with support for both Portuguese and English.
- The main interface (`main.py`) offers the user options to:
  - Encrypt a message
  - Decrypt a message
  - Simulate an attack without knowing the key
- Before analysis, the message is normalized by removing accents, symbols, and characters not present in the selected language.

### ✅ 
- The project clearly and effectively demonstrates the vulnerability of the Vigenère cipher.
- The user can interact with the system through the terminal and observe the cryptographic breaking process.
- The code is modular and can be easily extended to support other ciphers or attack techniques.
- Author: [https://github.com/Schatten900/]

---

## 🚀 How to run

```bash
git clone https://github.com/Schatten900/securityWork1.git
cd securityWork1
python main.py
