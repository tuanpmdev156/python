def find(search_list, value):
    original_list = search_list.copy()
    while len(search_list) > 0:
        middle_index = len(search_list) // 2
        middle_numb = search_list[middle_index]
        if value == middle_numb:
            return original_list.index(value)
        if value < middle_numb:
            search_list = search_list[:middle_index]
        if  value > middle_numb:
            search_list = search_list[middle_index+1:]
    raise ValueError("value not in array")