ALPHABET = ' ABCDEGHIJKLMNOPQRSTUVWXYZ'

KEY = 'ANIMAL'

def vignere_encrypt(plain_text, key):
  plain_text = plain_text.upper() # case insensitive
  key = key.upper() # case insensitive

  cipher_text = '' # return value
  key_idx = 0 # tracks the index of the letters in key

  for char in plain_text:
    char_idx = ALPHABET.find(char)  # get character index to encrypt
    updated_key_idx = ALPHABET.find(key[key_idx]) # get character index used to encrypt from key
    encrypted_idx = (char_idx + updated_key_idx) % len(ALPHABET) # encryption

    cipher_text += ALPHABET[encrypted_idx]  # add the encrypted letter to result

    # update the key_index
    key_idx += 1
    if (key_idx == len(key)):
      key_idx = 0
  
  return cipher_text

def vignere_decrypt(cipher_text, key):
  cipher_text = cipher_text.upper() # case insensitive
  key = key.upper() # case insensitive

  plain_text = '' # return value
  key_idx = 0 # tracks the index of the letters in key

  for char in cipher_text:
    idx = ALPHABET.find(char) # get the characted index
    updated_kex_idx = ALPHABET.find(key[key_idx]) # get character index used to decrypt from key
    decrypted_idx = (idx - updated_kex_idx) % len(ALPHABET)

    plain_text += ALPHABET[decrypted_idx]

    # update the key index
    key_idx += 1
    if key_idx == len(key):
      key_idx = 0
  
  return plain_text


if __name__ == '__main__':
  message = 'This is a message'
  encrypted = vignere_encrypt(message, KEY)
  decrypted = vignere_decrypt(encrypted, KEY)

  print('ENCRYPTED MESSAGE:: ', encrypted)
  print('DECRYPTED MESSAGE:: ', decrypted)


