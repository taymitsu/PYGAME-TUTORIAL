from random import randint 
from gameObject import GameObject
import pygame

class Apple(GameObject):
    def __init__(self):
        x = randint(50, 400)
        super(Apple, self).__init__(x, 0, 'apple.png')
        self.dy = (randint(0, 200) / 100) + 1

    def move(self):
        self.x += self.dx
        self.y += self.dy

        if self.y > 500:
            self.reset()

    def reset(self):
        self.x = randint(50, 400)
        self.y = -64