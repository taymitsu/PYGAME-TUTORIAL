from random import randint, random, choice
from gameObject import GameObject
import pygame

class Strawberry(GameObject):
    def __init__(self):
        self.positions = [93, 218, 343]
        x = random.choice(self.positions)
        super(Strawberry, self).__init__(0, 0, 'strawb.png')
        self.dx = 0
        self.dy = (randint(0, 200) / 100) + 1
        self.reset()

    def move(self):
        self.x += self.dx
        self.y += self.dy
        # Check the y position of the apple
        if self.y > 500: 
            self.reset()

    #New Method
    def reset(self):
        self.x = random.choice(self.positions)
        self.y = -64