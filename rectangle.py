class Point:
    definition: str = "Entidad geometrica abstracta que representa una ubicación en un espacio."
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


class Rectangle:                                       
    definition: str = "Entidad geometrica que representa la intersección de cuatro rectas, dos de ellas paralelas entre sí y perpendiculares a las dos restantes, las cuales son paralelas entre sí"  
    def __init__(self, width: float=0, height: float=0, bottom_left_corner: Point=0):                
        self.width = width                              
        self.height = height  
        self.bottom_left_corner = bottom_left_corner                          
    def compute_area(self):
        area = self.width * self.height
        print(f"The area of the rectangle is: {area}")
    def compute_perimeter(self):
        perimeter = (self.width * 2) + (self.height * 2)
        print(f"The perimeter of the rectangle is: {perimeter}")   
    def compute_interference_point(self, point: Point=0):
        x_total, y_total = self.width, self.height
        x_min, y_min = self.bottom_left_corner.x, self.bottom_left_corner.y 
        if (x_min <= point.x <= (x_min + x_total)) and (y_min <= point.y <= (y_min + y_total)): 
            print("The point is in the rectangle")
        else: print("The point is NOT in the rectangle")

class Square(Rectangle):
    definition: str = "Entidad geometrica que representa la intersección de cuatro rectas, un par de ellas paralelas entre sí y perpendiculares a las dos restantes, las cuales son paralelas entre sí, teniendo las cuatro la misma longitud" 
    def __init__(self, side_length, bottom_left_corner):
        super().__init__(width=side_length, height=side_length, bottom_left_corner=bottom_left_corner)    


option = int(input("If you know the bottom left corner point, width and height, please write 1"  "\n"  "If you know the central point, width and height, please write 2"  "\n"  "If you know the bottom left corner point, and the top right point, please write 3"  "\n\n"))

if option == 1:
    x_y_min = list(map(float, input("Please write the x and y components of the bottom left corner point:    "  "\n").split()))
    bottom_left_corner = Point(x= x_y_min[0], y= x_y_min[1])  

    dimension = list(map(float, input("Please write the width and height of the rectangle:    "  "\n").split()))
    width = dimension[0]
    height = dimension[1]

if option == 2:
    x_y_central = list(map(float, input("Please write the x and y components of the central point:    "  "\n").split()))
    x_central = x_y_central[0]
    y_central = x_y_central[1]

    dimension = list(map(float, input("Please write the width and height of the rectangle:    "  "\n").split()))
    width = dimension[0]
    height = dimension[1]

    bottom_left_corner_x = x_central - (width / 2)
    bottom_left_corner_y = y_central - (height / 2)
    bottom_left_corner = Point(x= bottom_left_corner_x, y= bottom_left_corner_y)

if option == 3:
    x_y_min = list(map(float, input("Please write the x and y components of the bottom left corner point:    "  "\n").split()))
    x_min = x_y_min[0]
    y_min = x_y_min[1]
    bottom_left_corner = Point(x= x_min, y= y_min) 

    x_y_max = list(map(float, input("Please write the x and y components of the top right corner point:    "  "\n").split()))
    x_max = x_y_max[0]
    y_max = x_y_max[1]

    width = x_max - x_min
    height = y_max - y_min
    
if option < 1 or option > 3:
    print("No valid number")

print("For the Rectangle") 

rectangle_1 = Rectangle(width=width, height=height, bottom_left_corner=bottom_left_corner)
rectangle_1.compute_area()
rectangle_1.compute_perimeter()


"""
print("\nFor the Square") 

square_1 = Square(side_length=width, bottom_left_corner=bottom_left_corner)
square_1.compute_area()
square_1.compute_perimeter()
"""

given_point = list(map(float, input("Please write the x and y components of the point to verify:    "  "\n\n").split()))
verify_point = Point(given_point[0], given_point[1])

rectangle_1.compute_interference_point(verify_point)