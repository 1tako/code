import pygame, os
from spritesheet import SpriteSheet

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

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        screen = pygame.display.get_surface()
        # self.rect = pygame.Rect(self.x, self.y, 15, 30)

        # Each sprite is 16x21 pixels starting at location 0,6 in the file
        main_dir = os.path.split(os.path.abspath(__file__))[0]
        character_ss = SpriteSheet(main_dir+'/graphics/character.png')
        self.image_front = character_ss.image_at((0, 6, 16, 21))
        self.image_front = pygame.transform.scale(self.image_front, (48, 63))
        self.image_back = character_ss.image_at((0, 69, 16, 21))
        self.image_back = pygame.transform.scale(self.image_back, (48, 63))
        self.image_left = character_ss.image_at((0, 101, 16, 21))
        self.image_left = pygame.transform.scale(self.image_left, (48, 63))
        self.image_right = character_ss.image_at((0, 38, 16, 21))
        self.image_right = pygame.transform.scale(self.image_right, (48, 63))
        self.image = self.image_front
        self.rect = self.image.get_rect()

    def move(self, direction):
        """ Update player rectangle based on current x and y """
        if direction == "up":
            self.rect.move_ip(0, -self.step)
            self.image = self.image_back
        elif direction == "down":
            self.rect.move_ip(0, self.step)
            self.image = self.image_front
        elif direction == "left":
           self.rect.move_ip(-self.step, 0)
           self.image = self.image_left
        elif direction == "right":
            self.rect.move_ip(self.step, 0)
            self.image = self.image_right

    # def draw(self, surface):
    #     pygame.draw.rect(surface, (156, 150, 228), self.rect)
