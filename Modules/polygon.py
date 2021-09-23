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