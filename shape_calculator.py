class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width
      
    def set_height(self, height):
        self.height = height
      
    def get_area(self):
        return self.width * self.height
      
    def get_perimeter(self):
        return (2 * self.width) + (2 * self.height)
      
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5
      
    def __repr__(self):
        return f'Rectangle(width={self.width}, height={self.height})'
    
    def get_picture(self):
        picture = ''
        if self.width <= 50 and self.height <= 50:
            for i in range(self.height):
                picture += ''.center(self.width, '*') + '\n'
            return picture
        else:
            return "Too big for picture."
        
    def get_amount_inside(self, shape):
        return self.get_area() // shape.get_area()



class Square(Rectangle):
    def __init__(self, side):
        Rectangle.__init__(self, side, side)
        
    def set_side(self, side):
        self.width = side
        self.height = side
        
    def __repr__(self):
        return f'Square(side={self.width})'
