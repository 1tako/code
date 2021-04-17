import pygame, sys, os
from spritesheet import SpriteSheet
from random import randrange

from player import Player

"""
List of Classes/Objects in the game:
1) what data does the class need to keep track of?
2) what actions can the class perform?

projectile
    type <- how to draw it
    damage
    location: x, y
    direction/angle
    move()
    collide()

environment_object
    type <- ex: tree, lava, water
    location: x, y

map ??
info panel ??
inventory ??

"""

##
# Camera System
#
# find objects to draw on the screen:
# 1) x within cameraX to cameraX + width
# 2) y within cameraY to cameraY + height


##
# Colors
black = 0, 0, 0
grey = 179, 179, 179
white = 255, 255, 255
red = 255, 0, 0
green = 0, 255, 0
blue = 0, 0, 255


##
# Initialize pygame
pygame.init()
pygame.display.set_caption('Title Here')
screen = pygame.display.set_mode()
pygame.display.flip()
main_dir = os.path.split(os.path.abspath(__file__))[0]
# pygame.display.toggle_fullscreen()
# Get screen height and width using:
#   screen.get_width()
#   screen.get_height()

##
# Load images



##
# Setup Game Objects
sprites = pygame.sprite.Group()

user = Player()

clock = pygame.time.Clock()


def main():
    """
    """
    print("start main()")

    # 1. start_screen - runs until user continues
    print("start start_screen()")
    # start_screen()
    print("end start_screen()")

    while True:
        # 2. game_loop - runs until player death
        print("start game_loop()")
        game_loop()
        print("end of game_loop()")

        # 3. death_screen - runs until user continues
        print("start death_screen()")
        new_game = death_screen()
        print("end death_screen()")

        # 4-a. Quit
        if not new_game:
            print("quitting...")
            pygame.quit()
            break

        # 4-a. If new_game is True restart game_loop
        print("restarting...")

#lookup midtop

def game_loop():
    """ 
    """
    alive = True
    while alive:
        clock.tick(60)

        # handle input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                alive = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                return

        # clear the screen
        screen.fill(black)
        # pygame.display.flip()


        # player controls
        keys_pressed = pygame.key.get_pressed()
        # print("keys pressed:", keys_pressed)
        if keys_pressed[pygame.K_w]:
            user.move("up")
        if keys_pressed[pygame.K_a]:
            user.move("left")
        if keys_pressed[pygame.K_s]:
            user.move("down")
        if keys_pressed[pygame.K_d]:
            user.move("right")

        # draw sprites
        # sprites.update()
        # user.draw(screen)
        screen.blit(user.image, user.rect)
        # pygame.display.update()
        pygame.display.flip()


def start_screen():
    """ 
    """
    screen.fill(black)
    startword = font.render(".", True, (0, 0, 0))
    #start_rect = startword.get_rect(center=(width/2, height/2))
    #screen.blit(startword, start_rect)
    pygame.display.flip()


def death_screen():
    """ returns true if player wants to start a new game
    """
    return False

if __name__ == "__main__":
    main()
