from pygame import Vector2

class Node:
    def __init__(self, x, y, color = (255, 255, 255), radius = 50, width = 15):
        self.cord = Vector2(x,y)
        self.color = color
        self.radius = radius
        self.width = width
        self.adjacent = []
    
    def insideNode(self, point, margin):
        return ((point[0] > (self.cord.x - margin) and point[0] < (self.cord.x + margin)) and ((point[1] > (self.cord.y - margin) and point[1] < (self.cord.y + margin))))

    