import sys

import pygame

pygame.init()

def main():
	# Setup screen and screen color
	screen = pygame.display.set_mode(1360, 700)
	screen.fill(230,230,230)
	pygame.display.set_caption("Rocket")
	
	# Load rocket and get rect
	image = pygame.image.load("images/ship.bmp")
	rect = image.get_rect
	
	while True:
		check_events()
		# Draw image on screen
		pygame.blit(image, rect)
	
def check_events():
	"""Listens for keyboard events and move accordingly"""
	for event in pygame.event.get:
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				rect.x += 1
			elif event == pygame.K_LEFT:
				rect.x -= 1
		#elif event.type == pygame.KEYUP:
