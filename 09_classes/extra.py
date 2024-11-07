class box:
    def __init__(self, width, length):
        self.width = int(width)
        self.length = int(length)
    def area(self):
        boxArea = int(self.width)*int(self.width)
        print (boxArea)


areas = box(6, 9)
areas.area()

    