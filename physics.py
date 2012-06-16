from Box2D import b2World

def get_world():
	
	world = b2World( gravity = (0,0), doSleep = False )

	return world
