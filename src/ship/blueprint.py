from parts import COCKPIT
import draw

V_PARTS = 7
H_PARTS = V_PARTS
V_CENTER = 4
H_CENTER = 4

class Blueprint:
	parts = []

	def __init__( self ):

		self.color = draw.PINK		
		self.parts = [[None for j in range(V_PARTS)] for i in range(H_PARTS)]
		self.define()

	def define( self ):

		self.parts[H_CENTER][V_CENTER] = COCKPIT
