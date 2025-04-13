import hashlib

# Input message
message = b"Karthikeya"

# Hashing with MD5
md5_hash = hashlib.md5(message).hexdigest()

# Hashing with SHA-1
sha1_hash = hashlib.sha1(message).hexdigest()

# Hashing with SHA-256
sha256_hash = hashlib.sha256(message).hexdigest()

# Hashing with SHA3-256
sha3_256_hash = hashlib.sha3_256(message).hexdigest()

# Display the results
print("Input Message:", message.decode())
print("\n--- Hash Values ---")
print("MD5        :", md5_hash)
print("SHA-1      :", sha1_hash)
print("SHA-256    :", sha256_hash)
print("SHA3-256   :", sha3_256_hash)
