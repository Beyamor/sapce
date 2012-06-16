import math
from Box2D import b2World, b2BodyDef, b2Vec2

def get_world():
	
	world = b2World( gravity=(0,0), doSleep=False )
	return world

def make_impulse( direction, magnitude ):
	return ( math.cos( math.radians(direction) ) * magnitude,
			-1 * math.sin( math.radians(direction) ) * magnitude )

def make_box( world, position=(0,0), dim=(1,1), density=1, friction=0.0, restitution=0.1 ):

	body = world.CreateDynamicBody( position=position )
	shape = body.CreatePolygonFixture( box=dim, density=density, friction=friction, restitution=restitution )

	return body

def make_poly( world, position=(0,0), vertices=[], density=1, friction=0.0, restitution=0.1 ):

	body = world.CreateDynamicBody( position=position )
	shape = body.CreatePolygonFixture( vertices=vertices, density=density, friction=friction, restitution=restitution )

	return body

def apply_impulse( body, impulse, pos=None ):

	if pos is None:
		pos = body.worldCenter

	body.ApplyLinearImpulse( impulse, pos )
