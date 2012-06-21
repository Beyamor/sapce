import math

class Parallaxor:
	view = None
	backgrounds = []

	def __init__(self, view):
		self.view = view

	def push_background(self, image):
		self.backgrounds.append(image)

	def draw(self):

		for layer in range(len(self.backgrounds)):
			image = self.backgrounds[layer]

			shift_factor = 1 - 0.8 ** (layer+1)
			ox = self.view.origin[0]
			oy = self.view.origin[1]
			shifted_ox = ox * shift_factor
			shifted_oy = oy * shift_factor

			step_x = self.view.from_pixels(image.get_width())
			step_y = self.view.from_pixels(image.get_height())

			min_x = shifted_ox
			while min_x > ox:
				min_x -= step_x
			while min_x + step_x < ox:
				min_x += step_x
			min_y = shifted_oy
			while min_y > oy:
				min_y -= step_y
			while min_y + step_y < oy:
				min_y += step_y

			max_x = min_x + self.view.width + step_x * 2
			max_y = min_y + self.view.height + step_y * 2

			x = min_x
			while x <= max_x:
				y = min_y
				while y <= max_y:
					self.view.draw_image(
							image,
							(x,y))
					y += step_y
				x += step_x
