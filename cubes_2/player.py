import pygame

class Player(pygame.sprite.Sprite):
    """
    Human-controlled main character

    Attributes
    ----------
    health : int
    x : int
    y : int
    aimX : int
    aimY : int
    rect: pygame.Rect


    Methods
    -------
    attack(attack_name)
        use the given attack, which can be either a melee or ranged attack
        if melee, damage any sprites in range
        elif ranged, create projectile pointed at aimX and aimY

    ability(ability_name)
        use the given ability pointed at aimX and aimY

    move(direction)
        move Player.rect by a certain amount depending on the given direction
    """
    x = 10
    y = 10
    width = 15
    height = 30
    step = 15

    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        screen = pygame.display.get_surface()
        # self.rect = pygame.Rect(self.x, self.y, 15, 30)

    def move(self, direction):
        """ Update player rectangle based on current x and y """
        if direction == "up":
            self.rect.move_ip(0, -self.step)
        elif direction == "down":
            self.rect.move_ip(0, self.step)
        elif direction == "left":
           self.rect.move_ip(-self.step, 0)
        elif direction == "right":
            self.rect.move_ip(self.step, 0)

    # def draw(self, surface):
    #     pygame.draw.rect(surface, (156, 150, 228), self.rect)
