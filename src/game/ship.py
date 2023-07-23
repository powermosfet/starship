import pygame

class Ship:
    def __init__(self, pos):
        self.pos = pos
        self.firing = False

    def update(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.firing = True

            if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                self.firing = False

    def draw(self, screen):
        imageFile = "img/ship.png"
        if self.firing:
            imageFile = "img/ship-firing.png"
        image = pygame.image.load(imageFile)
        screen.blit(image, self.pos)

