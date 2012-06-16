import math
import random
from pygame import Color
from pygame import draw
import draw
import phys

class Jucoid:
	screen = None
	world = None
	color = None
	vertices = None
	body = None
	direction = 0

	def __init__(self, context):

		self.screen = context.screen
		self.world = context.world

		self.direction = random.uniform(0,360)

		r = random.randint(0, 255)
		g = random.randint(0, 255)
		b = random.randint(0, 255)
		self.color = Color( r, g, b, 255 )

		numberOfVertices = random.randint( 6, 10 )
		degreeSplinter = 360 / numberOfVertices

		self.vertices = []
		for vertexIndex in range( numberOfVertices ):

			angle = vertexIndex * degreeSplinter + random.uniform( -degreeSplinter/2, degreeSplinter/2 )
			length = random.uniform( 0.5, 3 )
			vertex = ( math.cos( math.radians(angle) ) * length,
					-math.sin( math.radians(angle) ) * length )
			self.vertices.append( vertex )

		self.body = phys.make_poly( self.world, (10,10), self.vertices )

	def get_pos(self):

		return self.body.worldCenter

	def update(self,delta):

		MAGIC_FORCE = 1
		impulse = ( math.cos( math.radians(self.direction) ) * MAGIC_FORCE,
				math.sin( math.radians(self.direction) ) * MAGIC_FORCE )
		phys.apply_impulse( self.body, impulse )

	def draw(self):

		draw.phys_poly( self.screen, self.get_pos(), self.vertices, self.color )
