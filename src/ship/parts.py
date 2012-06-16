import math
from draw import get_image
import phys
import draw

WIDTH = 1
HEIGHT = 1

class Part:
	hp = 0
	total_hp = 0
	image = None
	context = None
	body = None

	def __init__( self, context ):
		self.context = context
		self.body = phys.make_box( self.context.world, dim=(WIDTH,HEIGHT) )

	def __del__( self ):
		self.context.world.DestroyBody( self.body )

	def take_hit( self, hit ):
		self.hp -= hit

	def is_destroyed( self ):
		return self.hp <= self.total_hp

	def get_pos( self ):
		return self.body.worldCenter

	def get_rotation( self ):
		return math.degrees( self.body.angle )

	def draw( self, screen ):

		if self.image:
			draw.image( screen, self.get_pos(), self.image, angle=self.get_rotation() )


COCKPIT = "cockpit"
class Cockpit( Part ):

	def __init__( self, context, color ):

		Part.__init__( self, context )
		self.hp = 1
		self.total_hp = 1
		self.image = get_image( "cockpit.png", color )

def make_part( part_name, context, color ):

	if part_name == COCKPIT:
		return Cockpit( context, color )
	else:
		return None
