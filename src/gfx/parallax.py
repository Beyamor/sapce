import math

class Parallaxor:

	class Layer:
		def __init__(self, image, view, scroll_rate):
			self.image = image
			self.step_x = view.from_pixels(image.get_width())
			self.step_y = view.from_pixels(image.get_height())
			self.scroll_rate = scroll_rate
		
	view = None
	backgrounds = []

	def __init__(self, view):
		self.view = view

	def next_background_scroll_rate(self):
		return 1 - 0.3 ** (len(self.backgrounds) + 1)

	def push_background(self, image):
		self.backgrounds.append(
				Parallaxor.Layer(
					image,
					self.view,
					self.next_background_scroll_rate()))

	def draw(self):
		for layer in self.backgrounds:
			scroll_rate = layer.scroll_rate
			ox = self.view.origin[0]
			oy = self.view.origin[1]
			shifted_ox = ox * scroll_rate
			shifted_oy = oy * scroll_rate

			wb2 = layer.step_x / 2.
			hb2 = layer.step_x / 2.

			min_x = shifted_ox
			while min_x > ox + wb2:
				min_x -= layer.step_x
			while min_x < ox - wb2:
				min_x += layer.step_x
			min_y = shifted_oy
			while min_y > oy + hb2:
				min_y -= layer.step_y
			while min_y < oy - hb2:
				min_y += layer.step_y

			max_x = ox + self.view.width + wb2
			max_y = oy + self.view.height + hb2

			x = min_x
			while x <= max_x:
				y = min_y
				while y <= max_y:
					self.view.draw_image(
							layer.image,
							(x,y))
					y += layer.step_y
				x += layer.step_x
