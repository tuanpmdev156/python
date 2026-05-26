def is_pangram(sentence):
    """
    A pangram is a sentence using every letter of the alphabet at least once. 
    
    A sentence is a pangram if it contains each of the 26 letters in the English alphabet
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    sentence = sentence.lower()
    for char in alphabet:
        if char not in sentence:
            return False
    return True