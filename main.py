from pygame import event as events, QUIT
from pygame.time import get_ticks, wait
from draw import get_screen
from flock import Jucoid

FPS = 30
IDEAL_FRAME_TIME = 1000 / FPS
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def mainLoop():

	screen = get_screen( SCREEN_WIDTH, SCREEN_HEIGHT )

	jucoid = Jucoid()

	playing = True
	currentTime = get_ticks()
	while playing:

		previousTime = currentTime
		currentTime = get_ticks()
		deltaTime = currentTime - previousTime

		for event in events.get():
			if event.type == QUIT:
				playing = False		

		elapsedTime = get_ticks() - currentTime
		if elapsedTime < IDEAL_FRAME_TIME:
			wait( IDEAL_FRAME_TIME - elapsedTime )	

if __name__ == "__main__":
	mainLoop()
