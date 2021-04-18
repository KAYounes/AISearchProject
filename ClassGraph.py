import Node

class Graph:
    def __init__(self, addMargin, deleteMargin):
        self.nodes = [] 
        self.addMargin = 95
        self.deleteMargin = 45 
        

    def addNode(self, point):
        for node in self.nodes:
            if (node.insideNode(point, self.addMargin)):


