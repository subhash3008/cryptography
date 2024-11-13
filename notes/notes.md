# Course Notes

### Cryptography
Way of talking securely between two persons in the presence of third

- Plain text:: doesn't need a key. human readable.
- Cipher text:: needs some kind of decryption to be readable, usually a key.
- Encryption:: process of encoding a message so that only authorized people can access it.
- Decryption:: process of decoding the message to read it 
- Key:: needed for both enryption and decryption

Thus, encryption/decryption is a function with message and key as parameters.

cipherText = f(message, key)

plainText = f(cipherText, key)


#### Symmetric Crypto Systems = Private Key Crypto Systems
- Uses only one key for both encryption and decryption.

Main disadvantage: private key must be exchanged. For a system with large number of users, it becomes an issue.

### Asymmetric Crypto Systems = Public Key Crypto Systems
- Uses public for encryption (to get cipherText) and private key for decryption(to get plainText)

Main advantage: private keys not to be exchanged, so no need to many keys.


## Symmetric Crypto System Algorithms
- Caesar Cipher

### Caesar Cipher
It is a symmetric crypto system. It is a substitution cipher i.e. each letter of plain text is shifted by a fixed number of places. Thus, the key is the value with which we shift the letters.

Each letter is assigned it's corresponding interger value between 0 and 25 or the ascii is used. When using the range 0 -25::

```C
E(x) = (x + n) % 26
D(x) = (x - n) % 26
```

Although it is simple to implement. The security is not top notch. As the number of letters are limited and encryption is proportional to the key and letters, it can be cracked with some difficulty. There are two approaches to achieve this:

- Brute force method - consider all the values in the key space and check if the plain text makes sense. Detecting valid english language helps here.
- Frequency analysis method - 








