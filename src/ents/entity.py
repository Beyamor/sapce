import math
import copy

def uses_body_position(cls):
	def get_position(self):
		return copy.copy(self.body.worldCenter)
	cls.get_position = get_position
	return cls

def uses_body_rotation(cls):
	def get_rotation(self):
		return math.degrees(self.body.angle)
	cls.get_rotation = get_rotation
	return cls

def uses_body_attributes(cls):
	cls = uses_body_position(cls)
	cls = uses_body_rotation(cls)
	return cls
