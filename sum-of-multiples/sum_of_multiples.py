def sum_of_multiples(limit, multiples):
    elements = []
    for multiple in multiples:
        if multiple > 0:
            [elements.append(n) for n in range(multiple, limit, multiple)]
    return sum(set(sorted(elements)))
