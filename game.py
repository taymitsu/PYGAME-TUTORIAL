#import and initialize pygame
import pygame
pygame.init()
from gameObject import GameObject 
from watermelon import Watermelon
from strawb import Strawb
from player import Player


# Configure the screen
#dimension (heigh and width) can be entered as TRUPLE or LIST 
screen = pygame.display.set_mode([500, 500])
clock = pygame.time.Clock()

watermelon = Watermelon()
strawb = Strawb()
player = Player()


# Creat the game loop
running = True 
while running: 
	#Looks at events 
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				running = False
			elif event.key == pygame.K_LEFT:
				player.left()
			elif event.key == pygame.K_RIGHT:
				player.right()
			elif event.key == pygame.K_UP:
				player.up()
			elif event.key == pygame.K_DOWN:
				player.down()

screen.fill((255, 255, 255))
#draw watermelon
watermelon.move()
watermelon.render(screen)

strawb.move()
strawb.render(screen)
# Draw player 
player.move()
player.render(screen)

# Update the window
pygame.display.flip()
clock.tick(60)