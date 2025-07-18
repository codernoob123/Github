import pygame
import random
import time

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

pygame.init()

width = 800
length = 500

screen = pygame.display.set_mode((width,length))
pygame.display.set_caption("Clicking Game")

background = Background('menu.jpg', [0,0])
background2 = Background('menu2.jpg', [0,0])
ball = pygame.image.load('ball.png')

running = True
not_starting = True
Isitend = False

score = 0
cir_x = 0
cir_y = 0
start_time = 0
second = 0
game_time = 20

try:
    with open("highscore.txt", "r") as file:
        high_score = int(file.read())
    if high_score < score:
        high_score = score
except:
    with open("highscore.txt", "w") as file:
        file.write(str(score))

font = pygame.font.Font('freesansbold.ttf', 18)
menufont = pygame.font.Font('freesansbold.ttf', 40)
namefont = pygame.font.Font('freesansbold.ttf', 60)
endfont = pygame.font.Font('freesansbold.ttf', 50)
endfont_2 = pygame.font.Font('freesansbold.ttf',30)

name_text = namefont.render('Clicking Game', True, (255,255,255), (0,0,0))
name_rect = name_text.get_rect()
name_rect.center = (400,100)

gameover_text = endfont.render('GAME OVER', True, (255,255,255), (0,0,0))
gameover_rect = gameover_text.get_rect()
gameover_rect.center = (400,150)

start_text = menufont.render('START', True, (255,255,255), (0,0,0))
startRect = start_text.get_rect()
startRect.center =  (width/2, length/2)

retry_text = endfont_2.render("Retry", True, (255,255,255), (0,0,0))
retry_rect = retry_text.get_rect()
retry_rect.center = (width/2, length/2 + 45)

home_text = endfont_2.render("Back To Home", True, (255,255,255), (0,0,0))
home_rect = home_text.get_rect()
home_rect.center = (width/2, length/2 + 90)

while running:

    mouse_x, mouse_y = pygame.mouse.get_pos()

    second = int((pygame.time.get_ticks() - start_time) / 1000)
    time_text = font.render("Time left: " + str(game_time - second), True, (0,255,0), (0,0,255))
    timeRect = time_text.get_rect()
    timeRect.center = (720,20)

    hscore_text = font.render('High Score: ' + str(high_score), True, (0, 255, 0), (0,0,255))
    textRect2 = hscore_text.get_rect()
    textRect2.center = (80,40)

    score_text = font.render('Score: ' + str(score), True, (0, 255, 0), (0,0,255))
    textRect = score_text.get_rect()
    textRect.center = (52,20)

    score_end_text = endfont_2.render("Score: " + str(score), True, (255,255,255), (0,0,0))
    score_end_rect = score_end_text.get_rect()
    score_end_rect.center = (width/2, length/2 - 40)

    hscore_end_text = endfont_2.render("High Score: " + str(high_score), True, (255,255,255), (0,0,0))
    hscore_end_rect = hscore_end_text.get_rect()
    hscore_end_rect.center = (width/2, length/2)

    if not_starting == True and Isitend == False:
        screen.fill("white")
        screen.blit(pygame.transform.scale(background.image, (width,length)), background.rect)
        screen.blit(start_text, startRect)
        screen.blit(name_text,name_rect)

    elif not_starting == False and Isitend == False:
        screen.fill("white")
        screen.blit(pygame.transform.scale(background2.image, (width,length)), background2.rect)
        screen.blit(score_text, textRect)
        screen.blit(hscore_text,textRect2)
        screen.blit(time_text, timeRect)
        pygame.draw.circle(screen, (255,0,0), (cir_x,cir_y), 35)
        if second > game_time:
            Isitend = True

    else:
        screen.fill("white")
        screen.blit(pygame.transform.scale(background.image, (width,length)), background.rect)
        screen.blit(gameover_text,gameover_rect)
        screen.blit(hscore_end_text,hscore_end_rect)
        screen.blit(score_end_text,score_end_rect)
        screen.blit(retry_text,retry_rect)
        screen.blit(home_text,home_rect)


    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if startRect.collidepoint((mouse_x,mouse_y)) and not_starting == True:
                    not_starting = False
                    start_time = pygame.time.get_ticks()
                    score = 0
                elif (mouse_x >= (cir_x - 35) and mouse_x <= (cir_x + 35)) and (mouse_y >= (cir_y - 35) and mouse_y <= (cir_y + 35)) and not_starting == False and Isitend == False:
                    score += 1
                elif not_starting == False and Isitend == False:
                    if score > 0:
                        score -= 1

                if retry_rect.collidepoint((mouse_x,mouse_y)) and Isitend == True:
                    not_starting = False
                    Isitend = False
                    score = 0
                    start_time = pygame.time.get_ticks()
                elif home_rect.collidepoint((mouse_x,mouse_y)) and Isitend == True:
                    not_starting = True
                    Isitend = False

                cir_x = random.randint(40,width-40)
                cir_y = random.randint(40,length-40)

        if event.type == pygame.QUIT:
            running = False

    # flip() the display to put your work on screen
    pygame.display.flip()

    with open("highscore.txt", "r") as file:
        high_score = int(file.read())
    if high_score < score:
        high_score = score
        with open("highscore.txt", "w") as file:
            file.write(str(high_score))



pygame.quit()
