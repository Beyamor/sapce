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

	can_thrust = False

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
