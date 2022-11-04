import random
import getpass

# Every possible symbol that can be encrypted/decrypted:
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
CIPHER_KEY = 'LMKJOHAPTDQNUFBSZRWEXVCGYI'

def encryptPassword(message):
    """Encrypt the message using the key."""
    return translateMessage(message, 'encrypt')

def decryptPassword(message):
    """Decrypt the message using the key."""
    return translateMessage(message, 'decrypt')

def translateMessage(message, mode):
    """Encrypt or decrypt the message using the key."""
    translated = ''
    charsA = LETTERS
    charsB = CIPHER_KEY
    if mode == 'decrypt':
        # For decrypting, we can use the same code as encrypting. We
        # just need to swap where the key and LETTERS strings are used.
        charsA, charsB = charsB, charsA

    # Loop through each symbol in the message:
    for symbol in message:
        if symbol.upper() in charsA:
            # Encrypt/decrypt the symbol:
            symIndex = charsA.find(symbol.upper())
            if symbol.isupper():
                translated += charsB[symIndex].upper()
            else:
                translated += charsB[symIndex].lower()
        else:
            # The symbol is not in LETTERS, just add it unchanged.
            translated += symbol

    return translated