from typing import List, Tuple


# Declare a point type annotation using a tuple of ints of [x, y]
Point = Tuple[int, int]


# Create a function designed to take in a list of Points
def print_points(points: List[Point]):
    for point in points:
        print("X:", point[0], "  Y:", point[1])


x1 : Point  = (4,5)
#x2 : Point = (3,4)
x2 = 4
 
print_points([x1,x2])
