import pygame, sys
from pygame.locals import *
from game.ship import Ship

pygame.init()

size = [800,600]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0, 0, 0))

ship = Ship([size[0] / 2, size[1] / 2])

while True:
    events = list(pygame.event.get())
    for event in events:
        if event.type == pygame.QUIT: sys.exit()

    ship.update(events)

    screen.blit(background, (0, 0))

    ship.draw(screen)

    pygame.display.flip()
    clock.tick(60)

