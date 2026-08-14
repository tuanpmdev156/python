def is_isogram(string):
    clean_list = ''.join(char.lower() for char in string if char.isalpha())
    return len(clean_list) == len(set(clean_list))
    
