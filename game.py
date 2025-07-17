import pygame
import random

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

def isTouched(mouse_x, mouse_y, border_x, border_y, width, length):
    if (mouse_x >= border_x and mouse_x <= border_x + width) and (mouse_y >= border_y and mouse_y <= border_y + length):
        return True
    else:
        return False 
    


pygame.init()

width = 800
length = 500

screen = pygame.display.set_mode((width,length))
pygame.display.set_caption("Clicking Game")

background = Background('menu.jpg', [0,0])

running = True
drawings = True
score = 0
cir_x = 0
cir_y = 0
try:
    with open("highscore.txt", "r") as file:
        high_score = int(file.read())
    if high_score < score:
        high_score = score
except:
    with open("highscore.txt", "w") as file:
        file.write(str(score))


while running:

    font = pygame.font.Font('freesansbold.ttf', 18)
    menufont = pygame.font.Font('freesansbold.ttf', 40)




    score_text = font.render('Score: ' + str(score), True, (0, 255, 0), (0,0,255))
    hscore_text = font.render('High Score: ' + str(high_score), True, (0, 255, 0), (0,0,255))

    textRect = score_text.get_rect()
    textRect2 = hscore_text.get_rect()


    textRect.center = (52,20)
    textRect2.center = (80,40)


    mouse_x, mouse_y = pygame.mouse.get_pos()
    screen.fill("black")
    screen.blit(pygame.transform.scale(background.image, (width,length)), background.rect)

    if drawings == True:
        menu_text = menufont.render('START', True, (255,255,255), (0,0,0))
        menuRect = menu_text.get_rect()
        menuRect.center =  (width/2, length/2)
        screen.blit(menu_text, menuRect)

    else:
        screen.blit(score_text, textRect)
        screen.blit(hscore_text,textRect2)
        pygame.draw.circle(screen, (255,0,0), (cir_x,cir_y), 35)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if menuRect.collidepoint((mouse_x,mouse_y)) and drawings == True:
                    drawings = False
                    cir_x = random.randint(40, width-40)
                    cir_y = random.randint(40, length-40)
                elif (mouse_x >= (cir_x - 35) and mouse_x <= (cir_x + 35)) and (mouse_y >= (cir_y - 35) and mouse_y <= (cir_y + 35)):
                    cir_x = random.randint(40,width-40)
                    cir_y = random.randint(40,length-40)
                    score += 1
                else:
                    if score > 0:
                        score -= 1
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
