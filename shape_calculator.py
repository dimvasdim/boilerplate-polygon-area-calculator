class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height
    
    def get_area(self):
        area = self.width * self.height
        return area

    def get_perimeter(self):
        perimeter = 2 * self.width + 2 * self.height
        return perimeter

    def get_diagonal(self):
        diagonal = (self.width ** 2 + self.height ** 2) ** 0.5
        return diagonal

    def get_picture(self):
        picture = ""
        if self.width > 50 or self.height > 50:
            picture = "Too big for picture."
        else:
            for i in range(self.height):
                picture += self.width * "*" + "\n"
        return picture

    def get_amount_inside(self, shape):
        fit_width = self.width // shape.width
        fit_height = self.height // shape.height
        amount = fit_width * fit_height
        return amount

    def __str__(self):
        display = f"Rectangle(width={self.width}, height={self.height})"
        return display


class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side

    def set_side(self, side):
        self.set_width(side)
        self.set_height(side)

    def __str__(self):
        display = f"Square(side={self.width})"
        return display
