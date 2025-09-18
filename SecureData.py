import hashlib
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

# --- Step 1: User input ---
message = input("Enter a message: ").encode()

# --- Step 2: Hash input with SHA-256 ---
original_hash = hashlib.sha256(message).hexdigest()
print(f"Original SHA-256 Hash: {original_hash}")

# --- Step 3: AES Key & IV Generation (256-bit key, 128-bit IV) ---
key = os.urandom(32)  
iv = os.urandom(16)   

# --- Step 4: Encrypt ---
cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
encryptor = cipher.encryptor()
ciphertext = encryptor.update(message) + encryptor.finalize()
print(f"Encrypted message (hex): {ciphertext.hex()}")

# --- Step 5: Decrypt ---
decryptor = cipher.decryptor()
decrypted_message = decryptor.update(ciphertext) + decryptor.finalize()
print(f"Decrypted message: {decrypted_message.decode()}")

# --- Step 6: Verify Integrity ---
decrypted_hash = hashlib.sha256(decrypted_message).hexdigest()
print(f"Decrypted SHA-256 Hash: {decrypted_hash}")

if decrypted_hash == original_hash:
    print(" Integrity Verified: Hashes match")
else:
    print("Integrity Failed: Hashes do not match")
