#import and initialize pygame
import pygame
pygame.init()

# Configure the screen
#dimension (heigh and width) can be entered as TRUPLE or LIST 
screen = pygame.display.set_mode([500, 500])


# Creat the game loop
running = True 
while running: 
	# Looks at events 
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	
	# Clear the screen
	screen.fill((255, 255, 255))
	# Draw a circle
	color = (255, 0, 255)
	position = (250, 250)
	pygame.draw.circle(screen, color, position, 75)
	# Update the display screen
	pygame.display.flip()

# Clear the screen
screen.fill((255, 255, 255))

# Your drawing here

# Update the display
pygame.display.flip()

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