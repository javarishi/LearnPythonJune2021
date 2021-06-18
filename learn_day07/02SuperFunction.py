class Rectangle:

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
        print("Rectangle initiated with ", self.length, self.breadth)

    def area(self):
        return self.length*self.breadth

class Square(Rectangle):

    def __init__(self, length):
        #Rectangle.__init__(self,length, length)
        super().__init__(length, length)
        print("Square Initiated")


sq = Square(4)
print("Area of square" , sq.area())