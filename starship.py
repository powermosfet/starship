import pygame, sys
from pygame.locals import *

pygame.init()

size = [800,600]
screen = pygame.display.set_mode(size)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    pygame.display.flip()
