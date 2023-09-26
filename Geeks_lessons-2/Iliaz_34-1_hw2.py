 print('HomeWork №2 Level: easy*\n')

 class Figure:
     unit = 'cm'
     def __init__(self):
         pass

     def calculate_area(self):
         pass

     def info(self):
         pass

 class Circle(Figure):
     def __init__(self, radius):
         super().__init__()
         self.__radius = radius
         if self.__radius < 0 :
             raise ValueError("radius must be more zero")


     def calculate_area(self):


         return 3.14 * self.__radius**2


     def info(self):
         print(f'Circle radius: {self.__radius}{self.unit},\n'
               f'Area: {self.calculate_area()}{self.unit}.\n')


 class RightTriangle(Figure):
     def __init__(self, side_a, side_b):
         super().__init__()
         self.__side_a = side_a
         self.__side_b = side_b
         if self.__side_a < 0 or self.__side_b < 0 :
             raise ValueError('side or sides must be more zero')

     def calculate_area(self):
         return self.__side_a* self.__side_b / 2

     def info(self):
         print(f'RightTriangle side a: {self.__side_a}{self.unit}, side b: {self.__side_b}{self.unit},\n'
               f'Area: {self.calculate_area()}{self.unit}.\n')


 circle1 = Circle(2)
 circle2 = Circle(7)
 triangle1 = RightTriangle(5, 8)
 triangle2 = RightTriangle(3, 7)
 triangle3 = RightTriangle(9, 12)

 figures_list = [circle1, circle2, triangle1, triangle2, triangle3]

 for figure in figures_list:
     figure.info()
