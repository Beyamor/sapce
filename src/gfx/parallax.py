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
			origin_x = self.view.origin[0] * (1 - 0.8 ** (layer+1))
			origin_y = self.view.origin[1] * (1 - 0.8 ** (layer+1))
			step_h = self.view.from_pixels(image.get_width())
			step_v = self.view.from_pixels(image.get_height())

			for i in range(10):
				for j in range(10):
					self.view.draw_image(
							image,
							(origin_x+step_h*i,
								origin_y+step_v*j))
