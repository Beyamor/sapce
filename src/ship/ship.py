import parts
from blueprint import V_CENTER,H_CENTER
from phys import phys

class Ship:
	blueprint = None
	pilot = None
	parts = None
	context = None

	def __init__( self, context, pilot, blueprint, position=(5,5) ):

		self.context = context
		self.pilot = pilot
		self.blueprint = blueprint
		self.__build__( position )

	def __build__( self, position ):

		# make the parts
		self.parts = []
		for i in range( len(self.blueprint.parts) ):

			self.parts.append( [] )
			for j in range( len(self.blueprint.parts[i]) ):

				pos = ( position[0]+(i-V_CENTER)*parts.WIDTH,
						position[1]+(j-H_CENTER)*parts.HEIGHT )

				self.parts[i].append(
						parts.make_part(
							self.context,
							self.blueprint.parts[i][j],
							pos ) )
		# attach them
		for i in range( len(self.parts) ):
			for j in range( len(self.parts[i]) ):

				child_data = self.blueprint.parts[i][j]
				if child_data is None or child_data.parent is None:
					continue

				parent_data = child_data.parent

				child_body = self.parts[child_data.x][child_data.y].body
				parent_body = self.parts[parent_data.x][parent_data.y].body

				phys.weld( self.context.world, child_body, parent_body )

	def get_position(self):
		return self.parts[H_CENTER][V_CENTER].get_pos()

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

				part.draw( self.context.view )
