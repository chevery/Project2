from random import randint
import pygame
from pygame import *
import os
import lvl2_easy



WIN_WIDTH = 1000
WIN_HEIGHT = 800
HALF_WIDTH = int(WIN_WIDTH / 2)
HALF_HEIGHT = int(WIN_HEIGHT / 2)

DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
DEPTH = 32
FLAGS = 0
CAMERA_SLACK = 30
white = (255,255,255)
dark = (20,20,20)
FPS = 60
pygame.init()

screen = pygame.display.set_mode(DISPLAY, FLAGS, DEPTH)
clock = pygame.time.Clock()

GREEN = (0,200,0)
bright_green = (0,255,0)
YELLOW = (255,255,0)
RED = (200,0,0)
bright_red = (255,0,0)
WHITE = (255,255,255)
black = (0,0,0)
font_name = font.match_font("OCR A Extended")
font = font.Font(font_name,int(20))



BG_MUSIC = "music.ogg"
game_folder = os.path.dirname(__file__)
music_folder = os.path.join(game_folder, "music")
img_folder = os.path.join(game_folder, "img")
#pygame.mixer.music.load(os.path.join(music_folder, BG_MUSIC))
#pygame.mixer.music.play(loops =- 1)


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(os.path.join(img_folder, "menu_picture.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

Background = Background("menu_picture.png", [100,100])

#def draw_text(surf, text, size, x, y):
 #   font = pygame.font.Font(font_name, size)
  #  text_surface = font.render(text, True, WHITE)
   # text_rect = text_surface.get_rect()
    #text_rect.midtop = (x, y)
    #surf.blit(text_surface, text_rect)

#background = pygame.image.load(os.path.join(img_folder, "apocalypse.jpg")).convert_alpha()
#background_rect = background.get_rect()
#START_IMG = 'apocalypse.jpg'
#start_img = pygame.image.load(os.path.join(img_folder, START_IMG)).convert_alpha()
startbackground = pygame.image.load(os.path.join(img_folder, "menu_picture.png")).convert_alpha()
startbackground_rect = startbackground.get_rect()
startpic = "menu_picture.png"
startpicture = pygame.image.load(os.path.join(img_folder, startpic)).convert_alpha()

def draw_text(surf, text, size, x, y):
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)
    
def wait_for_key():
    pygame.event.wait()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.quit:
                waiting = False
                quit()
            if event.type == pygame.KEYUP:
                waiting = False
                
def show_go_screen():
    screen.fill(dark)
    screen.blit(startpicture, (100,50))
    draw_text(screen, "A thunderstorm is here!", WIN_WIDTH*0.037, WIN_WIDTH*0.5 , 0 )
    draw_text(screen, "Try to hide under a stable hideout and survive it!", WIN_WIDTH*0.020, WIN_WIDTH*0.5, WIN_HEIGHT* 0.0375)
    draw_text(screen, "Instructions:", WIN_WIDTH*0.020, WIN_WIDTH*0.4, WIN_HEIGHT * 0.7625  )
    draw_text(screen, "Collect all the coins before the timer runs out", WIN_WIDTH*0.017, WIN_WIDTH*0.4, WIN_HEIGHT * 0.6875)
    draw_text(screen, "and reach the house", WIN_WIDTH*0.017,
              WIN_WIDTH*0.4, WIN_HEIGHT *  0.725)
    draw_text(screen, "You can move by using your keypad and press p for pause", WIN_WIDTH*0.017, WIN_WIDTH*0.4, WIN_HEIGHT* 0.8 )
    draw_text(screen, "Pay attention to the warning signs", WIN_WIDTH*0.017, WIN_WIDTH*0.4, WIN_HEIGHT * 0.8375 )
    draw_text(screen, "And evade the water", WIN_WIDTH*0.017, WIN_WIDTH*0.4, WIN_HEIGHT * 0.875 )
    draw_text(screen, "Press any key to begin", WIN_WIDTH*0.015, WIN_WIDTH*0.4,WIN_HEIGHT * 0.95 )
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                waiting = False
                pygame.display.update()
                clock.tick(FPS)

def show_end_screen():
    screen.fill(dark)
    screen.blit(startpicture, (100,50))
    draw_text(screen, "GAME OVER", WIN_WIDTH*0.070, WIN_WIDTH / 2, 100)
    draw_text (screen, "Press any key to restart", WIN_WIDTH*0.030, WIN_WIDTH / 2, 300)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False
                pygame.display.update()


"""def show_go_screen():
        game_folder = os.path.dirname(__file__)
        img_folder = os.path.join(game_folder, "img")
        screen.blit(start_img, [0,0])
        draw_text("GAME OVER", title_font, 70, WHITE, WIN_WIDTH / 2,
                       WIN_HEIGHT - 500, align="center")
        draw_text("Press any key to restart", title_font, 30, WHITE,
                       WIN_WIDTH /2, WIN_HEIGHT * 3 / 4, align="center")
        pg.display.flip()
        wait_for_key()"""

def text_objects(text, font):
    textSurface = font.render(text, True, WHITE)
    return textSurface, textSurface.get_rect()
 

def button (msg,x_positie,y_positie,width_positie,height_positie,ic,ac,action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    nummer = 1
    #print(click)
    if x_positie+width_positie > mouse[0] > x_positie and y_positie+height_positie > mouse[1] > y_positie:
        pygame.draw.rect(screen, ac,(x_positie,y_positie,width_positie,height_positie))

        if click[0] == 1 and action != None:
            #new()
            lvl2_easy.player.Hearts = 100
            mixer.music.play(loops =- 1)
            nummer =+ 1
            action()
            

    else:
        pygame.draw.rect(screen, ic,(x_positie,y_positie,width_positie,height_positie))

    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x_positie+(width_positie/2)), (y_positie+(height_positie/2)) )
    screen.blit(textSurf, textRect)
    
