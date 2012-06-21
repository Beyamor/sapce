from abilities import *
from gfx.image import get_image
from part import Part

PART_TYPES = {}

class Cockpit(Part):

	def __init__(self, context, plan, position):

		Part.__init__(self, context, plan, position)
		self.hp = 1
		self.total_hp = 1
		self.image = get_image("cockpit.png")
COCKPIT = "COCKPIT"
PART_TYPES[COCKPIT] = Cockpit

class Armor(Part):

	def __init__(self, context, plan, position):

		Part.__init__(self, context, plan, position)
		self.hp = 1
		self.total_hp = 1
		self.image = get_image("armor.png")
ARMOR = "ARMOR"
PART_TYPES[ARMOR] = Armor

@is_thruster
class Thruster(Part):

	def __init__(self, context, plan, position):
		
		Part.__init__(self, context, plan, position)
		self.hp = 1
		self.total_hp = 1
		self.image = get_image("thruster.png")

	def initial_rotation(self):

		if self.plan is None or self.plan.parent is None:
			return Part.initial_rotation(self)

		dx = self.plan.parent.x - self.plan.x
		dy = self.plan.parent.y - self.plan.y

		if dx > 0:
			return 0
		if dx < 0:
			return 180
		if dy > 0:
			return 90
		if dy < 0:
			return 270
THRUSTER = "THRUSTER"
PART_TYPES[THRUSTER] = Thruster
