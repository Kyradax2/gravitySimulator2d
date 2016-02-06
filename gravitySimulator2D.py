#Jerome Paris
#projet POO2

try:
#system
        import sys
	sys.path.append("modules") #for PyGame
        import random
        import math
        import os
        import getopt
	import time
#pyGame
        import pygame
        from socket import *
        from pygame.locals import *
except ImportError, err:
        print "couldn't load module. %s" % (err)
        sys.exit(2)

#screen size
screenSize = [800, 600]

#turns float into integer
def rndint(num):
	return int(round(num))

#load image and return image object
def load_png(name):
        fullname = os.path.join('data', name)
        try:
                image = pygame.image.load(fullname)
                if image.get_alpha is None:
                        image = image.convert()
                else:
                        image = image.convert_alpha()
        except pygame.error, message:
                print 'Cannot load image:', fullname
                raise SystemExit, message
        return image, image.get_rect()

#the ball class affected by gravity
class Ball(object):
	def __init__(self, xy = None, radius = None, dx = None, dy = None):
		if xy == None:
			self.xy = [random.uniform(100, screenSize[0] - 100), random.uniform(100, screenSize[1] - 100)]
		else:
			self.xy = xy
		if radius == None:
			self.radius = random.uniform (3, 5)
		else:
			self.radius = radius
		if dx == None:
			self.dx = random.uniform (-50, 50)
		else:
			self.dx = dx
		if dy == None:
			self.dy = random.uniform (-50, 50)
		else:
			self.dy = dy

	def update(self):
		if ((self.xy[1] + self.radius) < screenSize[1]):
			self.xy[0] += self.dx
			self.xy[1] += self.dy
		self.dx -= self.dx/10
		self.dy += 1

	def draw(self, surface):
		pygame.draw.circle(surface, (255,255,127), (rndint(self.xy[0]), rndint(self.xy[1])), rndint(self.radius), 0)

def main():
	#centers the window on the computer screen
	os.environ['SDL_VIDEO_CENTERED'] = '1'

        #initialise screen
        pygame.init()
        screen = pygame.display.set_mode(screenSize)
        pygame.display.set_caption('gravitySimulator2D')

	#fill background
	global background
	background = pygame.display.set_mode(screenSize)
	background = background.convert()
	background.fill((0, 0, 0))

	#set caption
	fontPath = 'data/coders_crux.ttf'
	font0 = pygame.font.Font(fontPath, 72)
	text0 = font0.render("gravitySimulator2D", 1, (255, 255, 255))
	textpos0 = text0.get_rect(center = (400, 100))
	background.blit(text0, textpos0)
	font1 = pygame.font.Font(fontPath, 36)
	text1 = font1.render("press ENTER to continue", 1, (255, 255, 255))
	textpos1 = text1.get_rect(center = (400, 300))
	background.blit(text1, textpos1)
	font2 = pygame.font.Font(None, 54)
	text2 = font2.render("Jerome", 1, (255, 255, 255))
	textpos2 = text2.get_rect(center = (150, 500))
	background.blit(text2, textpos2)
	font3 = pygame.font.Font(None, 54)
	text3 = font3.render("Paris", 1, (255, 255, 255))
	textpos3 = text3.get_rect(center = (150, 550))
	background.blit(text3, textpos3)

	#some variables
	start = 0
	ballsCount = 100

	#ignore mouse motion (greatly reduces resources when not needed)
	pygame.event.set_blocked(pygame.MOUSEMOTION)

	#first loop, screen before starting the game
	while start == 0:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == KEYDOWN:
				if event.key == K_RETURN:
					start = 1		
		screen.blit(background, (0, 0))
		pygame.display.flip()

	#deleting captions
	background.fill((0, 0, 0))
	screen.blit(background, (0, 0))
	pygame.display.flip()

	#creating objects
	balls = [Ball() for i in range (ballsCount)]

	#initialise clock
	clock = pygame.time.Clock()

	while True:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

		background.fill((0, 0, 0))


		for b in balls:
			b.update()
			b.draw(background)

		screen.blit(background, (0, 0))
		pygame.display.flip()

if __name__ == "__main__":
	main()
