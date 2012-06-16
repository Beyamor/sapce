import math
import random
from pygame import Color
from pygame import draw
import draw


class Jucoid:
	color = None
	vertices = None

	def __init__(self):

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

	def draw(self, surface):

		draw.physPolygon( surface, (5,5), self.vertices, self.color )
