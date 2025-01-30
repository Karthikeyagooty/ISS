def create_playfair_matrix(key):
    key = key.upper().replace('J', 'I')
    key_chars = []
    seen = set()
    for c in key:
        if c.isalpha() and c not in seen:
            seen.add(c)
            key_chars.append(c)
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    remaining = [c for c in alphabet if c not in seen]
    matrix = key_chars + remaining
    matrix = matrix[:25]
    return [matrix[i*5:(i+1)*5] for i in range(5)]

def find_position(matrix, char):
    for row_idx, row in enumerate(matrix):
        if char in row:
            return (row_idx, row.index(char))
    raise ValueError(f"Character {char} not found in matrix.")

def playfair_encrypt(plaintext, key):
    matrix = create_playfair_matrix(key)
    plaintext = plaintext.upper().replace('J', 'I')
    plaintext = [c for c in plaintext if c.isalpha()]
    processed = []
    i = 0
    n = len(plaintext)
    while i < n:
        if i == n - 1:
            processed.append(plaintext[i])
            processed.append('X')
            i += 1
        else:
            a, b = plaintext[i], plaintext[i+1]
            if a == b:
                processed.append(a)
                processed.append('X')
                i += 1
            else:
                processed.append(a)
                processed.append(b)
                i += 2
    if len(processed) % 2 != 0:
        processed.append('X')
    ciphertext = []
    for i in range(0, len(processed), 2):
        a, b = processed[i], processed[i+1]
        a_row, a_col = find_position(matrix, a)
        b_row, b_col = find_position(matrix, b)
        if a_row == b_row:
            cipher_a = matrix[a_row][(a_col + 1) % 5]
            cipher_b = matrix[b_row][(b_col + 1) % 5]
        elif a_col == b_col:
            cipher_a = matrix[(a_row + 1) % 5][a_col]
            cipher_b = matrix[(b_row + 1) % 5][b_col]
        else:
            cipher_a = matrix[a_row][b_col]
            cipher_b = matrix[b_row][a_col]
        ciphertext.append(cipher_a)
        ciphertext.append(cipher_b)
    return ''.join(ciphertext)

def playfair_decrypt(ciphertext, key):
    matrix = create_playfair_matrix(key)
    ciphertext = ciphertext.upper().replace('J', 'I')
    ciphertext = [c for c in ciphertext if c.isalpha()]
    processed = []
    for i in range(0, len(ciphertext), 2):
        a, b = ciphertext[i], ciphertext[i+1]
        a_row, a_col = find_position(matrix, a)
        b_row, b_col = find_position(matrix, b)
        if a_row == b_row:
            plain_a = matrix[a_row][(a_col - 1) % 5]
            plain_b = matrix[b_row][(b_col - 1) % 5]
        elif a_col == b_col:
            plain_a = matrix[(a_row - 1) % 5][a_col]
            plain_b = matrix[(b_row - 1) % 5][b_col]
        else:
            plain_a = matrix[a_row][b_col]
            plain_b = matrix[b_row][a_col]
        processed.append(plain_a)
        processed.append(plain_b)
    return ''.join(processed)

# Get user inputs
key = input("Enter the encryption key: ").strip()
plaintext = input("Enter the plaintext: ").strip()

# Encrypt and decrypt
encrypted = playfair_encrypt(plaintext, key)
decrypted = playfair_decrypt(encrypted, key)

# Display results
print("\nEncrypted Text:", encrypted)
print("Decrypted Text:", decrypted)