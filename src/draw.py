import pygame

PPM = 10.0
pygame.init()

Color = pygame.Color

def get_screen( width, height, caption = "boobs" ):

	screen = pygame.display.set_mode( (width,height), 0, 32 )
	pygame.display.set_caption( caption )

	return screen

def get_image( image_name, color=None ):

	root_dir = "resources/"
	image = pygame.image.load( root_dir + image_name )

	if color:
		image.fill( color, special_flags=pygame.BLEND_RGB_MULT )

	return image

def start_frame( screen ):
	screen.fill( (0,0,0,0) )

def finish_frame( screen ):
	pygame.display.flip()

def image( screen, pos, image, angle=None ):

	if angle != None:
		image = pygame.transform.rotate( image, angle )

	screen.blit( image, pos )


def phys_poly( screen, xy, vertices, color ):

	drawVertices = []
	for vertex in vertices:
		drawVertices.append(( (xy[0] + vertex[0]) * PPM,
			(xy[1] + vertex[1]) * PPM ))

	pygame.draw.polygon( screen, color, drawVertices, 0 )
	pygame.draw.circle( screen, Color("#00FFFF"), (int(xy[0]*PPM),int(xy[1]*PPM)), 2 )
