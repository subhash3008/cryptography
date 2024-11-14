import matplotlib.pylab as plot

# alphabets to perform operations using indexes. includes space as well.
ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ' # for enncryption and decryption
ENGLISH_WORDS = []


def get_words_data():
  dictionary = open('../../resources/words.txt', 'r')

  for word in dictionary.read().split('\n'):
    # print(word)
    ENGLISH_WORDS.append(word.upper())

  dictionary.close()

  print(f"Length of words::{len(ENGLISH_WORDS)}")

# counts how many words in message are english words
def count_words(message):
  message = message.upper() # convert the sentence to uppercase
  words = message.split(' ') # get words from the message
  matches = 0 # get the number of english word matches

  # loop over the words and check how many matches we got in english dictionary
  for word in words:
    if word in ENGLISH_WORDS:
      matches += 1
  
  return matches

# decide if a message is english or not
def is_text_english(message):
  matches = count_words(message)

  # if 80% of words are english, then it is english
  if ((float(matches) / len(message.split(' '))) * 100) >= 80.0:
    return True
  else:
    return False



def frequency_analysis(message):
  # count the number of letters
  message = message.upper()

  # dictionary to store the letter frequency
  letter_frequency = {}

  # initialize letter frequency
  for letter in ALPHABET:
    letter_frequency[letter] = 0

  for letter in message:
    if letter in ALPHABET:
      letter_frequency[letter] += 1
  
  return letter_frequency

def plot_distribution(frequencies):
  plot.bar(frequencies.keys(), frequencies.values())
  plot.show()


# encrypts the plain text based on provided key
def caesar_encrypt(plain_text, key = 10):
  cipher_text = ''
  # as we are only using uppercase in our alphabet variable
  plain_text = plain_text.upper()

  for char in plain_text:
    # get the index in the alphabet for char
    idx = ALPHABET.find(char)
    # perform the encryption i.e. index + key
    idx = (idx + key) % len(ALPHABET)
    # add the letter to the cipher text
    cipher_text += ALPHABET[idx]
  
  return cipher_text


# decrypts the cipher text based on provided key
def caesar_decrypt(cipher_text, key = 10):
  plain_text = ''

  # as we are only having the uppercase in alphabet variable
  cipher_text = cipher_text.upper()

  for char in cipher_text:
    # get index
    idx = ALPHABET.find(char)
    # peform operation
    idx = (idx - key) % len(ALPHABET)
    # update plain text
    plain_text += ALPHABET[idx]
  
  return plain_text


# decrypts the cipher text without key - bruteforce
def crack_caesar_brute(cipher_text):
  cipher_text = cipher_text.upper()
  # consider all possibilities of key and decrypt
  for key in range(len(ALPHABET)):
    plain_text = ''

    for char in cipher_text:
      idx = ALPHABET.find(char)
      idx = (idx - key) % len(ALPHABET)
      plain_text += ALPHABET[idx]

    if is_text_english(plain_text):
      print(f'Key: {key}, Plain Text: {plain_text}')

# decrypts the cipher text without key - frequency analysis
def crck_caesar_frequeny(cipher_text):
  freq = frequency_analysis(cipher_text)
  # print(freq)
  # plot_distribution(freq)
  freq = sorted(freq.items(), key= lambda x: x[1], reverse=True)
  # print(freq)
  print(f"Possible key:: {ALPHABET.find(freq[1][0]) - ALPHABET.find('E')}")





if __name__ == '__main__':
  get_words_data()
  message = "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using Content here, content here, making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like). There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc"
  encrypted = caesar_encrypt(message, 3)
  # decrypted = caesar_decrypt(encrypted)
  print('Encrypted::', encrypted)
  # print('Decrypted::', decrypted)

  print('Now cracking the algorithm with Brute Force method::')
  crack_caesar_brute(encrypted)

  # plot_distribution(frequency_analysis(plot_message))

  # crck_caesar_frequeny(encrypted)

  # print(is_text_english(message))

