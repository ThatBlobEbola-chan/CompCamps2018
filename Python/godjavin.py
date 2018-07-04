import pygame

class godjavin:
    def __init__(self, name):
        self.name = name
        self.image = "images/" + self.name.lower() + ".png"
        self.img = pygame.image.load(self.image)
        self.img = pygame.transform.scale(self.img, (800, 600))
