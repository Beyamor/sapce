import Box2D
import pygame

Vector = Box2D.b2Vec2

class Rect:
	
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
