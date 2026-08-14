def score(x, y):
    # Inside circle
    # (x - center_x)² + (y - center_y)² < radius²

    # On circle
    # (x - center_x)² + (y - center_y)² == radius²

    # Outside circle
    # (x - center_x)² + (y - center_y)² > radius²
    
    #center = (0,0)
    
    if pow(x, 2) + pow(y, 2) <= pow(1, 2):
        return 10
    if pow(1, 2) < pow(x, 2) + pow(y, 2) <= pow(5,2):
        return 5
    if pow(5,2) < pow(x, 2) + pow(y, 2) <= pow(10,2):
        return 1
    if pow(x, 2) + pow(y, 2) > pow(10, 2):
        return 0
    return None