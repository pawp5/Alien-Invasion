import pygame

pygame.init()

# Setup screen and screen color
screen = pygame.display.set_mode((1260, 600))
pygame.display.set_caption("Rocket")

# Raindrop settings
rain_speed = 1.0

# Load raindrop and get rect
raindrop = pygame.image.load("images/ship.bmp")
rect = raindrop.get_rect

def main():
	"""Game's main loop."""
	while True:
		check_events()
		update_rain()
		update_screen()

def check_events():
	"""Respond to keyboard events."""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		
	
def update_rain():
	"""Update the position of the raindrop."""
	y += rain_speed
	rect.y = y

def update_screen():
		"""Update images on the screen and flip to the new screen."""
		screen.fill(230, 230, 230)
		screen.blit(raindrop, rect)
		raindrop.draw(screen)
		screen.flip()