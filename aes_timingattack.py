from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import time
import numpy as np

# Generate a random 16-byte AES key
key = get_random_bytes(16)

# AES encryption function with artificial timing leak
def leaky_aes_encrypt(plaintext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    
    # Simulate timing leak: add time based on the value of the first byte of plaintext
    delay = plaintext[0] * 0.00001  # leak on first byte
    time.sleep(delay)
    
    start = time.time()
    ciphertext = cipher.encrypt(plaintext)
    end = time.time()
    
    return ciphertext, end - start