def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(dark)
        screen.blit(Background.image, Background.rect)
        TextSurf, TextRect = text_objects("A thunderstorm is here!" , font)
        TextSur, TextRect = text_objects("Try to hide and survive it!", font)
        TextSu, TextRect = text_objects("Instructions:", font)
        Textg, TextRect = text_objects("Collect all the coins before the timer runs out", font)
        Texth, TextRect = text_objects("and reach the house", font)
        TextS, TextRect = text_objects("You can move by using your keypad and p for pause", font)
        Textsurn, TextRect = text_objects("Pay attention to the warning signs", font)         
        Textw, TextRect = text_objects("And evade the water", font)
        #pygame.mixer.music.play(loops =- 1)



        screen.blit(TextSurf, (WIN_WIDTH*0.3, 0))
        screen.blit(TextSur, (WIN_WIDTH*0.3, WIN_HEIGHT* 0.0375))
        screen.blit(Textg, (WIN_WIDTH*0.05, WIN_HEIGHT * 0.725))
        screen.blit(Texth, (WIN_WIDTH*0.05, WIN_HEIGHT * 0.7625))
        screen.blit(TextSu, (WIN_WIDTH*0.05, WIN_HEIGHT * 0.6875))
        screen.blit(TextS, (WIN_WIDTH*0.05, WIN_HEIGHT* 0.8))
        screen.blit(Textsurn, (WIN_WIDTH*0.05, WIN_HEIGHT * 0.8375))
        screen.blit(Textw, (WIN_WIDTH*0.05, WIN_HEIGHT * 0.875))

        show_go_screen()
        mixer.music.play(loops =- 1)
        lvl2_easy.game()

        
        #wait_for_key(lvl2_easy.game)

        #wait_for_key()

        #mouse = pygame.mouse.get_pos()
        #button ("Play",WIN_WIDTH*0.4,WIN_HEIGHT * 0.875,WIN_WIDTH*0.2,WIN_HEIGHT * 0.0625,GREEN,bright_green,lvl2_easy.game)






        #story
        #
        
        pygame.display.update()

game_intro()

