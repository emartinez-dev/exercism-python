def commands(binary_str):
    positions = {
        4: "wink",
        3: "double blink",
        2: "close your eyes",
        1: "jump",
    }
    commands = []
    for i in range(1,len(binary_str)):
        if binary_str[i] == "1":
            commands.insert(0, positions[i])
    if binary_str[0] == "1":
        commands = commands[::-1]
    return commands