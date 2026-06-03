def is_paired(input_string):
    # Dictionary to match opening brackets and their closing
    brackets_pairs = {'(':')','[':']','{':'}'}
    # Keep only brackets in string
    brackets = ''.join(char for char in input_string if char in brackets_pairs or char in brackets_pairs.values())
    # Repeatly remove pair brackets
    while True:
        initial_length = len(brackets)
        for open_bracket, close_bracket in brackets_pairs.items():
            pairs = open_bracket + close_bracket
            brackets = brackets.replace(pairs,'')
        # Check if nothing else to remove
        if initial_length == len(brackets):
            break
    # Verify all chars are pair brackets
    return len(brackets) == 0