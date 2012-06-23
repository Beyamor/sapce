import pygame

PPM = 64.0
pygame.init()

Color = pygame.Color
WHITE = Color(255,255,255,255)
PINK = Color("#FAAFBE")
GREEN = Color("#4CC417")
BLUE = Color("#3090C7")
RED = Color("#C11B17")
YELLOW = Color("#FDD017")

def get_screen(width, height, caption = "boobs"):
	"""
	Creates a screen one which things can be drawn.
	Note that there should only be one screen created.

	Args:
		width: The width of the screen.
		height: The height of the screen.
		caption: The caption of the screen.

	Returns:
		The newly created screen.
	"""
	screen = pygame.display.set_mode((width,height), 0, 32)
	pygame.display.set_caption(caption)

	return screen

def start_frame(screen):
	"""
	Prepares a screen for a new drawing frame.

	Args:
		screen: The screen which is used for drawing.
	"""
	screen.fill((0,0,0,0))

def finish_frame(screen):
	"""
	Finishes a frame's drawing on a screen.

	Args:
		screen: The screen which was drawn on.
	"""
	pygame.display.flip()

def rect(screen, rect, color=WHITE, filled=True):
	if filled is True:
		width = 0
	else:
		width = 1

	pygame.draw.rect(
			screen,
			color,
			pygame.Rect(rect.x, rect.y, rect.width, rect.height),
			width)


def image(screen, image, pos, angle=0, color=None):
	"""
	Draws an image on a screen.

	Args:
		screen: The screen which is drawn on.
		pos: The center position at which the image is drawn on the screen.
		image: The image which is drawn.
		angle: The rotation of the image in degrees.
	"""
	image_data = image.get_data( rotation=angle, tint=color )
	w = image_data.get_width()
	h = image_data.get_height()

	pos = (pos[0]-w/2.0, pos[1]-h/2.0)

	screen.blit(image_data, pos)

def phys_poly(screen, xy, vertices, color):

	drawVertices = []
	for vertex in vertices:
		drawVertices.append(((xy[0] + vertex[0]) * PPM,
			(xy[1] + vertex[1]) * PPM))

	pygame.draw.polygon(screen, color, drawVertices, 0)
	pygame.draw.circle(screen, Color("#00FFFF"), (int(xy[0]*PPM),int(xy[1]*PPM)), 2)
