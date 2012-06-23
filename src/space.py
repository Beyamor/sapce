import math
import random
from gfx import image, view
from geometry import Rect, Vector


class Star:
	def __init__(self, position, depth):
		self.position = position
		if depth == 0:
			image_name = "star0.png"
		elif depth == 1:
			image_name = "star1.png"
		else:
			image_name = "star2.png"
		self.image = image.get_image(image_name)

	def draw(self, view):
		view.draw_image(
				self.image,
				self.position)


class Section:
	width = 10
	height = 10

	def __init__(self, position, depth):
		self.position = position
		self.stars = []
		self.make_stars(depth)

	def make_stars(self, depth):
		average_number = 20
		spread = 1
		number_of_stars = int(round(max(random.gauss(average_number, spread), 0)))

		for i in range(number_of_stars):
			x = random.uniform(0, Section.width) + self.position.x
			y = random.uniform(0, Section.height) + self.position.y
			self.stars.append(Star(Vector(x,y), depth))


class Layer:
	def __init__(self, depth):
		self.depth = depth
		self.sections = {}

	def make_section(self, x, y):
		new_section = Section(Vector(x, y), self.depth)
		self.sections[(x, y)] = new_section
		return new_section

	def get_section_position(self, x, y):
		closest_x = math.floor(x / Section.width) * Section.width
		closest_y = math.floor(y / Section.height) * Section.height
		
		return (closest_x, closest_y)

	def get_section(self, x, y):
		closest_x, closest_y = self.get_section_position(x, y)

		if (closest_x, closest_y) in self.sections:
			return self.sections[(closest_x, closest_y)]
		else:
			return self.make_section(closest_x, closest_y)

	def get_stars(self, area):
		stars = []
		min_x, min_y = self.get_section_position(area.x, area.y)

		x = min_x
		while x < area.x + area.width:
			y = min_y
			while y < area.y + area.height:
				section = self.get_section(x, y)
				stars.extend(section.stars)
				y += Section.height
			x += Section.width

		return stars


class Space:
	def __init__(self):
		self.layers = [Layer(0), Layer(1), Layer(2)]
	
class Spacilizer:
	def __init__(self, view):
		self.view = view
		self.space = Space()

	def draw(self):

		for layer in self.space.layers:
			scroll_lag = 0.05 * 0.1 ** layer.depth
			parallax_view = view.View(
					self.view.screen,
					self.view.scale,
					self.view.origin * scroll_lag)
			stars = layer.get_stars(
					Rect(
						parallax_view.origin.x,
						parallax_view.origin.y,
						parallax_view.width,
						parallax_view.height))

			for star in stars:
				star.draw(parallax_view)
