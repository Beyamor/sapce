from Box2D import b2World, b2BodyDef, b2Vec2

def get_world():
	
	world = b2World( gravity=(0,0), doSleep=False )
	return world

def make_box( world, position=(0,0), dim=(1,1), density=1, friction=0.1, restitution=0.1 ):

	body = world.CreateDynamicBody( position=position )
	shape = body.CreatePolygonFixture( box=dim, density=density, friction=friction, restitution=restitution )

	return body

def make_poly( world, position=(0,0), vertices=[], density=1, friction=0.1, restitution=0.1 ):

	body = world.CreateDynamicBody( position=position )
	shape = body.CreatePolygonFixture( vertices=vertices, density=density, friction=friction, restitution=restitution )

	return body

def apply_impulse( body, impulse ):

	body.ApplyLinearImpulse( impulse, body.worldCenter )
