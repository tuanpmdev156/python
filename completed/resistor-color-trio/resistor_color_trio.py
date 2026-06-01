units = ['ohms','kiloohms', 'megaohms', 'gigaohms']


resistor_value = {
    'black': 0,
    'brown': 1,
    'red': 2,
    'orange': 3,
    'yellow': 4,
    'green': 5,
    'blue': 6,
    'violet': 7,
    'grey': 8,
    'white': 9
}


def label(colors):
    first_color = colors[0]
    second_color = colors[1]
    third_color = colors[2]
    raw_color_value = (resistor_value[first_color] * 10 + resistor_value[second_color]) * 10**resistor_value[third_color]
    index = 0
    if raw_color_value == 0:
        return '0 ohms'
    while raw_color_value % 1000 == 0:
        index += 1
        raw_color_value = raw_color_value // 1000    
    return str(raw_color_value) + ' ' + units[index]
    
