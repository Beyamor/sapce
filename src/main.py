import pygame
from pygame import event as events, QUIT, KEYDOWN
from pygame.time import get_ticks, wait
from gfx.draw import get_screen, finish_frame, start_frame
from arena import Arena
from ship.ship import Ship
from ship.blueprint import BlueprintFactory
from ship.pilot import Pilot
from gfx.draw import get_image, image
from debug.phys_debug import PhysDebugRenderer
import gfx.draw

FPS = 30
IDEAL_FRAME_TIME = 1000 / FPS
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def main_loop():

	class Context: pass
	context = Context()
	context.screen = get_screen( SCREEN_WIDTH, SCREEN_HEIGHT )

	arena = Arena()
	context.world = arena.world

	pdr = PhysDebugRenderer( context.world )

	ship = Ship( context, Pilot(), BlueprintFactory().make() )
	arena.add( ship )

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
			context.world.Step( deltaTime * 0.001, 10, 10 )

		for entity in arena.entities:
			entity.update( deltaTime )

		start_frame( context.screen )
		for entity in arena.entities:
			entity.draw()
		#pdr.draw( context.screen )
		finish_frame( context.screen )

		elapsedTime = get_ticks() - currentTime
		if elapsedTime < IDEAL_FRAME_TIME:
			wait( IDEAL_FRAME_TIME - elapsedTime )	

if __name__ == "__main__":
	main_loop()
