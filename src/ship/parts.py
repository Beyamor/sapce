import math
import copy
from gfx.image import get_image
from phys import phys

WIDTH = 1
HEIGHT = 1

PART_TYPES = {}

class Part:
	hp = 0
	total_hp = 0
	image = None
	context = None
	body = None
	plan = None

	can_thrust = False

	def __init__( self, context, plan, position ):
		self.context = context
		self.plan = plan
		self.body = phys.make_box(
				self.context.world,
				dim=(WIDTH,HEIGHT),
				position=position,
				rotation=self.initial_rotation() )

	def initial_rotation( self ):
		return 0

	def __del__( self ):
		self.context.world.DestroyBody( self.body )

	def take_hit( self, hit ):
		self.hp -= hit

	def is_destroyed( self ):
		return self.hp <= self.total_hp

	def get_pos( self ):
		return copy.copy( self.body.worldCenter )

	def get_rotation( self ):
		return math.degrees( self.body.angle )

	def draw( self, view ):

		if self.image:
			view.draw_image( self.image, self.get_pos(), angle=-1*self.get_rotation(), color=self.plan.color )

def thruster( part ):

	orig_init = part.__init__

	def __init__( self, *args, **kwargs ):
		orig_init( self, *args, **kwargs )
		self.can_thrust = True

	def apply_thrust( self ):

		MAGIC_IMPULSE_VALUE = 0.025

		pos = self.get_pos()
		ang = self.get_rotation()
		wb2 = WIDTH*0.5
		applyPoint = ( math.cos( math.radians(ang-180) ) * wb2,
				math.sin( math.radians(ang-180) ) * wb2 )

		pos[0] += applyPoint[0]
		pos[1] += applyPoint[1]

		phys.apply_impulse( self.body,
				phys.make_impulse( self.get_rotation(), MAGIC_IMPULSE_VALUE ),
				pos=pos )

	part.__init__ = __init__
	part.apply_thrust = apply_thrust

	return part

class Cockpit( Part ):

	def __init__( self, context, plan, position ):

		Part.__init__( self, context, plan, position )
		self.hp = 1
		self.total_hp = 1
		self.image = get_image( "cockpit.png" )

PART_TYPES["COCKPIT"] = Cockpit

class Armor( Part ):

	def __init__( self, context, plan, position ):

		Part.__init__( self, context, plan, position )
		self.hp = 1
		self.total_hp = 1
		self.image = get_image( "armor.png" )

PART_TYPES["ARMOR"] = Armor


@thruster
class Thruster( Part ):

	def __init__( self, context, plan, position ):
		
		Part.__init__( self, context, plan, position )
		self.hp = 1
		self.total_hp = 1
		self.image = get_image( "thruster.png" )

	def initial_rotation( self ):

		if self.plan is None or self.plan.parent is None:
			return Part.initial_rotation( self )

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

PART_TYPES["THRUSTER"] = Thruster

def make_part( context, part_data, position ):

	if part_data is not None and part_data.name in PART_TYPES:
		return PART_TYPES[part_data.name]( context, part_data, position )
	else:
		return None
