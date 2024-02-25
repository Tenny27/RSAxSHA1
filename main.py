import rsa
import hashlib



def sha1_hash(data):

  sha1_hasher = hashlib.sha1()
  sha1_hasher.update(data.encode())
  return sha1_hasher.hexdigest()


# Generate RSA key pair (not secure in real-world applications)
(public_key, private_key) = rsa.newkeys(2048)  # Adjust key size as needed

# Message to encrypt (not secure to send plain text)
message = str(input("Enter Message : "))
hash_value = sha1_hash(message)
print("SHA-1 hash:", hash_value)

# Encrypt message with public key (not secure)
encrypted_message = rsa.encrypt(message.encode(), public_key)

# Decrypt message with private key (not secure)
decrypted_message = rsa.decrypt(encrypted_message, private_key).decode()
hash_value2= sha1_hash(decrypted_message)

print("Original message:", message)
print("Encrypted message:", encrypted_message)
print("Decrypted message:", decrypted_message)
if hash_value==hash_value2:
    print("Verification Successfull.")
else:
    print("Verification Failed.")