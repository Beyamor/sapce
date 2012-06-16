from parts import COCKPIT


V_PARTS = 7
H_PARTS = V_PARTS
V_CENTER = 4
H_CENTER = 4

class Blueprint:
	parts = []

	def __init__( self ):

		self.parts = [[None for i in range(H_PARTS)] for j in range(V_PARTS)]
		self.define()


	def define( self ):

		self.parts[V_CENTER][H_CENTER] = COCKPIT
