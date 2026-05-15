def is_armstrong_number(number):
    """
    An Armstrong number is a number that is the total of its own digits each raised to the power of the number of digits.

    For example:

    >>> 9 is an Armstrong number, because 9 = 9^1 = 9
    10 is not an Armstrong number, because 10 != 1^2 + 0^2 = 1
    >>> 153 is an Armstrong number, because: 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
    >>> 154 is not an Armstrong number, because: 154 != 1^3 + 5^3 + 4^3 = 1 + 125 + 64 = 190
    """
    total = 0
    number_of_digit = len(str(number))
    for digit in str(number):
        total += int(digit)**number_of_digit
    if total == number:
        return True
    return False
