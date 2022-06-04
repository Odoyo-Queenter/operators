#Create the following python classes inside shapes.py
#Class Circle
#It has a method area that returns the area (A) of the circle using the formula A=πr2
#It has a method to calculate circumference (c) using the formula C=2πr

class   Circle:
    def __init__(self,r):
        self.radius=r
    def area(self):
        area = 3.14*self.radius**2
        return area
    def perimeter(self):
        perimeter=3.14*2*self.radius
        return perimeter

Circle2=Circle(20)
print(Circle2.area())
print(Circle2.perimeter())        


# Class Square
# A Square instance accepts the attribute side (a)
# It has method area that returns the area (A) of the square using the formula A=a2
# It has a method to calculate the perimeter (P) of the square using the formula P=4a

class   Square:
    def __init__(self,a):
        self.width=a
    def area(self):
        area =self.width**2
        return area
    def perimeter(self):
        perimeter=self.width*4
        return perimeter

Square2=Square(50)
print(Square2.area())
print(Square2.perimeter()) 

# Class Rectangle
# A Rectangle instance accepts two sides of a rectangle (w,l)
# It has method to calculate the area (A) of the rectangle using the formula A=wl
# It has a method to calculate the perimeter (P) of the rectangle using the formula P=2(l+w)

class   Rectangle:
    def __init__(self,w,l):
        self.width=w
        self.length=l
    def area(self):
        area =self.width * self.length
        return area
    def perimeter(self):
        perimeter=2*self.length+self.width
        return perimeter

Rectangle2=Rectangle(40,20)
print(Rectangle2.area())
print(Rectangle2.perimeter()) 


# Class Sphere
# A Sphere Instance accepts the radius of the sphere (r)
# It has a method to calculate the surface area (A) using the formula A=4πr2
# It has a method to calculate the volume (V) of the sphere using the formula V = 4/3(πr3)

class   Sphere:
    def __init__(self,r):
        self.radius=r
    def area(self):
        area = 4*3.14*self.radius**2
        return area
    def perimeter(self):
        perimeter=4/3*self.radius**3
        return perimeter

Sphere2=Sphere(5)
print(Sphere2.area())
print(Sphere2.perimeter())
