from random import randrange
from other import Other
class Food(Other):
    color = (54, 169, 73)
    def __init__(self, width, height, playersize):
        self.radius = randrange(4, playersize-5)
        super(Food, self).__init__(width, height)
    
