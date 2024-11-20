from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from Crypto.Random import get_random_bytes

# size of the key must be 64 bits (8 bytes)
# What if the key is not 8 bytes? Either ask user to enter 8 bytes
# input or use hashing (SHA) to make the key 8 bytes.
KEY = b'MYSECRET'

# DES would generate initialization vector (iv) automatically, if not defined
cipher = DES.new(KEY, DES.MODE_CBC)
print(cipher.iv)
print(cipher.block_size)

plain_text = 'This is a message'.encode()
print("plain_text::", plain_text)
padded_plain_text = pad(plain_text, DES.block_size)
print("padded_plain_text::", padded_plain_text)

cipher_text = cipher.encrypt(padded_plain_text)
print("encrypted::", cipher_text)

init_vector = cipher.iv

# same instance of the DES cannot be used to decrypt the encrypted
# message. Hence, new instance with same initialization vector
decrypt_cipher = DES.new(KEY, DES.MODE_CBC, init_vector)

decrypted = decrypt_cipher.decrypt(cipher_text)
decrypted = unpad(decrypted, DES.block_size)
print("decrypted::", decrypted.decode())

