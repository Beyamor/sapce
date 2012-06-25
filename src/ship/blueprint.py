import random
from gfx import draw
from parts.types import *
from debug import log

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
	added_a_thruster = False
	colors  = [
			draw.PINK,
			draw.BLUE,
			draw.YELLOW,
			draw.GREEN,
			draw.RED]
	color_index = 0

	def __init__( self ):
		pass

	def is_candidate_parent( self, part ):
		return part is not None and \
			PART_TYPES[part.name].can_be_parent

	def add_cockpit( self, bp ):
		bp.set_part( (H_CENTER, V_CENTER), COCKPIT )

	def add_part( self, bp, name=None ):

		candidates = []
		for i in range( len(bp.parts) ):
			for j in range( len(bp.parts[i]) ):
				if not self.is_candidate_parent( bp.parts[i][j] ):
					continue

				if i > 0 and bp.parts[i-1][j] is None:
					candidates.append(( (i,j), (i-1,j) ))

				if i < len(bp.parts)-1 and bp.parts[i+1][j] is None:
					candidates.append(( (i,j), (i+1,j) ))

				if j > 0 and bp.parts[i][j-1] is None:
					candidates.append(( (i,j), (i,j-1) ))

				if j < len(bp.parts[i])-1 and bp.parts[i][j+1] is None:
					candidates.append(( (i,j), (i,j+1) ))

		if len(candidates) is 0:
			log.logmsg("No candidate parents", log.LOG_INFO)
			return

		candidate = candidates[ random.randint(0,len(candidates)-1) ]
		child = candidate[1]
		parent = candidate[0]

		if name is None:
			derp = random.randint(0,3)
			if derp == 0:
				name = THRUSTER
			elif derp == 1:
				name = BLASTER
			else:
				name = ARMOR
		if name is THRUSTER:
			self.added_a_thruster = True

		bp.set_part( child, name )
		bp.attach_parts( child, parent )


	def make( self ):
		self.added_a_thruster = False

		bp = Blueprint()
		bp.color = self.colors[self.color_index % len(self.colors)]
		self.color_index += 1
		self.add_cockpit( bp )

		number_of_parts = random.randint( 4, 7 )
		for i in range( number_of_parts ):
			self.add_part( bp )

		if not self.added_a_thruster:
			self.add_part( bp, THRUSTER )

		return bp

	def make_thruster_ship(self):
		bp = Blueprint()
		bp.color = self.colors[self.color_index % len(self.colors)]
		self.color_index += 1
		self.add_cockpit(bp)
		bp.set_part((H_CENTER - 1,V_CENTER), THRUSTER)
		bp.attach_parts((H_CENTER - 1,V_CENTER), (H_CENTER, V_CENTER))
		return bp
