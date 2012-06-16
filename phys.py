from Box2D import b2World, b2BodyDef, b2Vec2

def get_world():
	
	world = b2World( gravity = (0,0), doSleep = False )

	return world

def make_poly( world, position=(0,0), vertices=[] ):

	body = world.CreateDynamicBody( position=position )
	shape = body.CreatePolygonFixture( vertices=vertices )

	return body
