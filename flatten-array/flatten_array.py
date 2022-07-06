def flatten(iterable, valid_items=None):
    if valid_items == None:
        valid_items = []
    for i in iterable:
        if not isinstance(i, list) and i is not None:
            valid_items.append(i)
        elif isinstance(i, list):
            flatten(i, valid_items)
    return valid_items