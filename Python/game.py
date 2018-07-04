import os, pygame, math, random

from settings import Settings
from godjavin import godjavin

class Game():
	def __init__(self):
		self.background = pygame.image.load("images/bliss.jpg")
		self.enemy = None
		self.godjavins = [
			godjavin("GodJavin"),
			godjavin("Test")
		]
		random.shuffle(self.godjavins)

	def loop(self, screen):
		clock = pygame.time.Clock()

		if not self.enemy:
			self.enemy = self.godjavins.pop()

		while True:
			delta_t = clock.tick(Settings.frameRate)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					return

			screen.fill((0, 0, 0))
			screen.blit(self.background, (0,0))

			screen.blit(self.enemy.img, (Settings.width - 800, 0))

			pygame.display.flip()

	def quit(self):
		pass
