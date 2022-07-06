def is_valid(isbn:str):
    isbn = isbn.replace("-","")
    if len(isbn) < 10:
        return False
    
    range_list = list(range(len(isbn),0,-1))
    temp_number = 0
    
    for i in range(len(isbn)):
        if isbn[i] == "X":
            pass
        elif isbn[i].isnumeric():
            temp_number += range_list[i] * int(isbn[i])
        else:
            return False

    if isbn[-1] == "X":
        temp_number += 10

    return temp_number % 11 == 0 and len(isbn) == 10