from polygon import Polygon
#Create Child Class (Square) from Parent Class(Polygon)
class Square(Polygon):  # Inheriting the Polygon class
        def area(self):
            return self.get_height() * self.get_width()

