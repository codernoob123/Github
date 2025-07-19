import pygame
import random
import time

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

size = (70,70)

class Animation(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y):
        super().__init__()
        self.sprite = []
        self.animating = False
        self.sprite.append(pygame.transform.scale(pygame.image.load('1.5.png'),size))
        self.sprite.append(pygame.transform.scale(pygame.image.load('2.5.png'),size))
        self.sprite.append(pygame.transform.scale(pygame.image.load('3.5.png'),size))
        self.sprite.append(pygame.transform.scale(pygame.image.load('4.5.png'),size))
        self.sprite.append(pygame.transform.scale(pygame.image.load('5.5.png'),size))
        self.sprite.append(pygame.transform.scale(pygame.image.load('6.5.png'),size))
        self.sprite.append(pygame.transform.scale(pygame.image.load('7.5.png'),size))
        self.sprite.append(pygame.transform.scale(pygame.image.load('8.5.png'),size))

        self.currentsprite = 0
        self.image = self.sprite[self.currentsprite]

        self.rect = self.image.get_rect()
        self.rect.center = [pos_x,pos_y]

    def animate(self):
        self.animating = True

    def update(self):
        if self.animating == True:
            self.currentsprite += 0.15
            if self.currentsprite > int(len(self.sprite)):
                self.currentsprite = 0
                self.animating = False

            self.image = self.sprite[int(self.currentsprite)]

    def Isanimating(self):
        if self.animating == True:
            return True
        else:
            return False


pygame.init()

width = 800
length = 500

GREEN = (76, 235, 52)
BLACK = (0,0,0)
WHITE = (255,255,255)

screen = pygame.display.set_mode((width,length))
pygame.display.set_caption("Clicking Game")

background = Background('menu.jpg', [0,0])
background2 = Background('menu2.jpg', [0,0])
checkbox = pygame.transform.scale(pygame.image.load('checkbox.png'),(50,50))
checkbox_tick = pygame.transform.scale(pygame.image.load('checkbox_tick.png'),(50,50))
checkbox2 = pygame.transform.scale(pygame.image.load('checkbox.png'),(50,50))
checkbox_tick2 = pygame.transform.scale(pygame.image.load('checkbox_tick.png'),(50,50))
back_arrow = pygame.transform.scale(pygame.image.load('arrow.png'), (50,50))

musical = pygame.mixer.music.load('mus.mp3')
pop = pygame.mixer.Sound('pop.mp3')
error = pygame.mixer.Sound('error.mp3')
pygame.mixer.music.set_volume(0.2)
pygame.mixer.Sound.set_volume(pop, 0.1)
pygame.mixer.Sound.set_volume(error, 0.2)
pygame.mixer.music.play(-1)

running = True
not_starting = True
music_playing = True
Isitend = False
Optioning = False
Istick = False
effectsound = True
Istick2 = False

score = 0
cir_x = 0
cir_y = 0
start_time = 0
second = 0
count = 0
where_are_you = 2
game_time = 20
countball = 0

try:
    with open("highscore.txt", "r") as file:
        high_score = int(file.read())
    if high_score < score:
        high_score = score
except:
    with open("highscore.txt", "w") as file:
        file.write(str(score))
        high_score = score

font = pygame.font.Font('freesansbold.ttf', 20)
menufont = pygame.font.Font('freesansbold.ttf', 40)
namefont = pygame.font.Font('freesansbold.ttf', 60)
endfont = pygame.font.Font('freesansbold.ttf', 50)
endfont_2 = pygame.font.Font('freesansbold.ttf',30)

checkbox_rect = checkbox.get_rect()
checkbox_tick_rect = checkbox.get_rect()
checkbox_rect2 = checkbox2.get_rect()
checkbox_tick_rect2 = checkbox2.get_rect()
back_arrow_rect = back_arrow.get_rect()

checkbox_rect.center = (450,115)
checkbox_tick_rect.center = (450,115)
checkbox_rect2.center = (450,187)
checkbox_tick_rect2.center = (450,187)
back_arrow_rect.topleft = (10,10)

name_text = namefont.render('Clicking Game', True, WHITE, BLACK)
name_rect = name_text.get_rect()
name_rect.center = (410,120)

option_text = menufont.render('Options', True, WHITE, BLACK)
option_rect = option_text.get_rect()
option_rect.center = (400, 300)

option_text2 = menufont.render('Options', True, BLACK, WHITE)
option_rect2 = option_text2.get_rect()
option_rect2.center = (400, 300)

gameover_text = endfont.render('GAME OVER', True, WHITE, BLACK)
gameover_rect = gameover_text.get_rect()
gameover_rect.center = (400,150)

start_text = menufont.render('START', True, WHITE, BLACK)
startRect = start_text.get_rect()
startRect.center =  (width/2, 230)

