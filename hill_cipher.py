def text_to_numbers(text):
    return [ord(c.upper()) - ord('A') for c in text if c.isalpha()]

def numbers_to_text(numbers):
    return ''.join([chr(n + ord('A')) for n in numbers])

def matrix_inverse(key_matrix):
    a, b = key_matrix[0]
    c, d = key_matrix[1]
    det = (a * d - b * c) % 26

    det_inv = None
    for i in range(26):
        if (det * i) % 26 == 1:
            det_inv = i
            break
    if det_inv is None:
        raise ValueError("Key matrix is not invertible modulo 26")

    adjugate = [[d, (-b) % 26], [(-c) % 26, a]]
    inverse = []
    for row in adjugate:
        inverse_row = [(det_inv * x) % 26 for x in row]
        inverse.append(inverse_row)
    return inverse

def hill_encrypt(plaintext, key_matrix):
    n = len(key_matrix)
    plaintext = ''.join(filter(str.isalpha, plaintext.upper()))
    if len(plaintext) % n != 0:
        pad_length = n - (len(plaintext) % n)
        plaintext += 'X' * pad_length
    numbers = text_to_numbers(plaintext)
    ciphertext_numbers = []
    for i in range(0, len(numbers), n):
        block = numbers[i:i+n]
        encrypted_block = [0] * n
        for row in range(n):
            total = 0
            for col in range(n):
                total += key_matrix[row][col] * block[col]
            encrypted_block[row] = total % 26
        ciphertext_numbers.extend(encrypted_block)
    return numbers_to_text(ciphertext_numbers)

def hill_decrypt(ciphertext, key_matrix):
    n = len(key_matrix)
    inverse_key = matrix_inverse(key_matrix)
    ciphertext = ''.join(filter(str.isalpha, ciphertext.upper()))
    numbers = text_to_numbers(ciphertext)
    plaintext_numbers = []
    for i in range(0, len(numbers), n):
        block = numbers[i:i+n]
        decrypted_block = [0] * n
        for row in range(n):
            total = 0
            for col in range(n):
                total += inverse_key[row][col] * block[col]
            decrypted_block[row] = total % 26
        plaintext_numbers.extend(decrypted_block)
    return numbers_to_text(plaintext_numbers)

# Get user input
def get_key_matrix():
    while True:
        try:
            key_input = input("Enter the 2x2 key matrix as 4 integers separated by spaces (e.g., '5 8 17 3'): ")
            key_values = list(map(int, key_input.split()))
            if len(key_values) != 4:
                raise ValueError("Exactly 4 integers required")
            return [key_values[:2], key_values[2:]]
        except ValueError as e:
            print(f"Invalid input: {e}. Try again.")

if __name__ == "__main__":
    # Get inputs
    key_matrix = get_key_matrix()
    plaintext = input("Enter plaintext: ").strip()

    # Encrypt
    try:
        encrypted = hill_encrypt(plaintext, key_matrix)
        print("\nEncrypted Text:", encrypted)
        
        # Decrypt (to verify)
        decrypted = hill_decrypt(encrypted, key_matrix)
        print("Decrypted Text:", decrypted)
    
    except ValueError as e:
        print(f"\nError: {e}. The key matrix is not valid for decryption.")