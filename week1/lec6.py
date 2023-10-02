# object oriented in python

class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

    def translate(self, deltax, deltay):
        self.x += deltax
        self.y += deltay

    def odistance(self):
        import math
        d = math.sqrt(self.x*self.x + self.y*self.y)
        return d
    
    def __str__(self):
        return ('(' + str(self.x)+','+str(self.y)+')')
    
    def __add__(self, p):
        return (Point(self.x + p.x, self.y + p.y))
    
