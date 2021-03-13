from random import random, randrange
class Other:
    def __init__(self, width, height):
        #makes new food spawn at edge of screen
        self.speed = randrange(2, 5)
        x, y = randrange(0, width), randrange(0, height)
        edge = randrange(1, 5)

        #1 is top, clockwise from 1
        if edge == 1:
            y = 0
            self.dir = "down"
        elif edge == 2:
            x = width
            self.dir = "left"
        elif edge == 3:
            y = height
            self.dir = "up"
        elif edge == 4:
            x = 0
            self.dir = "right"

        self.x = x
        self.y = y
    
    def move(self):
        if self.dir == "down":
            self.y += self.speed
        elif self.dir == "left":
            self.x -= self.speed
        elif self.dir == "up":
            self.y -= self.speed
        elif self.dir == "right":
            self.x += self.speed