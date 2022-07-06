def flatten(iterable, valid_items=None):
    if valid_items == None:
        valid_items = []
    for i in iterable:
        if i is None:
            pass
        if not isinstance(i, list):
            valid_items.append(i)
        elif isinstance(i, list):
            valid_items.extend(i)
    return valid_items