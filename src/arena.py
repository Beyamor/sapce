from phys import phys

class Arena:
	entities = []
	entity_index = 0
	world = None

	def __init__(self):
		"""
		Constructs the arena's world.
		"""
		self.world = phys.make_world()

	def add( self, entity ):
		"""
		Adds an entity to the arena.

		Args:
			entity: The entity to add.
		"""
		self.entities.append( entity )

	def remove( self, entity ):
		"""
		Removes an entity from the arena.

		Args:
			entity: The entity to remove.
		"""
		self.entities.remove( entity )
		self.entity_index = self.entity_index % len(self.entities)

	def get_next_entity(self):
		entity = self.entities[self.entity_index]
		self.entity_index = (self.entity_index + 1) % len(self.entities)
		return entity
