import math

class Parallaxor:

	class Layer:
		def __init__(self, image, view, shift_factor):
			self.image = image
			self.step_x = view.from_pixels(image.get_width())
			self.step_y = view.from_pixels(image.get_height())
			self.shift_factor = shift_factor
		
	view = None
	backgrounds = []

	def __init__(self, view):
		self.view = view

	def next_background_factor(self):
		return 1 - 0.9 ** (len(self.backgrounds) + 1)

	def push_background(self, image):
		self.backgrounds.append(
				Parallaxor.Layer(
					image,
					self.view,
					self.next_background_factor()))

	def draw(self):

		for layer in self.backgrounds:
			shift_factor = layer.shift_factor
			ox = self.view.origin[0]
			oy = self.view.origin[1]
			shifted_ox = ox * shift_factor
			shifted_oy = oy * shift_factor

			min_x = shifted_ox
			while min_x > ox:
				min_x -= layer.step_x
			while min_x + layer.step_x < ox:
				min_x += layer.step_x
			min_y = shifted_oy
			while min_y > oy:
				min_y -= layer.step_y
			while min_y + layer.step_y < oy:
				min_y += layer.step_y

			max_x = min_x + self.view.width + layer.step_x * 2
			max_y = min_y + self.view.height + layer.step_y * 2

			x = min_x
			while x <= max_x:
				y = min_y
				while y <= max_y:
					self.view.draw_image(
							layer.image,
							(x,y))
					y += layer.step_y
				x += layer.step_x
