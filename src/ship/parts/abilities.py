import math
from phys import phys
from part import WIDTH, HEIGHT

def is_thruster(part):

	orig_init = part.__init__

	def __init__(self, *args, **kwargs):
		orig_init(self, *args, **kwargs)
		self.can_thrust = True

	def apply_thrust(self):

		MAGIC_IMPULSE_VALUE = 0.05

		pos = self.get_pos()
		ang = self.get_rotation()
		wb2 = WIDTH*0.5
		applyPoint = (math.cos(math.radians(ang-180)) * wb2,
				math.sin(math.radians(ang-180)) * wb2)

		pos[0] += applyPoint[0]
		pos[1] += applyPoint[1]

		phys.apply_impulse(self.body,
				phys.make_impulse(self.get_rotation(), MAGIC_IMPULSE_VALUE),
				pos=pos)

	part.__init__ = __init__
	part.apply_thrust = apply_thrust
	return part

def is_blaster(part):

	orig_init = part.__init__

	def __init__(self, *args, **kwargs):
		orig_init(self, *args, **kwargs)
		self.can_shoot = True

	def shoot(self):
		pass

	part.__init__ = __init__
	part.shoot = shoot
	return part
