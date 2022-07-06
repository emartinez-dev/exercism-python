from calendar import c


def answer(question):
    words = question.replace("?","").split(" ")
    commands = []
    
    # text parsing
    for word in words:
        if word.isdigit():
            commands.append(int(word))
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

    # exception checking
    if commands == []:
        raise ValueError("unknown operation")
    for command_pos in range(len(commands)):
        if commands[command_pos] in ["+","-","*","/","**"]:
            if not isinstance(commands[command_pos-1],int) or not isinstance(commands[command_pos+1],int):
                raise ValueError("syntax error")

    # operations
    if len(commands) == 1:
        return commands[0]

    return commands

print(answer("What is 7 raised 4"))
