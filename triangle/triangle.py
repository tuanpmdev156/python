def  triangle_inequality(sides):
    """Check is a triangle"""
    return (sides[0] + sides[1] + sides[2] > 0) and (sides[0] + sides[1] >= sides[2]) and (sides[2] + sides[0] >= sides[1]) and (sides[1] + sides[2] >= sides[0])

def equilateral(sides):
    return triangle_inequality(sides) and (sides[0] == sides[1] == sides[2])
    
def isosceles(sides):
    return triangle_inequality(sides) and (sides[0] == sides[1] or sides[1] == sides[2] or sides[2] == sides[0])

def scalene(sides):
    return triangle_inequality(sides) and (sides[0] != sides[1] and sides[1] != sides[2] and sides[2] != sides[0])
