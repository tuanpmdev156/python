import string

AZ_LOWER = string.ascii_lowercase
ZA_LOWER = AZ_LOWER[::-1]
CIPHER_MAP = str.maketrans(AZ_LOWER,ZA_LOWER)


def encode(plain_text):
    """Cleans text, applies Atbash cipher, and groups into 5-character blocks."""
    # Keep only lowercase alphanumeric characters, removing all punctuation
    clean_text = ''.join(char.lower() for char in list(plain_text) if char.isalnum())
    # Translate the entire string instantly
    cipher_text = clean_text.translate(CIPHER_MAP)
    result = ' '.join(cipher_text[i : i + 5] for i in range(0, len(cipher_text), 5))
    return result


def decode(ciphered_text):
    """Removes spaces and decodes the Atbash cipher text."""
    ciphered_text = ciphered_text.replace(' ','').lower()
    return ciphered_text.translate(CIPHER_MAP)
    