start_text2 = menufont.render('START', True, BLACK, WHITE)
startRect2 = start_text2.get_rect()
startRect2.center =  (width/2, 230)

retry_text = menufont.render("Retry", True, WHITE, BLACK)
retry_rect = retry_text.get_rect()
retry_rect.center = (width/2, length/2 + 70)

retry_text2 = menufont.render("Retry", True, BLACK, WHITE)
retry_rect2 = retry_text2.get_rect()
retry_rect2.center = (width/2, length/2 + 70)

home_text = menufont.render("Back To Home", True, WHITE, BLACK)
home_rect = home_text.get_rect()
home_rect.center = (width/2, length/2 + 120)

home_text2 = menufont.render("Back To Home", True, BLACK, WHITE)
home_rect2 = home_text2.get_rect()
home_rect2.center = (width/2, length/2 + 120)

music_text = menufont.render('Music: ', True, WHITE, BLACK)
music_rect = music_text.get_rect()
music_rect.topleft = (150,100)

effect_text = menufont.render('Effect sound: ', True, WHITE, BLACK)
effect_rect = effect_text.get_rect()
effect_rect.topleft = (150, 170)

playtime_text = menufont.render('Choose Your Play Time', True, WHITE, BLACK)
playtime_rect = playtime_text.get_rect()
playtime_rect.center = (400, 280)

ingame_text = font.render('5 secs', True, WHITE, BLACK)
ingame_rect = ingame_text.get_rect()
ingame_rect.topleft = (110, 325)

ingame_text2 = font.render('20 secs', True, WHITE, BLACK)
ingame_rect2 = ingame_text2.get_rect()
ingame_rect2.topleft = (274, 325)

ingame_text3 = font.render('60 secs', True, WHITE, BLACK)
ingame_rect3 = ingame_text2.get_rect()
ingame_rect3.topleft = (444, 325)

ingame_text4 = font.render('90 secs', True, WHITE, BLACK)
ingame_rect4 = ingame_text2.get_rect()
ingame_rect4.topleft = (614, 325)

