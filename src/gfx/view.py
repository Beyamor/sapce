import draw
from geometry import Vector, Rect

class View:
	screen = None
	scale = 1
	origin = Vector(0,0)
	width = 0
	height = 0

	def __init__(self, screen, scale, origin):
		self.screen = screen
		self.scale = scale
		self.width = self.from_pixels(screen.get_width())
		self.height = self.from_pixels(screen.get_height())
		self.origin = origin

	def from_pixels(self, number):
		return number/self.scale

	def to_pixels(self, number):
		return number*self.scale

	def center(self, position):
		self.origin = Vector(position.x - self.width/2.,
				position.y - self.height/2.)

	def draw_rect(self, rect, color=draw.WHITE, filled=True):
		rect = Rect(
				(rect.x - self.origin.x) * self.scale,
				(rect.y - self.origin.y) * self.scale,
				rect.width * self.scale,
				rect.height * self.scale)
		
		draw.rect(
				self.screen,
				rect,
				color=color,
				filled=filled)

	def draw_image(self, image, pos, angle=0, color=None):

		x = (pos[0] - self.origin[0]) * self.scale
		y = (pos[1] - self.origin[1]) * self.scale

		draw.image(
				self.screen,
				image,
				(x,y),
				angle=angle,
				color=color )

class PhysView(View):

	def __init__(self, screen):
		View.__init__(self, screen, draw.PPM, (0,0))
