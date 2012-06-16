from pygame import event as events, QUIT
from pygame.time import get_ticks, wait
from draw import get_screen, finish_frame, start_frame
from phys import get_world
from flock import Jucoid

FPS = 30
IDEAL_FRAME_TIME = 1000 / FPS
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def main_loop():

	class Context: pass
	context = Context()
	context.screen = get_screen( SCREEN_WIDTH, SCREEN_HEIGHT )
	context.world = get_world()

	jucoid = Jucoid( context )

	playing = True
	currentTime = get_ticks()
	while playing:

		previousTime = currentTime
		currentTime = get_ticks()
		deltaTime = currentTime - previousTime

		for event in events.get():
			if event.type == QUIT:
				playing = False

		context.world.Step( deltaTime * 0.001, 10, 10 )

		jucoid.update( deltaTime )

		start_frame( context.screen )
		jucoid.draw()
		finish_frame( context.screen )

		elapsedTime = get_ticks() - currentTime
		if elapsedTime < IDEAL_FRAME_TIME:
			wait( IDEAL_FRAME_TIME - elapsedTime )	

if __name__ == "__main__":
	main_loop()
