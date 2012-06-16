from pygame.time import get_ticks, wait

FPS = 30
IDEAL_FRAME_TIME = 1000 / FPS

def mainLoop():

	currentTime = get_ticks()

	while True:

		previousTime = currentTime
		currentTime = get_ticks()
		deltaTime = currentTime - previousTime

		elapsedTime = get_ticks() - currentTime
		if elapsedTime < IDEAL_FRAME_TIME:
			wait( IDEAL_FRAME_TIME - elapsedTime )	

if __name__ == "__main__":
	mainLoop()
