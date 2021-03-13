import pygame, sys
from time import sleep
from random import randrange
from player import Player
from food import Food
from enemy import Enemy
pygame.init()
pygame.display.set_caption('fish in a pond')



#     if r >= 0.5:
#         x = randrange(0, width)
#     else:
#         x = randrange(width*-1, 0)



size = width, height = 1000, 840
speed = [2, 2]
black = 179, 179, 179

highscore = 0

screen = pygame.display.set_mode(size)




font = pygame.font.SysFont("Arial", 25)

def gameloop():
    #player
    dot = Player(width, height)

    #enemies
    enemylist = [] 
    for n in range(0, 2):
        enemylist.append(Enemy(width, height, dot.radius))

    #food
    foodlist = []
    for n in range(0, 2):
        foodlist.append(Food(width, height, dot.radius))

    pygame.mouse.set_visible(False)

    gameloop.score = 0
    gameover = False
    while not gameover:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
        screen.fill(black)
        dot.rect = pygame.draw.circle(screen, dot.color, (dot.x, dot.y), dot.radius)
        for n in range(0, len(enemylist)):
            bot = enemylist[n]
            bot.rect = pygame.draw.circle(screen, bot.color, (bot.x, bot.y), bot.radius)
            bot.move()
            notdead = not dot.rect.colliderect(bot.rect)
            if notdead:
                out = bot.x < 0 or bot.x > width or bot.y < 0 or bot.y > width
                if out:
                    del enemylist[n]
                    enemylist.append(Enemy(width, height, dot.radius))
            else:
                gameover = True
                break
        
        mx, my = pygame.mouse.get_pos()
        if pygame.mouse.get_pos() != (0, 0):
            dot.x = mx
            dot.y = my

        for n in range(0, len(foodlist)):
            got = foodlist[n]
            got.rect = pygame.draw.circle(screen, got.color, (got.x, got.y), got.radius)
            got.move()
            out = got.x<0 or got.x>width or got.y<0 or got.y>height
            eaten = dot.rect.colliderect(got.rect)
            if out or eaten:
                del foodlist[n]
                foodlist.append(Food(width, height, dot.radius))
            if eaten:
                dot.radius += 2
                gameloop.score += 1
            
    

        pygame.display.flip()

#start screen
screen.fill(black)
startword = font.render("Click anywhere to start.", True, (0, 0, 0))
start_rect = startword.get_rect(center=(width/2, height/2))
screen.blit(startword, start_rect)
pygame.display.flip()

#play
while 1:
    # gameloop()
    
    # pygame.mouse.set_visible(True)
    # screen.fill(black)
    # text = font.render("Game over! Click anywhere to restart.", True, (0, 0, 0))
    # text_rect = text.get_rect(center=(width/2, height/2))
    # screen.blit(text, text_rect)
    # text2 = font.render("Your score is: "+str(gameloop.score)+"!", True, (0, 0, 0))
    # text_rect2 = text.get_rect(center=(width/2, (height/2)+20))
    # screen.blit(text2, text_rect2)
    # pygame.display.flip()
    

    restart = False
    while not restart:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP: 
                restart = True
        sleep(0.1)
    
    gameloop()
    if gameloop.score>highscore:
        highscore = gameloop.score

    pygame.mouse.set_visible(True)
    screen.fill(black)
    text = font.render("Game over! Click anywhere to restart.", True, (0, 0, 0))
    text_rect = text.get_rect(center=(width/2, height/2))
    screen.blit(text, text_rect)
    text2 = font.render("Your score is: "+str(gameloop.score), True, (0, 0, 0))
    text_rect2 = text2.get_rect(center=(width/2, (height/2)+20))
    screen.blit(text2, text_rect2)
    text3 = font.render("High score: "+str(highscore), True, (0, 0, 0))
    text_rect3 = text3.get_rect(center=(width/2, (height/2)+40))
    screen.blit(text3, text_rect3)
    pygame.display.flip()



#make score var in game loop
#increment when eaten
#display below game over
#if high score, init outside gameloop
#if score>high score, high score = score