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
from ents.bullet import Bullet

FPS = 30
IDEAL_FRAME_TIME = 1000 / FPS
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def main_loop():
	screen = get_screen(SCREEN_WIDTH, SCREEN_HEIGHT)

	arena = Arena(screen)

	arena.make(Ship, position=(5,5))
	arena.make(Ship, position=(2,2))
	arena.make(Ship, position=(2,8))
	arena.make(Ship, position=(8,2))
	arena.make(Ship, position=(8,8))
	arena.make(Bullet)

	space = Spacilizer(arena.view)

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

			elif event.type is KEYDOWN:
				if event.key is pygame.K_SPACE:
					isPaused = not isPaused
				elif event.key is pygame.K_RETURN:
					ship = arena.focus_on_next_entity()

		arena.update(deltaTime)
		for entity in arena.entities:
			entity.update(deltaTime)

		start_frame(screen)
		space.draw()
		for entity in arena.entities:
			entity.draw()
		finish_frame(screen)

		elapsedTime = get_ticks() - currentTime
		if elapsedTime < IDEAL_FRAME_TIME:
			wait(IDEAL_FRAME_TIME - elapsedTime)	

if __name__ == "__main__":
	main_loop()
