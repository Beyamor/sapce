import phys

class Arena:
	entities = []
	world = None

	def __init__(self):

		self.world = phys.get_world()

	def add( self, entity ):

		self.entities.append( entity )

	def remove( self, entity ):

		self.entities.remove( entity )
