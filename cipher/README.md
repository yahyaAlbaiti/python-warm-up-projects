# Cipher Encryption Project
## Description
- #### A simple Python substitution cipher that encrypts and decrypts text using a randomly generated key.

## Features
* Encrypt plain text
- Decrypt cipher text
- Randomly generates a unique key each time the program runs
- Uses dictionaries for fast character lookup

## Concepts Practiced
* **Python modules**: `string`, `random`
* **Data structures**: Lists, Dictionaries
* **Built-in functions**: `zip()`, `join()`
* **Module methods**: `random.shuffle()`
* **Optimization**: Generator expressions

## How It Works
1. **Character List:** A list containing all supportable characters is initialized.
2. **Key Generation:** A copy of the list is created and randomly rearranged using `random.shuffle()`.
3. **Dictionary Mapping:** Encryption and decryption dictionaries are built by mapping the original list to the shuffled list using `zip()`.
4. **Encryption:** Plain text is passed through the encryption dictionary to substitute each character with its paired key character.
5. **Decryption:** Cipher text is passed through the decryption dictionary to revert the substituted characters back to their original form.

## Example

```text
Original Text:
Hello World

Encrypted Text:
@7xk!9pW2#

Decrypted Text:
Hello World
```
## Notes
- #### A new encryption key is generated every time the program runs.
- #### Encrypted messages can only be decrypted using the same generated key.