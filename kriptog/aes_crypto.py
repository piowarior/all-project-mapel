import os
import hashlib
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding

# ---- KEY DERIVATION ----
def derive_key(password: str) -> bytes:
    return hashlib.sha256(password.encode()).digest()  # 32 byte

# ---- ENCRYPT ----
def encrypt_file(input_path, output_path, password):
    key = derive_key(password)
    iv = os.urandom(16)

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    encryptor = cipher.encryptor()

    with open(input_path, "rb") as f:
        data = f.read()

    # Padding PKCS7
    padder = padding.PKCS7(128).padder()
    padded = padder.update(data) + padder.finalize()

    ciphertext = encryptor.update(padded) + encryptor.finalize()

    # Save IV + ciphertext
    with open(output_path, "wb") as f:
        f.write(iv + ciphertext)

# ---- DECRYPT ----
def decrypt_file(input_path, output_path, password):
    key = derive_key(password)

    with open(input_path, "rb") as f:
        filedata = f.read()

    iv = filedata[:16]
    ciphertext = filedata[16:]

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    decryptor = cipher.decryptor()

    padded = decryptor.update(ciphertext) + decryptor.finalize()

    # Remove padding
    unpadder = padding.PKCS7(128).unpadder()
    data = unpadder.update(padded) + unpadder.finalize()

    with open(output_path, "wb") as f:
        f.write(data)
