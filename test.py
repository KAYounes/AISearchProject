
###> Imports
import pygame, sys, random
from pygame.constants import QUIT,KEYDOWN,K_UP, K_RIGHT, K_DOWN, K_LEFT, USEREVENT
from pygame import init, quit, Vector2

###> Setting up pygame
init()
pygame.mixer.pre_init(44100, -16, 2, 512) #! handles a lot of things. Used here to remove delay before sound plays
clock = pygame.time.Clock()

hor, ver = 1820, 980
pygame.display.set_caption("CAPTION")
# pygame.display.set_icon(pygame.image.load(""))
screen = pygame.display.set_mode((hor, ver))
nodes = []
rect = pygame.Rect(0,0,80,80)

def draw_nodes():
    for node in nodes:
        pygame.draw.circle(screen, (255, 255, 255), node, 50, 5)

def delete_node(mouse_pos):
    delete_index = []
    for i, node in enumerate(nodes):
        # print((mouse_pos[0], (node[0] - 50), mouse_pos[0], (node[0] + 50), node, mouse_pos))
        if (mouse_pos[0] > (node[0] - 40) and mouse_pos[0] < (node[0] + 40)):
            if (mouse_pos[1] > (node[1] - 40) and mouse_pos[1] < (node[1] + 40)):
                delete_index.append(i)

    for i in delete_index:
        # print(nodes, i)
        nodes.pop(i)

def add_node(mouse_pos):
    add = True
    for node in nodes: 
        # print(">>", node, mouse_pos, node[0] - 50, node[0] + 50)
        if ((mouse_pos[0] > (node[0] - 95) and mouse_pos[0] < (node[0] + 95)) and ((mouse_pos[1] > (node[1] - 95) and mouse_pos[1] < (node[1] + 95)))):
            # print(">>", node[0], mouse_pos[0], node[1] - 50, node[1] + 50)
            # print(">>", node[1], mouse_pos[1], node[1] - 50, node[1] + 50)
            print(">", "TRUE")
            add = False

    if (add):
        nodes.append(mouse_pos)
        add = False
    # print(nodes)

    if (len(nodes) == 0):
        nodes.append(mouse_pos)


#> Main Loop
#>
loop = True
while(loop):
    
    #$ Event Loop
    for event in pygame.event.get():        
        #$ QUIT event
        if (event.type == QUIT):
            loop = False

        if (event.type == pygame.MOUSEBUTTONDOWN):
            if (event.button == 1):
                add_node(pygame.mouse.get_pos())
                # print(nodes)

            if (event.button == 3):
                delete_node(pygame.mouse.get_pos())

    screen.fill((0,0,0))
    draw_nodes()
    #$ Update Display
    pygame.display.update()
    clock.tick(60)

quit()
sys.exit()


# {1: {2: {'weight': 5}}, 2: {3: {'weight': 1}, 4: {'weight': 5}}, 3: {4: {'weight': 10}}, 4: {5: {'weight': 10}}, 5: {}}