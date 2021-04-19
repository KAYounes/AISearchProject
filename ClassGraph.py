import pygame
from ClassNode import Node

class Graph:
    def __init__(self, surface, addMargin, deleteMargin):
        self.screen = surface
        self.addMargin = 95
        self.deleteMargin = 45 
        self.nodes = []
        self.edge = []
        self.edges = []
        self.adding = False
        

    def addNode(self, point):
        for node in self.nodes:
            if (node.insideNode(point, self.addMargin)):
                return
        
        self.nodes.append(Node(point[0], point[1]))
        self.adding = True

    def deleteNode(self, point):
        deleteIndices = []
        for idx, node in enumerate(self.nodes):
            if (node.insideNode(point, self.deleteMargin)):
                deleteIndices.append(idx)



        for index in deleteIndices:
            self.nodes.pop(index)

    def draw(self):
        for node in self.nodes:
            pygame.draw.circle(self.screen, node.color, (node.cord), node.radius, node.width)

        

        for edge in self.edges:
            pygame.draw.line(self.screen, node.color, edge[0], edge[1], 5)

    def addEdge(self, point):
        if (self.adding):
            self.adding = False
        else:
            for node in self.nodes:
                if (node.insideNode(point, self.addMargin)):
                    node.color = (255,0,0)
                    self.edge.append(node.cord)
                    if len(self.edge) == 2:
                        self.edges.append(self.edge)
                        self.edge = []

                    
            
                            
        
