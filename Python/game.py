import os, pygame

from settings import Settings

class Game():
	def __init__(self):
		self.background = pygame.image.load("images/bliss.jpg")

		self.godjavins = [
			godjavin("GodJavin")
		]

	def loop(self, screen):
		clock = pygame.time.Clock()

		while True:
			delta_t = clock.tick(Settings.frameRate)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					return

			screen.fill((0, 0, 0))
			screen.blit(self.background, (0,0))

			pygame.display.flip()

	def quit(self):
		pass
