def sum_of_multiples(limit, multiples):
    levels = set()
    if multiples in ([],[0]):
        return 0
    for number in range(limit):
        for item in multiples:
            if item != 0 and number % item == 0:
                levels.add(number)
    return sum(levels)

    
