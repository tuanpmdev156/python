"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    """Take the given word and add the 'un' prefix."""
    prefix_un = 'un'
    return prefix_un + word
    
def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words."""
    seperate_char = ' :: ' + vocab_words[0]
    return seperate_char.join(vocab_words)
    
def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.

    Parameters:
        word (str): Word to remove suffix from.

    Returns:
        str: Word with suffix removed & spelling adjusted.

    Examples:
        >>> remove_suffix_ness('heaviness')
        'heavy'

        >>> remove_suffix_ness('sadness')
        'sad'

    """
    character_before_suffix_ness = word[-5]
    if character_before_suffix_ness == 'i':
        character_before_suffix_ness = 'y'
        result = word[:-5] + character_before_suffix_ness
        return result
    return word[:-4]
    
def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    Parameters:
        sentence (str): The word used in a sentence as an adjective.
        index (int): Index of the adjective to remove and transform.

    Returns:
        str: The extracted adjective in verb form.

    Examples:
        >>> adjective_to_verb('It got dark as the sun set.', 2)
        'darken'

        >>> adjective_to_verb('The ink stains her fingers black.', -1)
        'blacken'

    """
    suffix = 'en'
    splitted_sentence = sentence.split('.')
    sentence_without_dot = splitted_sentence[0]
    extracted_adjective = sentence_without_dot.split()[index]
    result = extracted_adjective + suffix
    return result
