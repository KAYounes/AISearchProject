class Node:
    def __init__(self, x, y):
        self.x = x
        self. y = y
        self.adjacent = []
    
    def insideNode(self, point, margin):
        return ((point[0] > (self.x - margin) and point[0] < (self.x + margin)) and ((point[1] > (self.y - margin) and point[1] < (self.y + margin))))

    