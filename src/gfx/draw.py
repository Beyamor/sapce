import pygame

PPM = 64.0
pygame.init()

Color = pygame.Color
WHITE = Color(255,255,255,255)
PINK = Color(250,175,190,255)

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

def get_image(image_name, color=None):
	"""
	Loads an image from the resources directory.

	Args:
		image_name: The name of the image file.
		color: A color with which the image is tinted.

	Returns:
		The new image.
	"""
	root_dir = "resources/"
	image = pygame.image.load(root_dir + image_name)

	if color:
		image.fill(color, special_flags=pygame.BLEND_RGB_MULT)

	return image

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

def image(screen, pos, image, angle=0):
	"""
	Draws an image on a screen.

	Args:
		screen: The screen which is drawn on.
		pos: The center position at which the image is drawn on the screen.
		image: The image which is drawn.
		angle: The rotation of the image in degrees.
	"""
	image = pygame.transform.rotate(image, angle)
	w = image.get_width()
	h = image.get_height()

	pos[0] -= w/2
	pos[1] -= h/2

	screen.blit(image, pos)

def phys_image(screen, xy, img, angle=None):
	"""
	Draws an image from physics space onto the screen.

	Args:
		screen: The screen which is drawn on.
		xy: The center position at which the image is drawn on the screen.
		image: The image which is drawn.
		angle: The rotation of the image in degrees.
	"""
	xy[0] *= PPM
	xy[1] *= PPM

	image(screen, xy, img, angle=angle)

def phys_poly(screen, xy, vertices, color):

	drawVertices = []
	for vertex in vertices:
		drawVertices.append(((xy[0] + vertex[0]) * PPM,
			(xy[1] + vertex[1]) * PPM))

	pygame.draw.polygon(screen, color, drawVertices, 0)
	pygame.draw.circle(screen, Color("#00FFFF"), (int(xy[0]*PPM),int(xy[1]*PPM)), 2)
