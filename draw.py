import pygame

PPM = 40.0
pygame.init()

def get_screen( width, height, caption = "boobs" ):

	screen = pygame.display.set_mode( (width,height), 0, 32 )
	pygame.display.set_caption( caption )

	return screen
