from math import asin
from math import degrees

class Point:
    def __init__(self, x: float=0, y: float=0):
        self.x = x
        self.y = y
    def move(self, new_x: float, new_y: float):
        self.x = new_x
        self.y = new_y
    def reset(self):
        self.x = 0
        self.y = 0
    def compute_distance(self, point)-> float:
        distance = ((self.x - point.x)**2+(self.y - point.y)**2)**(0.5)
        return distance


class Line:
    def __init__(self, start: Point=0, end: Point=0):
        self.start = start
        self.end = end

    def compute_length(self):
        x_cathetus = self.end.x - self.start.x
        y_cathetus = self.end.y - self.start.y
        hypotenuse = ((x_cathetus ** 2) + (y_cathetus ** 2)) ** 0.5
        return hypotenuse

    def compute_slope(self):
        x_cathetus = self.end.x - self.start.x
        y_cathetus = self.end.y - self.start.y
        hypotenuse = self.compute_length()
        rad = asin(y_cathetus / hypotenuse)
        slope = degrees(rad)
        return abs(slope)

    def compute_horizontal_cross(self):
        if self.start.y > 0 and self.end.y > 0:
            return False
        if self.start.y < 0 and self.end.y < 0:
            return False
        else: return True

    def compute_vertical_cross(self):
        if self.start.x > 0 and self.end.x > 0:
            return False
        if self.start.x < 0 and self.end.x < 0:
            return False
        else: return True        



print("Example of a line")

st = list(map(float, input("Please write the x and y components of the start point:    "  "\n").split()))
en = list(map(float, input("Please write the x and y components of the end left corner point:    "  "\n").split()))

l = Line(start=Point(st[0], st[1]), end=Point(en[0], en[1]))


print(f"The line in the points:   {l.start.x}, {l.start.y}   y   {l.end.x}, {l.end.y}\n")
print(f"Length of the line:   {l.compute_length(): .3f}")
print(f"Slope of the line:   {l.compute_slope(): .3f}")
print(f"Intersection of the line with x axis:   {l.compute_horizontal_cross()}")
print(f"Intersection of the line with y axis:   {l.compute_horizontal_cross()}\n\n")
