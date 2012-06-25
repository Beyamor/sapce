from ship import Ship
from pilot import Pilot
from blueprint import BlueprintFactory

class ShipFactory:
	def __init__(self, arena):
		self.arena = arena
		self.blueprinter = BlueprintFactory()

	def make(self, position=(0,0)):
		arena = self.arena
		ship = Ship(
				physics_space=arena.physics_space,
				view=arena.view,
				pilot=Pilot(),
				blueprint=self.blueprinter.make(),
				position=position)
		return ship
