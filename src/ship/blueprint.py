import draw

V_PARTS = 7
H_PARTS = V_PARTS
V_CENTER = 4
H_CENTER = 4

class PartData:
	name = None
	attached = None
	x = None
	y = None
	parent = None

	def __init__( self, x, y, name ):
		self.x = x
		self.y = y
		self.name = name

	def set_parent( self, parent ):
		self.parent = parent

class Blueprint:
	parts = []

	def __init__( self ):

		self.color = draw.PINK		
		self.parts = [[None for j in range(V_PARTS)] for i in range(H_PARTS)]
		self.define()

	def set_part( self, (x,y), name ):
		self.parts[x][y] = PartData( x, y, name )

	def attach_parts( self, (cx,cy), (px,py) ):
		self.parts[cx][cy].set_parent( self.parts[px][py] )

	def define( self ):

		self.set_part( (H_CENTER,V_CENTER), "COCKPIT" )
		self.set_part( (H_CENTER-1,V_CENTER), "THRUSTER" )
		self.attach_parts( (H_CENTER-1,V_CENTER), (H_CENTER,V_CENTER) )
