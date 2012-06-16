import parts

class Ship:
	blueprint = None
	pilot = None
	parts = None
	context = None

	def __init__( self, context, pilot, blueprint ):

		self.context = context
		self.pilot = pilot
		self.blueprint = blueprint
		self.__build__()

	def __build__( self ):

		self.parts = []
		for i in range( len(self.blueprint.parts) ):

			self.parts.append( [] )
			for j in range( len(self.blueprint.parts[i]) ):
				self.parts[i].append( parts.make_part( self.blueprint.parts[i][j], self.context, self.blueprint.color ) )

	def update( self, dt ):
		for i in range( len(self.parts) ):
			for j in range( len(self.parts[i]) ):

				part = self.parts[i][j]

				if part is None:
					continue

				if part.can_thrust:
					part.apply_thrust()
	
	def draw( self ):

		for i in range( len(self.parts) ):
			for j in range( len(self.parts[i]) ):

				part = self.parts[i][j]

				if part is None:
					continue

				part.draw( self.context.screen )
