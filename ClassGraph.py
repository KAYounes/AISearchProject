import pygame
from ClassNode import Node

class Graph:
    def __init__(self, surface, addMargin, deleteMargin):
        self.screen = surface
        self.addMargin = 95
        self.deleteMargin = 45 
        self.nodes = [] 
        

    def addNode(self, point):
        for node in self.nodes:
            if (node.insideNode(point, self.addMargin)):
                return
        
        self.nodes.append(Node(point[0], point[1]))

    def draw(self):
        for node in self.nodes:
            pygame.draw.circle(self.screen, node.color, (node.cord), node.radius, node.width)

