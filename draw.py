from pygame import init as pyinit, display, draw as pydraw, Color

PPM = 40.0
pyinit()

def get_screen( width, height, caption = "boobs" ):

	screen = display.set_mode( (width,height), 0, 32 )
	display.set_caption( caption )

	return screen

def finish_frame():
	display.flip()

def physPolygon( surface, xy, vertices, color ):

	drawVertices = []
	for vertex in vertices:
		drawVertices.append(( (xy[0] + vertex[0]) * PPM,
			(xy[1] + vertex[1]) * PPM ))

	pydraw.polygon( surface, color, drawVertices, 0 )
	pydraw.circle( surface, Color("#00FFFF"), (int(xy[0]*PPM),int(xy[1]*PPM)), 2 )
