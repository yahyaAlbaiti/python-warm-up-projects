from string import punctuation, digits, ascii_letters
from random import shuffle

chars = punctuation + digits + ascii_letters + " "
chars = list(chars)
key = chars.copy()
shuffle(key)

print(f"chars: {chars}\n")
print(f"key  : {key}\n")

encrypt_dict = dict(zip(chars, key))
decrypt_dict = dict(zip(key, chars))

# ENCRYPT
plain_text = input("enter your text to encrypt: ")
cipher_text = "".join(
    encrypt_dict[letter]
    for letter in plain_text
)

print(f"the oringinal text: {plain_text}")
print(f"the encrypted text: {cipher_text}")

# DECRYPT
cipher_text = input("enter your text to decrypt: ")
plain_text = "".join(
    decrypt_dict[letter]
    for letter in cipher_text
)

print(f"the Oringinal text: {cipher_text}")
print(f"the Decrypted text: {plain_text}")