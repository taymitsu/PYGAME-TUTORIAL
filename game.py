#import and initialize pygame
import pygame
pygame.init()
from gameObject import GameObject 
from random import randint
from apple import Apple

# Configure the screen
#dimension (heigh and width) can be entered as TRUPLE or LIST 
screen = pygame.display.set_mode([500, 500])
ara = GameObject(120, 300, 'ara.png')
apple = Apple()
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
    #Draw circle
	for i in range(0, 9):
		color = (255, 0, 255)
		x = ((i % 3) * 175) + 75
		y = (int(i / 3) * 175) + 75
		position = (x, y)
		#Update screen display 
		pygame.draw.circle(screen, color, position, 75)
	pygame.display.flip()

screen.fill((255, 255, 255))
#draw apple
apple.move()
apple.render(screen)

# Draw player 
player.move()
player.render(screen)

# Update the window
pygame.display.flip()
	
	# Clear the screen
	#screen.fill((255, 255, 255))
	# Draw a circle
	#color = (255, 0, 255)
	#position = (250, 250)
	#pygame.draw.circle(screen, color, position, 75)
	# Update the display screen
	#pygame.display.flip()

#(255, 0, 0) - RED has no Green or Blue
#(0, 255, 0) - GREEN has no Red or Blue
#(0, 0, 255) - BLUE has no Red or Green
#(255, 255, 0) - YELLOW is all Red and Green and no Blue
#(0, 255, 255) - CYAN is Green and Blue with no Red
#(255, 0, 255) - FUSCHIA has no Green.
#(255, 255, 255) - We get white when all of the values are 255
#(0, 0, 0) - We get black when all of the values are 0
#(100, 100, 100) - If all of the values are equal we get gray
#(250, 141, 7) - A nice shade of orange.
#(25, 184, 22) - A nice shade of green.
#(20, 121, 199) - A nice shade of green.
#position = (250, 250) - Puts the circle in the center.
#position = (0, 250) - Places the circle at the left edge. Since the pygame.draw.circle() method draws from the center the circle is half off the screen and its center is at the left edge.
#position = (0, 0) - Place the center of the circle at the top left corner. left edge.
#position = (400, 300) - Place the circle near the lower right.