while running:

    mouse_x, mouse_y = pygame.mouse.get_pos()
    if countball == 0:
        ball_sprites = pygame.sprite.Group()
        ball = Animation(cir_x,cir_y)
        ball_sprites.add(ball)
    else:
        if ball.Isanimating() == True:
            pass
        else:
            ball_sprites = pygame.sprite.Group()
            ball = Animation(cir_x,cir_y)
            ball_sprites.add(ball)

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

    score_end_text = endfont_2.render("Score: " + str(score), True, WHITE, BLACK)
    score_end_rect = score_end_text.get_rect()
    score_end_rect.center = (width/2, length/2 - 40)

    hscore_end_text = endfont_2.render("High Score: " + str(high_score), True, WHITE, BLACK)
    hscore_end_rect = hscore_end_text.get_rect()
    hscore_end_rect.center = (width/2, length/2)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if startRect.collidepoint((mouse_x,mouse_y)) and not_starting == True:
                    not_starting = False
                    start_time = pygame.time.get_ticks()
                    score = 0

                elif (mouse_x >= (cir_x - 35) and mouse_x <= (cir_x + 35)) and (mouse_y >= (cir_y - 35) and mouse_y <= (cir_y + 35)) and not_starting == False and Isitend == False:
                    score += 1
                    countball += 1
                    ball.animate()
                    if effectsound == True:
                        pop.play()
                elif not_starting == False and Isitend == False:
                    if score > 0:
                        score -= 1
                    if effectsound == True:
                        error.play()

                if option_rect.collidepoint((mouse_x,mouse_y)) and not_starting == True and Isitend == False:
                    Optioning = True
                elif back_arrow_rect.collidepoint((mouse_x, mouse_y)) and Optioning == True:
                    Optioning = False

                if checkbox_rect.collidepoint((mouse_x,mouse_y)) and Istick == False and Optioning == True:
                    Istick = True
                elif checkbox_tick_rect.collidepoint((mouse_x,mouse_y)) and Istick == True and Optioning == True:
                    Istick = False

                if checkbox_rect2.collidepoint((mouse_x,mouse_y)) and Istick2 == False and Optioning == True:
                    Istick2 = True
                elif checkbox_tick_rect2.collidepoint((mouse_x,mouse_y)) and Istick2 == True and Optioning == True:
                    Istick2 = False

                if (mouse_x >= 100 and mouse_x <= 180) and (mouse_y >= 350 and mouse_y <= 430) and Optioning == True:
                    where_are_you = 1
                elif (mouse_x >= 270 and mouse_x <= 350) and (mouse_y >= 350 and mouse_y <= 430) and Optioning == True:
                    where_are_you = 2
                elif (mouse_x >= 440 and mouse_x <= 520) and (mouse_y >= 350 and mouse_y <= 430) and Optioning == True:
                    where_are_you = 3
                elif (mouse_x >= 610 and mouse_x <= 690) and (mouse_y >= 350 and mouse_y <= 430) and Optioning == True:
                    where_are_you = 4

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

    if Optioning == True:
        screen.fill("white")
        screen.blit(pygame.transform.scale(background.image, (width,length)), background.rect)
        screen.blit(music_text,music_rect)
        screen.blit(back_arrow, back_arrow_rect)
        screen.blit(effect_text,effect_rect)
        screen.blit(playtime_text,playtime_rect)
        if where_are_you == 1:
            pygame.draw.rect(screen, GREEN, (100,350,80,80))
            pygame.draw.rect(screen, WHITE, (270,350,80,80))
            pygame.draw.rect(screen, WHITE, (440,350,80,80))
            pygame.draw.rect(screen, WHITE, (610,350,80,80))
        elif where_are_you == 2:
            pygame.draw.rect(screen, WHITE, (100,350,80,80))
            pygame.draw.rect(screen, GREEN, (270,350,80,80))
            pygame.draw.rect(screen, WHITE, (440,350,80,80))
            pygame.draw.rect(screen, WHITE, (610,350,80,80))
        elif where_are_you == 3:
            pygame.draw.rect(screen,WHITE, (100,350,80,80))
            pygame.draw.rect(screen, WHITE, (270,350,80,80))
            pygame.draw.rect(screen, GREEN, (440,350,80,80))
            pygame.draw.rect(screen, WHITE, (610,350,80,80))
        else:
            pygame.draw.rect(screen, WHITE, (100,350,80,80))
            pygame.draw.rect(screen, WHITE, (270,350,80,80))
            pygame.draw.rect(screen, WHITE, (440,350,80,80))
            pygame.draw.rect(screen, GREEN, (610,350,80,80))
        screen.blit(ingame_text,ingame_rect)
        screen.blit(ingame_text2,ingame_rect2)
        screen.blit(ingame_text3,ingame_rect3)
        screen.blit(ingame_text4,ingame_rect4)
        if Istick == False:
            screen.blit(checkbox,checkbox_rect)
            music_playing = True
        else:
            screen.blit(checkbox_tick,checkbox_tick_rect)
            music_playing = False

        if Istick2 == False:
            screen.blit(checkbox2,checkbox_rect2)
            effectsound = True
        else:
            screen.blit(checkbox_tick2,checkbox_tick_rect2)
            effectsound = False


    if not_starting == True and Isitend == False and Optioning == False:
        screen.fill("white")
        screen.blit(pygame.transform.scale(background.image, (width,length)), background.rect)
        screen.blit(name_text,name_rect)
        screen.blit(option_text,option_rect)
        if startRect.collidepoint((mouse_x,mouse_y)):
            screen.blit(start_text2, startRect2)
        else:
            screen.blit(start_text, startRect)

        if option_rect.collidepoint((mouse_x,mouse_y)):
            screen.blit(option_text2,option_rect2)
        else:
            screen.blit(option_text,option_rect)

    elif not_starting == False and Isitend == False and Optioning == False:
        screen.fill("white")
        screen.blit(pygame.transform.scale(background2.image, (width,length)), background2.rect)
        screen.blit(score_text, textRect)
        screen.blit(hscore_text,textRect2)
        screen.blit(time_text, timeRect)
        ball_sprites.draw(screen)
        ball_sprites.update()
        if second > game_time:
            Isitend = True

    else:
        if Optioning == False:
            screen.fill("white")
            screen.blit(pygame.transform.scale(background.image, (width,length)), background.rect)
            screen.blit(gameover_text,gameover_rect)
            screen.blit(hscore_end_text,hscore_end_rect)
            screen.blit(score_end_text,score_end_rect)
            if retry_rect.collidepoint((mouse_x,mouse_y)):
                screen.blit(retry_text2,retry_rect2)
            else:
                screen.blit(retry_text, retry_rect)

            if home_rect.collidepoint((mouse_x,mouse_y)):
                screen.blit(home_text2,home_rect2)
            else:
                screen.blit(home_text, home_rect)
    # flip() the display to put your work on screen
    pygame.display.flip()

    with open("highscore.txt", "r") as file:
        high_score = int(file.read())
    if high_score < score:
        high_score = score
        with open("highscore.txt", "w") as file:
            file.write(str(high_score))

    if music_playing == True:
        if count == 1:
            musical = pygame.mixer.music.load('mus.mp3')
            pygame.mixer.music.play(-1)
            count = 0
        else:
            pass
    elif music_playing == False:
        pygame.mixer.music.stop()
        count = 1

    if where_are_you == 1:
        game_time = 5
    elif where_are_you == 3:
        game_time = 60
    elif where_are_you == 4:
        game_time = 90
    else:
        game_time = 20

pygame.quit()
