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

		self.color = draw.PINK		
		self.parts = [[None for j in range(V_PARTS)] for i in range(H_PARTS)]
		self.define()

	def set_part( self, (x,y), name ):
		self.parts[x][y] = PartData( x, y, name, self.color )

	def attach_parts( self, (cx,cy), (px,py) ):
		self.parts[cx][cy].set_parent( self.parts[px][py] )

	def define( self ):

		"""
		self.set_part( (H_CENTER,V_CENTER), "COCKPIT" )
		self.set_part( (H_CENTER-1,V_CENTER), "THRUSTER" )
		self.attach_parts( (H_CENTER-1,V_CENTER), (H_CENTER,V_CENTER) )
		"""
		self.set_part( (3,3), "COCKPIT" )
		self.set_part( (2,3), "ARMOR" )
		self.attach_parts( (2,3), (3,3) )
		self.set_part( (2,2), "ARMOR" )
		self.attach_parts( (2,2), (2,3) )
		self.set_part( (2,1), "THRUSTER" )
		self.attach_parts( (2,1), (2,2) )
		self.set_part( (4,3), "ARMOR" )
		self.attach_parts( (4,3), (3,3) )
		self.set_part( (4,2), "ARMOR" )
		self.attach_parts( (4,2), (4,3) )
		self.set_part( (5,3), "THRUSTER" )
		self.attach_parts( (5,3), (4,3) )

