from abilities import *
from gfx.image import get_image
from part import *

PART_TYPES = {}

@is_possible_parent
class Cockpit(Part):

	def __init__(self, context, plan, position):

		Part.__init__(self, context, plan, position)
		self.image = get_image("cockpit.png")
COCKPIT = "COCKPIT"
PART_TYPES[COCKPIT] = Cockpit

@is_possible_parent
class Armor(Part):

	def __init__(self, context, plan, position):

		Part.__init__(self, context, plan, position)
		self.image = get_image("armor.png")
ARMOR = "ARMOR"
PART_TYPES[ARMOR] = Armor

@rotated_to_parent
@is_thruster
class Thruster(Part):
	def __init__(self, context, plan, position):
		Part.__init__(self, context, plan, position)
		self.image = get_image("thruster.png")
THRUSTER = "THRUSTER"
PART_TYPES[THRUSTER] = Thruster

@rotated_to_parent
@is_blaster
class Blaster(Part):
	def __init__(self, context, plan, position):
		Part.__init__(self, context, plan, position)
		self.image = get_image("blaster.png")
BLASTER = "BLASTER"
PART_TYPES[BLASTER] = Blaster
