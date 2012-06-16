import random
from pygame import Color


class Jucoid:
	color = None
	vertices = None


	def __init__(self):

		r = random.randint(0, 255)
		g = random.randint(0, 255)
		b = random.randint(0, 255)
		self.color = Color( r, g, b, 255 )

		numberOfVertices = random.randint( 3, 10 )
		degreeSplinter = 360 / numberOfVertices

		self.vertices = []
		for vertexIndex in range( numberOfVertices ):

			angle = vertexIndex * degreeSplinter + random.uniform( -degreeSplinter/2, degreeSplinter/2 )
			length = random.uniform( 0.5, 3 )
			self.vertices.append( (angle,length) )

	def draw(self):
		pass
