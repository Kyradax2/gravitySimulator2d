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

#turn float into integer
def rndint(num):
	return int(round(num))

#the ball class affected by gravity
class Ball:
	def __init__(self, xy = None, radius = None, dx = None, dy = None):
		if xy == None:
			self.xy = [random.uniform(100, screenSize[0] - 100), random.uniform(100, screenSize[1] - 500)]
		else:
			self.xy = xy
		if radius == None:
			self.radius = random.uniform (3, 5)
		else:
			self.radius = radius
		if dx == None:
			self.dx = random.uniform (-15, 15)
		else:
			self.dx = dx
		if dy == None:
			self.dy = random.uniform (-5, 5)
		else:
			self.dy = dy

#moves the ball
	def update(self):
		#apply the ball related force vector to the current position
		self.xy[0] += self.dx
		self.xy[1] += self.dy
		#check if the ball hits the ground
		if ((self.xy[1] + self.radius) > screenSize[1]):
			self.dy *= -0.7
			self.dx -= self.dx/10
		else:
			self.dy += 0.3
			self.dy -= self.dy/100
			self.dx -= self.dx/100
		#check if the ball hits the screen's sides
		if ((self.xy[0] + self.radius) < 0 or (self.xy[0] + self.radius) > screenSize[0]):
			self.dx *= -1
		#process the event related to a collision with the Board class
		if ((self.xy[0] > board.xy[0] - self.radius and self.xy[0] < board.xy[0] + self.radius or self.xy[0] > board.xy[0] + board.width - self.radius and self.xy[0] < board.xy[0] + board.width + self.radius) and self.xy[1] > board.xy[1] and self.xy[1] < board.xy[1] + board.height):
			self.dx *= -1
		if ((self.xy[1] > board.xy[1] - self.radius and self.xy[1] < board.xy[1] + self.radius) and self.xy[0] > board.xy[0] and self.xy[0] < board.xy[0] + board.width):
			if (self.dy < 1 and self.dy > -1):
				self.dy = 0
			else:
				self.dy *= -0.7
			self.dx -= self.dx/10

	def draw(self, surface):
		pygame.draw.circle(surface, (255,255,127), (rndint(self.xy[0]), rndint(self.xy[1])), rndint(self.radius), 0)

#an immobile object class where the balls can collide
class Board:
	def __init__(self, xy = None, width = None, height = None):
		if xy == None:
			self.xy = (250, 400)
		else:
			self.xy = xy
		if width == None:
			self.width = 300
		else:
			self.width = width
		if height == None:
			self.height = 50
		else:
			self.height = height

	def draw(self, surface):
		pygame.draw.rect(surface, (255,127,255), (self.xy[0], self.xy[1], self.width, self.height), 0)

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
	ballsCount = 200

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
	global board #declared global because used in the Ball() class
	board = Board()

	#initialise clock
	clock = pygame.time.Clock()

	#start the gravity simulation
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
		board.draw(background)

		screen.blit(background, (0, 0))
		pygame.display.flip()

if __name__ == "__main__":
	main()
