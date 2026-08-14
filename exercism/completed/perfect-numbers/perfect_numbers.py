def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise  ValueError("Classification is only possible for positive integers.")
    sum_of_aliquote = 0
    for numb in range(1,number):
        if number % numb == 0:
            sum_of_aliquote += numb
    if  number == sum_of_aliquote:
        return "perfect"
    if  number < sum_of_aliquote:
        return "abundant"
    if  number > sum_of_aliquote:
        return "deficient"
    return None