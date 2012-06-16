from draw import get_image
import draw

class Part:
	hp = 0
	total_hp = 0
	image = None
	context = None

	def __init__( self, context ):

		self.context = context

	def take_hit( self, hit ):
		self.hp -= hit

	def is_destroyed( self ):
		return self.hp <= self.total_hp

	def get_pos( self ):
		return (0,0)

	def get_rotation( self ):
		return 0

	def draw( self, screen ):

		if self.image:
			draw.image( screen, self.get_pos(), self.image, angle=self.get_rotation() )


COCKPIT = "cockpit"
class Cockpit( Part ):

	def __init__( self, context, color ):

		Part(self).__init__( context )
		self.hp = 1
		self.total_hp = 1
		self.image = get_image( "cockpit.png", color )

def make_part( part_name, context, color ):

	if part_name == COCKPIT:
		return Cockpit( context, color )
	else:
		return None
