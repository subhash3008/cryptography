# alphabets to perform operations using indexes. includes space as well.
ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
KEY = 10

def caesar_encrypt(plain_text):
  cipher_text = ''
  # as we are only using uppercase in our alphabet variable
  plain_text = plain_text.upper()

  for char in plain_text:
    # get the index in the alphabet for char
    idx = ALPHABET.find(char)
    # perform the encryption i.e. index + key
    idx = (idx + KEY) % len(ALPHABET)
    # add the letter to the cipher text
    cipher_text += ALPHABET[idx]
  
  return cipher_text

def caesar_decrypt(cipher_text):
  plain_text = ''

  # as we are only having the uppercase in alphabet variable
  cipher_text = cipher_text.upper()

  for char in cipher_text:
    # get index
    idx = ALPHABET.find(char)
    # peform operation
    idx = (idx - KEY) % len(ALPHABET)
    # update plain text
    plain_text += ALPHABET[idx]
  
  return plain_text


if __name__ == '__main__':
  message = "SUBHASH CHANDRA"
  encrypted = caesar_encrypt(message)
  decrypted = caesar_decrypt(encrypted)
  print('Encrypted::', encrypted)
  print('Decrypted::', decrypted)