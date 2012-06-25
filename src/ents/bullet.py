import copy
import math
from gfx import image
from gfx.draw import PPM
from phys import phys

RADIUS = 8 / PPM
DIAMETER = 2 * RADIUS
SPEED = 5

class Bullet:
	def __init__(self, physics_space, view, position=(0,0), speed=SPEED, direction=0):
		self.physics_space = physics_space
		self.view = view
		self.image = image.get_image("shot.png")
		self.body = phys.make_box(
				physics_space,
				dim=(DIAMETER, DIAMETER),
				position=position,
				rotation=math.radians(direction),
				friction=0)
		
		initial_impulse = phys.make_impulse(
				direction,
				SPEED) # TODO: make speed actually represent speed
		phys.apply_impulse(
				self.body,
				initial_impulse)

	def get_position(self):
		return copy.copy(self.body.worldCenter)

	def get_rotation(self):
		return math.degrees(self.body.angle)

	def update(self, dt):
		pass
	
	def draw(self):
		self.view.draw_image(
				self.image,
				self.get_position(),
				angle=self.get_rotation())

class BulletFactory:
	def __init__(self, arena):
		self.arena = arena

	def make(self, position=(0,0), speed=SPEED, direction=0):
		arena = self.arena
		bullet = Bullet(
			arena.physics_space,
			arena.view,
			position=position,
			speed=speed,
			direction=direction)
		return bullet
