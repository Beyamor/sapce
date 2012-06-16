from draw import get_image

class Part:
	hp = 0
	total_hp = 0
	image = None


	def take_hit( self, hit ):

		self.hp -= hit


	def is_destroy( self ):

		return self.hp <= self.total_hp

COCKPIT = "cockpit"
class Cockpit( Part ):

	def __init__( self ):

		self.hp = 1
		self.total_hp = 1

def make_part( part_name ):

	if part_name == COCKPIT:

		return Cockpit()

	else:

		return None
