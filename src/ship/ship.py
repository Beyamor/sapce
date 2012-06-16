class Ship:
	blueprint = None
	pilot = None
	parts = None

	def __init__( self, pilot, blueprint ):

		self.blueprint = blueprint
		self.__build__()

	def __build__( self ):
		pass

	def update( self, dt ):
		pass

	def draw( self ):
		pass
