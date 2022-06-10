def response(hey_bob:str):
    hey_bob = hey_bob.strip()
    if hey_bob == "":
        return "Fine. Be that way!"  

    has_text = hey_bob.lower() != hey_bob.upper()
    yelling = (hey_bob == hey_bob.upper() and not hey_bob.isnumeric() and has_text)
    question = hey_bob[-1] == "?"
  
    if question:
        if yelling:
            return "Calm down, I know what I'm doing!"
        return "Sure."
    if yelling:
        return "Whoa, chill out!"
    return "Whatever."
