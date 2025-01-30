def caesar_cipher(text, shift):
    shift %= 26
    result = []
    for char in text:
        if char.isupper():
            new_ord = (ord(char) - 65 + shift) % 26 + 65
            result.append(chr(new_ord))
        elif char.islower():
            new_ord = (ord(char) - 97 + shift) % 26 + 97
            result.append(chr(new_ord))
        else:
            result.append(char)
    return ''.join(result)

def encrypt(text, shift):
    return caesar_cipher(text, shift)

def decrypt(text, shift):
    return caesar_cipher(text, -shift)

# Example usage
if __name__ == "__main__":
    plaintext = "Hello, World!"
    shift = 3

    encrypted = encrypt(plaintext, shift)
    decrypted = decrypt(encrypted, shift)

    print("Original:", plaintext)
    print("Encrypted:", encrypted)
    print("Decrypted:", decrypted)