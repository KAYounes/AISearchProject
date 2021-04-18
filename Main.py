/
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

#> Main Loop
#>
loop = True
while(loop):
    
    #$ Event Loop
    for event in pygame.event.get():        
        #$ QUIT event
        if (event.type == QUIT):
            loop = False

    #$ Update Display
    pygame.display.update()
    clock.tick(60)

quit()
sys.exit()