import pygame

_MAX_ROTATION_CACHE = 5

class Image():

	_raw = None
	_tinted = None
	_tint_color = None
	_rotations = []

	def __init__(self, data):
		self._raw = data

	def _get_unrotated( self ):
		if self._tinted is not None:
			return self._tinted
		else:
			return self._raw

	def _cache_tint( self, tint ):
		# new tint - must be cached
		if tint != self._tint_color:
			self._tint_color = tint

			# discard rotations based on previous tint
			self._rotations = []

			if tint is not None:
				self._tinted = self._raw.copy()
				self._tinted.fill( tint, special_flags=pygame.BLEND_RGB_MULT )
			else:
				self._tinted = None

	def _cache_rotation( self, rotation ):
		rotation_is_cached = False

		# check whether the rotation is in the cache
		for rot in range(len(self._rotations)):
			if self._rotations[rot][0] == rotation:
				rotation_is_cached = True
				break

		# if it's not, add it to the cache
		if not rotation_is_cached:
			self._rotations.append((
				rotation,
				pygame.transform.rotate( self._get_unrotated(), rotation )))
			
			if len(self._rotations) >= _MAX_ROTATION_CACHE:
				self._rotations = self._rotations[-_MAX_ROTATION_CACHE:]

	def get_data( self, tint=None, rotation=0 ):
		"""
		self._cache_tint( tint )
		self._cache_rotation( rotation )

		# since we cached tint/rotation, image is in rotation cache
		rotation_length = len(self._rotations)
		for i in range(rotation_length):
			index = rotation_length - i - 1
			if self._rotations[index][0] == rotation:
				return self._rotations[index][1]

		# uh oh?
		return None
		"""
		image = self._raw.copy()
		if tint is not None:
			image.fill(tint, special_flags=pygame.BLEND_RGB_MULT)
		if rotation != 0:
			image = pygame.transform.rotate(image, rotation)
		return image

	def get_width(self):
		return self._raw.get_width()

	def get_height(self):
		return self._raw.get_height()

def get_image(image_name):
	"""
	Loads an image from the resources directory.

	Args:
		image_name: The name of the image file.
		color: A color with which the image is tinted.

	Returns:
		The new image.
	"""
	root_dir = "resources/"
	image = Image( pygame.image.load( root_dir + image_name ) )
	image.name = image_name
	return image
