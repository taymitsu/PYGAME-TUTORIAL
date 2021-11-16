from random import randint, random, choice
from gameObject import GameObject
import pygame
lanes = [93, 218, 343]

class Strawberry(GameObject):
    def __init__(self):
        super(Strawberry, self).__init__(0, 0, 'strawb.png')
        self.dx = 0
        self.dy = (randint(0, 200) / 100) + 1
        self.reset() # call reset here! 

    def move(self):
        self.x += self.dx
        self.y += self.dy
        # Check the y position of the apple
        if self.y > 500: 
            self.reset()

    # add a new method
    def reset(self):
        self.x = choice(lanes)
        self.y = -64