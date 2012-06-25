import copy
import math
from gfx import image
from gfx.draw import PPM
from gfx import draw
from phys import phys
from ents.entity import uses_body_attributes

RADIUS = 8 / PPM
DIAMETER = 2 * RADIUS
SPEED = 0.5

@uses_body_attributes
class Bullet:
	def __init__(self, physics_space=None, view=None, position=(0,0), speed=SPEED, direction=0):
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
				speed) # TODO: make speed actually represent speed
		phys.apply_impulse(
				self.body,
				initial_impulse)

	def update(self, dt):
		pass
	
	def draw(self):
		self.view.draw_image(
				self.image,
				self.get_position(),
				angle=self.get_rotation(),
				color=draw.CYAN)

class BulletFactory:
	def __init__(self, arena):
		self.arena = arena

	def make(self, position=(0,0), speed=SPEED, direction=0):
		arena = self.arena
		bullet = Bullet(
			physics_space=arena.physics_space,
			view=arena.view,
			position=position,
			speed=speed,
			direction=direction)
		return bullet
