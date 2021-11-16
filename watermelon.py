from random import randint
import random 
from gameObject import GameObject
import pygame

class Watermelon(GameObject):
    def __init__(self):
        self.positions = [93, 218, 343]
        y = random.choice(self.positions)
        super(Watermelon, self).__init__(x, 0, 'watermelon.png')
        self.dy = (randint(0, 200) / 100) + 1

    def move(self):
        self.x += self.dx
        self.y += self.dy

        if self.y > 500:
            self.reset()

    def reset(self):
        self.y = random.chouce(self.positions)
        self.x = -64