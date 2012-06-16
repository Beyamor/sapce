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

	def __init__( self, x, y, name ):
		self.x = x
		self.y = y
		self.name = name

class Blueprint:
	parts = []

	def __init__( self ):

		self.color = draw.PINK		
		self.parts = [[None for j in range(V_PARTS)] for i in range(H_PARTS)]
		self.define()

	def set_part( x, y, name ):
		self.parts[x][y] = PartData( x, y, name )

	def define( self ):

		self.parts[H_CENTER][V_CENTER] = "COCKPIT"
		self.parts[H_CENTER][V_CENTER-1] = "THRUSTER"
