def is_valid(isbn):
    # Check empty string
    if not isbn:
        return False
    # Remove all dashes & transform into array
    isbn_arr = list(isbn.replace('-',''))
    # Check array must contains percisely 10 elements
    if len(isbn_arr) != 10:
        return False
    # Check array contains only numbers & 'X'
    valid_isbn_arr = []
    for element in isbn_arr:
        try:
            number = int(element)
        except ValueError:
            if isbn_arr.index(element) != 9 or element != 'X':
                return False
            number = 10
        valid_isbn_arr.append(number)

    # Check correct isbn
    result = valid_isbn_arr[0] * 10 + valid_isbn_arr[1] * 9 + valid_isbn_arr[2] * 8 + valid_isbn_arr[3] * 7 + valid_isbn_arr[4] * 6 + valid_isbn_arr[5] * 5 + valid_isbn_arr[6] * 4 + valid_isbn_arr[7] * 3 + valid_isbn_arr[8] * 2 + valid_isbn_arr[9] * 1

    if result % 11 == 0:
        return True
    return False