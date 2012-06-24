import pygame

_MAX_ROTATION_CACHE = 5

class Image():

	def __init__(self, img, print_cache_misses = False):
		self._raw = img
		self._cached_tint = None
		self._tinted = None
		self._cached_angle = 0
		self._rotated = None
		self._unrotated = self._raw
		self._transformed = self._raw
		self.width = self._transformed.get_width()
		self.height = self._transformed.get_height()
		self._data = self._transformed.convert_alpha()
		self._cache(None, 0)
		self._print_cache_misses = print_cache_misses

	def _cache(self, tint, rotation):
		cache_miss = False
		new_tint = False
		
		if self._cached_tint != tint:
			cache_miss = True
			new_tint = True

			# throw away angle based on previous tint
			self._cached_angle = 0

			self._cached_tint = tint
			if tint is not None:
				self._tinted = self._raw.copy()
				self._tinted.fill(tint, special_flags=pygame.BLEND_RGB_MULT)
				self._unrotated = self._tinted
				self._transformed = self._tinted
			else:
				self._tinted = None
				self._unrotated = self._raw
				self._transformed = self._raw

		# if new angle or need to redraw angle
		angle_difference = rotation - self._cached_angle
		min_difference = 1
		if angle_difference > min_difference or angle_difference < -min_difference or new_tint:
			cache_miss = True

			self._cached_angle = rotation
			self._rotated = pygame.transform.rotate(self._unrotated, rotation)
			self._transformed = self._rotated

		if cache_miss:
			self.width = self._transformed.get_width()
			self.height = self._transformed.get_height()
			self._data = self._transformed.convert_alpha() 
			if self._print_cache_misses:
				print "IMAGE CACHE MISS"
		
	def get_data(self, tint=None, rotation=0):
		self._cache(tint, rotation)
		return self._data

	def get_width(self):
		return self._raw.get_width()

	def get_height(self):
		return self._raw.get_height()

def get_image(image_name, print_cache_misses=False):
	"""
	Loads an image from the resources directory.

	Args:
		image_name: The name of the image file.
		color: A color with which the image is tinted.

	Returns:
		The new image.
	"""
	root_dir = "resources/"
	image = Image(pygame.image.load(root_dir + image_name), print_cache_misses)
	image.name = image_name
	return image
