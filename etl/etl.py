def transform(legacy_data:dict):
    new_data = {}
    for key, value in legacy_data.items():
        for elem in value:
            elem = elem.lower()
            new_data[elem] = key
    return new_data
