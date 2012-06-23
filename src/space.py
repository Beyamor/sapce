import math
import random
from gfx import image
from geometry import Rect, Vector


class Star:
	def __init__(self, position):
		self.position = position
		self.image = image.get_image("star1.png")

	def draw(self, view):
		view.draw_image(
				self.image,
				self.position)


class Section:
	width = 10
	height = 10

	def __init__(self, position):
		self.position = position
		self.stars = []
		self.make_stars()

	def make_stars(self):
		average_number = 20
		spread = 1
		number_of_stars = int(round(max(random.gauss(average_number, spread), 0)))

		for i in range(number_of_stars):
			x = random.uniform(0, Section.width) + self.position.x
			y = random.uniform(0, Section.height) + self.position.y
			self.stars.append(Star(Vector(x,y)))


class Space:
	def __init__(self):
		self.sections = {}

	def make_section(self, x, y):
		new_section = Section(Vector(x, y))
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

class Spacelizer:
	pass
