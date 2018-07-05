import pygame

class Button:
    def __init__(self, x, y, w, h, text):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.font = pygame.font.SysFont('Haettenschweiler', 30)
        self.text = self.font.render(text, False, (214, 255, 212))
