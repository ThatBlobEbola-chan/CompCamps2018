import os, pygame, math, random

from settings import Settings
from godjavin import godjavin
from button import Button

class Game():
	def __init__(self):
		self.background = pygame.image.load("images/bliss.jpg")
		self.enemy = None
		self.godjavins = [
			godjavin("GodJavin"),
			godjavin("Test")
		]
		random.shuffle(self.godjavins)

		self.font = pygame.font.SysFont('Haettenschweiler', 30)

		self.buttons = [
			Button(0, Settings.height - 50, 100, 50, "Bone"),
			Button(100, Settings.height - 50, 100, 50, "Bolt"),
		]

	def loop(self, screen):
		clock = pygame.time.Clock()

		if not self.enemy:
			self.enemy = self.godjavins.pop()
			self.text = self.font.render(self.enemy.name, False, (214, 255, 212))

		while True:
			delta_t = clock.tick(Settings.frameRate)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					return

			screen.fill((0, 0, 0))
			screen.blit(self.background, (0,0))

			self.enemy.health = 20

			screen.blit(self.enemy.img, (Settings.width - 800, 0))
			pygame.draw.rect(screen, (139, 0, 0), (Settings.width - 150, 150, 100, 10))
			pygame.draw.rect(screen, (0, 255, 0), (Settings.width - 150, 150, (self.enemy.health / 20) * 100, 10))
			screen.blit(self.text, (Settings.width - 150, 130))

			for button in self.buttons:
				pygame.draw.rect(screen, (0, 255, 0), (button.x, button.y, button.w, button.h))
				screen.blit(button.text, (button.x, button.y))

			pygame.display.flip()

	def quit(self):
		pass
