"""
in actual, the secrets module shall be used to generate the random numbers
The prng used from random module shall not be used in cryptograhy
"""
from random import randint

ALPHABET = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# provides an array of random numbers with same length as input text
def random_sequence(plain_text):
  random = []

  for _ in range(len(plain_text)):
    random.append(randint(0, len(ALPHABET) - 1))
  
  return random

# implements one time pad encryption
def encrypt(plain_text, key):
  plain_text = plain_text.upper()
  
  cipher_text = ''

  for index, char in enumerate(plain_text): # enumerate returns index + value at position
    key_index = key[index] # value with which the char needs to be shifted
    char_index = ALPHABET.find(char)

    cipher_index = (char_index + key_index) % len(ALPHABET)
    cipher_text += ALPHABET[cipher_index]
  
  return cipher_text

def decrypt(cipher_text, key):
  cipher_text = cipher_text.upper()

  plain_text = ''

  for index, char in enumerate(cipher_text):
    key_index = key[index]
    char_index = ALPHABET.find(char)

    plain_index = (char_index - key_index) % len(ALPHABET)
    plain_text += ALPHABET[plain_index]
  
  return plain_text


if __name__ == "__main__":
  message = "This is random text"
  key = random_sequence(message)
  encrypted = encrypt(message, key)
  print("encrypted::", encrypted)
  decrypted = decrypt(encrypted, key)
  print("decrypt", decrypted)