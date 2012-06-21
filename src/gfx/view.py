import draw

class View:
	screen = None
	scale = 1
	origin = (0,0)

	def __init__(self, screen, scale, origin):
		self.screen = screen
		self.scale = scale
		self.origin = origin

	def draw_image(self, image, pos, angle=0, color=None):

		x = (self.origin[0] + pos[0]) * self.scale
		y = (self.origin[1] + pos[1]) * self.scale

		draw.image(
				self.screen,
				image,
				(x,y),
				angle=angle,
				color=color )

class PhysView(View):

	def __init__(self, screen):
		View.__init__(self, screen, draw.PPM, (0,0))
