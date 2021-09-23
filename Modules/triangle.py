from polygon import Polygon
  #Create Child Class (Triangle) from Parent Class(Polygon)
class Triangle(Polygon):
      def triangle_area(self):
         return (self.get_triangle_height() * self.get_triangle_width()) * 1/2