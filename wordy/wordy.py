import re
def answer(question): 
    
    default_operations = ['plus', 'minus', 'multiplied', 'divided']

    # Extract numbers & operations
    question = question[8:-1].split()
    # Remove all 'by' word
    question = [item for item in question if item != 'by']

    # if array has only numbers: return numbers
    if len(question) == 1:
        return int(question[0])
    if len(question) == 0:
        raise ValueError('syntax error')
    count_op = 0
    for operation in default_operations:
        if operation in question:
            count_op += 1
    # if array has numbers and does not has default_operations
    if count_op == 0:
        raise ValueError('unknown operation')
            
    # Extract all operations
    all_operations = []
    for element in question:
        if element in default_operations:
            all_operations.append(element)
    # Extract all numbers
    all_numbers = [int(x) for x in question if re.fullmatch(r'-?\d+', x)]

    # Check valid expression(every 2 numbers need 1 operation)
    if len(all_operations) != len(all_numbers) -1:
        raise ValueError('syntax error')
    
    # Check sequence of expression
    for index in range(0,len(question),2):
        # check if item at even indexies (0,2,4) is integer
        try:
            int(question[index])
        except ValueError as e:
            raise ValueError('syntax error') from e
    for index in range(1,len(question),2):
        # check if item at odd indexies (1,3,5) is not in default_operations
        if question[index] not in default_operations:
            raise ValueError('syntax error') 
    
    # Get first number
    result = int(all_numbers[0])
    # Exclude first number
    all_numbers = all_numbers[1:]
    # Loop to calculate
    for index,operation in enumerate(all_operations):
        if operation == 'plus':
            result += int(all_numbers[index])
        if  operation == 'minus':
            result -= int(all_numbers[index])
        if operation == 'multiplied':
            result *= int(all_numbers[index])
        if operation == 'divided':
            result /= int(all_numbers[index])
    return int(result)