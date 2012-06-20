from Box2D import b2_staticBody, b2_dynamicBody, b2_kinematicBody, b2Shape
import pygame
import gfx.draw
from gfx.draw import phys_poly

bodyColors = {
	b2_staticBody	: (255,255,255,255),
	b2_dynamicBody   : (127,127,127,255),
	b2_kinematicBody : (50,127,127,255),
}

class PhysDebugRenderer():
	def __init__(self, world):
		self.world = world

	def draw(self, screen):
		for body in self.world.bodies:
			
			# Draw every body in the world
			for fixture in body.fixtures:
				shape=fixture.shape
				
				# Polygon
				if (shape.type == b2Shape.e_polygon):
					vertices=[(body.transform*v)*draw.PPM for v in shape.vertices]
		
					# Draw Poly to the screen
					pygame.draw.lines(screen, bodyColors[body.type], True, vertices)
					
				# Circle
				else:
					pass
