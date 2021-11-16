import pygame
from random import randint, random, choice
from gameObject import GameObject

lanes = [93, 218, 343]

class Bomb(GameObject):
    def __init__(self):
        super(Bomb, self).__init__(0, 0, 'bomb.gif')
        self.dx = 0
        self.dy = (randint(0, 200) / 100) + 1
        self.reset() # call reset here! 

    def move(self):
        self.x += self.dx
        self.y += self.dy
        # Check the y position of the apple
        if self.y > 500 or self.x > 500: 
            self.reset()

    # add a new method
    def reset(self):
        self.dx = 0
        self.dy = 0
        direction = choice(['down', 'right'])
        if direction == 'down':
            self.x = choice(lanes)
            self.y = -64
            self.dy = (randint(0, 200) / 100) + 1
        elif direction == 'right':
            self.x = -64
            self.y = choice(lanes)
            self.dx = (randint(0, 200) / 100) + 1