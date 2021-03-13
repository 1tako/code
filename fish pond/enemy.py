from random import randrange
from other import Other
class Enemy(Other):
    color = (161, 38, 38)
    def __init__(self, width, height, playersize):
        self.radius = randrange(playersize+5, playersize+20)
        super(Enemy, self).__init__(width, height)
