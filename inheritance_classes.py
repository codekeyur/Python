#Calculate area of Square and Triangle using the concept of Inheritance Class (here Polygon) in Python.
while(True):
 class Polygon:

     #Width and Height of Square
    __width = float(input("Please Enter the Width: "))
    __height = float((input("Please Enter the Height: ")))
    
    #Width and height of Triangle
    __triangleHeight = float((input("Please Enter the Triangle Height: ")))
    __triangleWidth = float(input("Please Enter the Triangle Width: "))

    def set_values(self, height, width):
        self.__height = height
        self.__width = width

    def get_height(self):
        return self.__height

    def get_width(self):
        return self.__width

    def set_triangle_values(self, triangleHeight, triangleWidth):
        self.__triangleHeight = triangleHeight
        self.__triangleWidth = triangleWidth

    def get_triangle_height(self):
        return self.__triangleHeight

    def get_triangle_width(self):
        return self.__triangleWidth
 
 #Create Child Class (Square) from Parent Class(Polygon)
 class Square(Polygon):  # Inheriting the Polygon class
        def area(self):
            return self.get_height() * self.get_width()

 #Create Object from Child class(Square)
 square = Square()
 print(square.area())
 print(f"Based on the Given Value the area of the square is {square.area()}")


 #Create Child Class (Triangle) from Parent Class(Polygon)
 class Triangle(Polygon):
     def triangle_area(self):
         return (self.get_triangle_height() * self.get_triangle_width()) * 1/2

#Create Object from Child class(Triangle)
 triangle = Triangle()
 print(triangle.triangle_area())
 print(f"Based on the given values area of the triangle is {triangle.triangle_ar