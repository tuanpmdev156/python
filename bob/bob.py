def response(hey_bob):
    if not hey_bob.isupper() and hey_bob.strip().endswith("?"):  
        return "Sure."
    if hey_bob.isupper() and not hey_bob.endswith("?"):
        return "Whoa, chill out!"
    if hey_bob.upper().endswith("?"):
        return "Calm down, I know what I'm doing!"
    if hey_bob.isspace() or not hey_bob:
        return "Fine. Be that way!"
    return "Whatever."