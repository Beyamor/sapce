import pygame
from pygame import event as events, QUIT, KEYDOWN
from pygame.time import get_ticks, wait
from gfx.draw import get_screen, finish_frame, start_frame
from gfx.view import PhysView
from gfx.image import get_image
import gfx.draw
from arena import Arena
from ship.ship import Ship
from ship.blueprint import BlueprintFactory
from ship.pilot import Pilot
from debug.phys_debug import PhysDebugRenderer
from gfx.parallax import Parallaxor
from geometry import Rect
from space import Spacilizer

FPS = 30
IDEAL_FRAME_TIME = 1000 / FPS
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def main_loop():

	class Context: pass
	context = Context()

	screen = get_screen( SCREEN_WIDTH, SCREEN_HEIGHT )
	context.view = PhysView( screen )

	parallax = Parallaxor(context.view)
	parallax.push_background(get_image("stars1.png"))
	parallax.push_background(get_image("stars2.png"))
	parallax.push_background(get_image("stars3.png"))

	arena = Arena()
	context.world = arena.world

	pdr = PhysDebugRenderer( context.world )

	factory = BlueprintFactory()
	ship = Ship( context, Pilot(), factory.make() )
	#ship = Ship(context, Pilot(), factory.make_thruster_ship())
	arena.add( ship )
	arena.add(Ship(context, Pilot(), factory.make(), position=(2,2)))
	arena.add(Ship(context, Pilot(), factory.make(), position=(2,8)))
	arena.add(Ship(context, Pilot(), factory.make(), position=(8,2)))
	arena.add(Ship(context, Pilot(), factory.make(), position=(8,8)))

	space = Spacilizer(context.view)

	playing = True
	isPaused = True
	currentTime = get_ticks()
	while playing:

		previousTime = currentTime
		currentTime = get_ticks()
		deltaTime = currentTime - previousTime

		for event in events.get():
			if event.type == QUIT:
				playing = False

			if event.type is KEYDOWN and event.key is pygame.K_SPACE:
				isPaused = not isPaused


		if not isPaused:
			context.world.Step(deltaTime * 0.001, 10, 10)

		for entity in arena.entities:
			entity.update( deltaTime )
		context.view.center(ship.get_position())

		start_frame( screen )
		space.draw()
		for entity in arena.entities:
			entity.draw()
		finish_frame( screen )

		elapsedTime = get_ticks() - currentTime
		if elapsedTime < IDEAL_FRAME_TIME:
			wait( IDEAL_FRAME_TIME - elapsedTime )	

if __name__ == "__main__":
	main_loop()
