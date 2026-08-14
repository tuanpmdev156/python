
#step1:

# input: string + number

# output: string

# rules: depending on key -> shift the posisition of 26 characters
# key = 13
#Plain:  abcdefghijklmnopqrstuvwxyz
#Cipher: nopqrstuvwxyzabcdefghijklm

# hidden rules: 
# - chars not in alphabet don't need to convert
# - Case 1 chữ cái nhưng cả viết hoa và viết thường

def rotate(text, key):
    plain = 'abcdefghijklmnopqrstuvwxyz' 
    cipher = plain[key:] + plain[:key] 
     # Create translation table
    table = str.maketrans(plain + plain.upper(), cipher + cipher.upper())
    # Mapping characters
    return text.translate(table)