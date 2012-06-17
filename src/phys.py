import math
from Box2D import b2World, b2BodyDef, b2Vec2

def make_world():
	"""
	Creates a new physical world.

	Returns:
		The newly created world.
	"""
	world = b2World(gravity=(0,0), doSleep=False)
	return world


def make_impulse(direction, magnitude):
	"""
	Makes a physical impulse.

	Args:
		direction: The direction of the impulse in degrees.
		magnitude: The magnitude of the impulse.

	Returns:
		The impulse tuple.
	"""
	return (math.cos(math.radians(direction)) * magnitude,
			math.sin(math.radians(direction)) * magnitude)


def make_box(world, position=(0,0), dim=(1,1), density=1, friction=0.0, restitution=0.1, rotation=0):
	"""
	Creates a box in the physical world.

	Returns:
		The new box in the world.
	"""
	dim = (dim[0] * 0.5, dim[1] * 0.5)
	body = world.CreateDynamicBody(position=position, angle=math.radians(rotation))
	shape = body.CreatePolygonFixture(box=dim, density=density, friction=friction, restitution=restitution)

	return body


def weld(world, b1, b2):
	"""
	Fuses together two bodies in a world.

	Args:
		world: The world the two bodies inhabit.
		b1: The first body.
		b2: The second body.
	"""
	world.CreateWeldJoint(
			bodyA=b1,
			bodyB=b2,
			anchor= (b1.worldCenter + b2.worldCenter) / 2)


def apply_impulse(body, impulse, pos=None):
	"""
	Applies an impulse to a body.

	Args:
		body: The body to which the impulse is applied.
		impulse: The applied impulse.
		pos: The position at which the impulse is applied,
			defaulting to the body's world center.
	"""
	if pos is None:
		pos = body.worldCenter

	body.ApplyLinearImpulse(impulse, pos)
