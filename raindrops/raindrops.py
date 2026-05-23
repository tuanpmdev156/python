def convert(number):
    result = ''
    items = [(3,'Pling'),(5,'Plang'),(7,'Plong')]
    for item in items:
        if number % item[0] == 0:
            result += item[1]
    if result == '': result = str(number)
    return result  