import os, pygame
import sys
from os import path
from random import choice

WIDTH = 1000
HEIGHT = 800
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GRAY80 = (204, 204, 204)
GRAY = (26, 26, 26)


screen = pygame.display.set_mode((1000, 800))
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")

def draw_text(surf, text, size, x, y):
    font_name = pygame.font.match_font('OCR A Extended')
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            if action == quit:
                pygame.quit()
                quit()
        else:
            pygame.draw.rect(screen, ic,(x,y,w,h))

def main():
    # Initialise screen
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((1000, 800))
    pygame.display.set_caption('Credits')

    # Fill background
    background = pygame.image.load(os.path.join(img_folder, "STARS1.jpg")).convert_alpha()
    clock = pygame.time.Clock()
    start_ticks=pygame.time.get_ticks()
    screen.blit(background, (0, 0))
    pygame.display.flip()
    running = True

    while running:

         for event in pygame.event.get():
             if event.type == pygame.QUIT:
                return
                quit()

         screen.blit(background, (0, 0))
         pygame.draw.rect(screen, GRAY,(400,650,190,60))
         draw_text(screen, "Credits", 60, 500, 100)
         draw_text(screen, "Vincent", 30, 500, 250)
         draw_text(screen, "Chevery", 30, 500, 330)
         draw_text(screen, "Charlie", 30, 500, 410)
         draw_text(screen, "Julian", 30, 500, 490)
         draw_text(screen, "Sheriyar", 30, 500, 570)
         draw_text(screen, "Julian", 30, 500, 650)

         mouse = pygame.mouse.get_pos()

         if 400+190 > mouse[0] > 400 and 650+60 > mouse[1] > 650:
            pygame.draw.rect(screen, GRAY80,(400,650,190,60))
         else:
            pygame.draw.rect(screen, GRAY,(400,650,190,60))
                             
         draw_text(screen, "EXIT", 40, 488, 660)
         #screen.blit(arrow, imagerect)
         button("EXIT",400,650,190,60,GRAY,GRAY80,quit)
        
         pygame.display.flip()

if __name__ == '__main__': 
    main()
    pygame.quit()
