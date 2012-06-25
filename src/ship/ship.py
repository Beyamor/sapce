import parts
from parts import part
from blueprint import V_CENTER,H_CENTER
from phys import phys

class Ship:
	blueprint = None
	pilot = None
	parts = None

	def __init__(self, arena=None, pilot=None, blueprint=None, position=(5,5)):
		self.view = arena.view
		self.pilot = pilot
		self.blueprint = blueprint
		self.__build__(position, arena)

	def __build__(self, position, arena):
		physics_space = arena.physics_space

		# make the parts
		self.parts = []
		for i in range(len(self.blueprint.parts)):

			self.parts.append([])
			for j in range(len(self.blueprint.parts[i])):

				pos = (position[0]+(i-V_CENTER)*part.WIDTH,
						position[1]+(j-H_CENTER)*part.HEIGHT)

				self.parts[i].append(
						parts.make_part(
							arena,
							self.blueprint.parts[i][j],
							pos) )
		# attach them
		for i in range(len(self.parts)):
			for j in range(len(self.parts[i])):

				child_data = self.blueprint.parts[i][j]
				if child_data is None or child_data.parent is None:
					continue

				parent_data = child_data.parent

				child_body = self.parts[child_data.x][child_data.y].body
				parent_body = self.parts[parent_data.x][parent_data.y].body

				phys.weld(physics_space, child_body, parent_body)

	def get_position(self):
		return self.parts[H_CENTER][V_CENTER].get_position()

	def update(self, dt):
		for i in range(len(self.parts)):
			for j in range(len(self.parts[i])):

				part = self.parts[i][j]

				if part is None:
					continue

				part.update(dt)

				if part.can_thrust:
					part.apply_thrust()
				if part.can_shoot:
					part.shoot()
	
	def draw(self):

		for i in range(len(self.parts)):
			for j in range(len(self.parts[i])):

				part = self.parts[i][j]

				if part is None:
					continue

				part.draw(self.view)
