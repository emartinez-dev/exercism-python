def answer(question):
    words = question.replace("?","").split(" ")
    commands = []
    
    # text parsing
    for word in words:
        try:
            commands.append(int(word))
        except:
            pass
        if word == "plus":
            commands.append("+")
        if word == "minus":
            commands.append("-")
        if word == "multiplied":
            commands.append("*")
        if word == "divided":
            commands.append("/")
        if word == "raised":
            commands.append("**")
        if word in ["cubed","Who","When","Why","How"]:
            commands.append("INVALID")

    # exception checking
    has_invalid = "INVALID" in commands
    has_opperators = any(opperand in commands for opperand in ["+","-","*","/","**"])
    
    n_opperands = 0
    for command in commands:
        if type(command) == int:
            n_opperands += 1
    
    if has_invalid:
        raise ValueError("unknown operation")
    if n_opperands == 1 and len(commands) == 1:
        return commands[0]
    if not has_opperators or n_opperands < 2:
        raise ValueError("syntax error")

    for command_pos in range(len(commands)):
        if commands[command_pos] in ["+","-","*","/","**"]:
            # if the items ahead and behind the operator are not opperands, error
            if type(commands[command_pos-1]) != int \
                or type(commands[command_pos+1]) != int:
                raise ValueError("syntax error")
        if command_pos < len(commands)-1:
            # if two opperands are consecutive, error
            if type(commands[command_pos]) == int \
                and type(commands[command_pos +1]) == int:
                raise ValueError("syntax error")

    # operations
    temp_result = 0
    first_opperand = True

    for command_pos in range(0, command_pos):
        if commands[command_pos] in ["+","-","*","/","**"]:
            opperand = commands[command_pos]

            if first_opperand:
                digit_1 = commands[command_pos-1]
                digit_2 = commands[command_pos+1]
                first_opperand = False
            else:
                digit_1 = temp_result
                digit_2 = commands[command_pos+1]

            if opperand == "+":
                temp_result = digit_1 + digit_2
            if opperand == "-":
                temp_result = digit_1 - digit_2
            if opperand == "*":
                temp_result = digit_1 * digit_2
            if opperand == "/":
                temp_result = digit_1 / digit_2
            if opperand == "**":
                temp_result = digit_1 ** digit_2
    
    return temp_result

print(answer("What is -3 plus 7 multiplied by -2?"))
