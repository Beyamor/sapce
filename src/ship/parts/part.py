import math
import copy
from phys import phys
from ents.entity import uses_body_attributes

WIDTH = 1
HEIGHT = 1

@uses_body_attributes
class Part:
	hp = 0
	total_hp = 0
	image = None
	physics_space = None
	body = None
	plan = None
	can_be_parent = False
	can_thrust = False
	can_shoot = False

	def __init__(self, arena, plan, position):
		self.arena = arena
		self.physics_space = arena.physics_space
		self.plan = plan
		self.body = phys.make_box(
				arena.physics_space,
				dim=(WIDTH,HEIGHT),
				position=position,
				rotation=self.initial_rotation())

	def initial_rotation(self):
		return 0

	def __del__(self):
		self.physics_space.DestroyBody(self.body)

	def take_hit(self, hit):
		self.hp -= hit

	def is_destroyed(self):
		return self.hp <= self.total_hp

	def update(self, dt):
		pass

	def draw(self, view):
		if self.image:
			view.draw_image(self.image, self.get_position(), angle=-1*self.get_rotation(), color=self.plan.color)

def is_possible_parent(part):
	part.can_be_parent = True
	return part

def rotated_to_parent(part):
	def initial_rotation(self):
		if self.plan is None or self.plan.parent is None:
			return Part.initial_rotation(self)

		dx = self.plan.parent.x - self.plan.x
		dy = self.plan.parent.y - self.plan.y

		if dx > 0:
			return 0
		if dx < 0:
			return 180
		if dy > 0:
			return 90
		if dy < 0:
			return 270
	part.initial_rotation = initial_rotation
	return part
