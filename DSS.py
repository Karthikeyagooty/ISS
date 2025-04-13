from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import utils
from cryptography.exceptions import InvalidSignature
private_key = dsa.generate_private_key(key_size=1024)
public_key = private_key.public_key()

# Step 2: Message to be signed
message = b"Karthikeya"

# Step 3: Hash the message using SHA-1
hasher = hashes.Hash(hashes.SHA1())
hasher.update(message)
digest = hasher.finalize()

# Step 4: Sign the digest
signature = private_key.sign(
    message,
    hashes.SHA1()
)

print("Message:", message.decode())
print("Signature:", signature.hex())

# Step 5: Verify the signature
try:
    public_key.verify(
        signature,
        message,
        hashes.SHA1()
    )
    print("✅ Signature is valid!")
except InvalidSignature:
    print("❌ Signature is invalid!")
