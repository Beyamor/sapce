from phys import phys
from gfx.view import PhysView
from ship.ship import Ship
from ship.shipfactory import ShipFactory
from ents.bullet import Bullet, BulletFactory
from debug import log

class Arena:
	entities = []
	ships = []
	ship_index = 0

	def __init__(self, screen):
		"""
		Constructs the arena's world.
		"""
		self.physics_space = phys.make_world()
		self.view = PhysView(screen)
		self.ship_index = 0
		self.factories = {
				Ship: ShipFactory(self),
				Bullet: BulletFactory(self)
				}

	def make(self, cls, **kwargs):
		if cls in self.factories:
			factory = self.factories[cls]
			entity = factory.make(**kwargs)
			self.add(entity)
			if cls is Ship:
				self.ships.append(entity)
			return entity
		else:
			log.logmsg("No factory for class " + str(cls), log.LOG_WARNING)	
			return None

	def add(self, entity):
		"""
		Adds an entity to the arena.

		Args:
			entity: The entity to add.
		"""
		self.entities.append(entity)

	def remove(self, entity):
		"""
		Removes an entity from the arena.

		Args:
			entity: The entity to remove.
		"""
		self.entities.remove(entity)

	def focus_on_next_ship(self):
		self.ship_index = (self.ship_index + 1) % len(self.ships)

	def update(self, dt):
		self.physics_space.Step(dt*0.001, 10, 10)
		self.view.center(self.ships[self.ship_index].get_position())
		for entity in self.entities:
			entity.update(dt)
