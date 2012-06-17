import draw
V_PARTS = 7
H_PARTS = V_PARTS
V_CENTER = 3
H_CENTER = 3

class PartData:
	name = None
	attached = None
	x = None
	y = None
	parent = None
	color = None

	def __init__( self, x, y, name, color ):
		self.x = x
		self.y = y
		self.name = name
		self.color = color

	def set_parent( self, parent ):
		self.parent = parent

class Blueprint:
	parts = []

	def __init__( self ):
		self.parts = [[None for j in range(V_PARTS)] for i in range(H_PARTS)]

	def set_part( self, (x,y), name ):
		self.parts[x][y] = PartData( x, y, name, self.color )

	def attach_parts( self, (cx,cy), (px,py) ):
		self.parts[cx][cy].set_parent( self.parts[px][py] )

class BlueprintFactory:

	def __init__( self ):
		pass

	def make( self ):
		bp = Blueprint()
		bp.color = draw.PINK

		bp.set_part( (3,3), "COCKPIT" )
		bp.set_part( (2,3), "ARMOR" )
		bp.attach_parts( (2,3), (3,3) )
		bp.set_part( (2,2), "ARMOR" )
		bp.attach_parts( (2,2), (2,3) )
		bp.set_part( (2,1), "THRUSTER" )
		bp.attach_parts( (2,1), (2,2) )
		bp.set_part( (4,3), "ARMOR" )
		bp.attach_parts( (4,3), (3,3) )
		bp.set_part( (4,2), "ARMOR" )
		bp.attach_parts( (4,2), (4,3) )
		bp.set_part( (5,3), "THRUSTER" )
		bp.attach_parts( (5,3), (4,3) )

		return bp


