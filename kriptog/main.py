import time
from aes_crypto import encrypt_file, decrypt_file

def menu():
    print("==== AES-256 File Encrypt/Decrypt ====")
    print("1. Encrypt File")
    print("2. Decrypt File")
    print("3. Exit")
    return input("Choose: ")

while True:
    choice = menu()

    if choice == "1":
        inp = input("Input file path: ")
        out = input("Output encrypted file path: ")
        pw = input("Password: ")

        start = time.time()
        encrypt_file(inp, out, pw)
        end = time.time()

        print(f"Encryption done! Time: {end - start:.4f} seconds")

    elif choice == "2":
        inp = input("Encrypted file path: ")
        out = input("Output decrypted file path: ")
        pw = input("Password: ")

        start = time.time()
        decrypt_file(inp, out, pw)
        end = time.time()

        print(f"Decryption done! Time: {end - start:.4f} seconds")

    else:
        break
