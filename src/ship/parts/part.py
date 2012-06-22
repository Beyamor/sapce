import math
import copy
from phys import phys

WIDTH = 1
HEIGHT = 1

class Part:
	hp = 0
	total_hp = 0
	image = None
	context = None
	body = None
	plan = None
	can_be_parent = False
	can_thrust = False
	can_shoot = False

	def __init__( self, context, plan, position ):
		self.context = context
		self.plan = plan
		self.body = phys.make_box(
				self.context.world,
				dim=(WIDTH,HEIGHT),
				position=position,
				rotation=self.initial_rotation() )

	def initial_rotation( self ):
		return 0

	def __del__( self ):
		self.context.world.DestroyBody( self.body )

	def take_hit( self, hit ):
		self.hp -= hit

	def is_destroyed( self ):
		return self.hp <= self.total_hp

	def get_pos( self ):
		return copy.copy( self.body.worldCenter )

	def get_rotation( self ):
		return math.degrees( self.body.angle )

	def draw( self, view ):

		if self.image:
			view.draw_image( self.image, self.get_pos(), angle=-1*self.get_rotation(), color=self.plan.color )

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
