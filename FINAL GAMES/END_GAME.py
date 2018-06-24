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

#arrow = pygame.image.load(path.join(img_folder, 'arrow.png')).convert()
#imagerect = arrow.get_rect()

def draw_text(surf, text, size, x, y):
    font_name = pygame.font.match_font('OCR A Extended')
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

def wait_for_key():
    pygame.event.wait()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
                pygame.quit()
                quit()
            if event.type == pygame.KEYUP:
                waiting = False


class PlanetA(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image= pygame.image.load(os.path.join(img_folder, "Planet_A.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 4, 350)

class PlanetZ(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image= pygame.image.load(os.path.join(img_folder, "Planet_Z.png")).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (750, 350)

        
def main():
    # Initialise screen
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((1000, 800))
    pygame.display.set_caption('End game')

    # Fill background
    background = pygame.image.load(os.path.join(img_folder, "STARS2.jpg")).convert_alpha()
    clock = pygame.time.Clock()
    player = PlanetA()
    planet = PlanetZ()
    spritegroup= pygame.sprite.RenderPlain(( player,  planet))
    start_ticks=pygame.time.get_ticks()

    screen.blit(background, (0, 0))
    spritegroup.draw(screen)
    pygame.display.flip()
    running = True
    
    while running:
         for event in pygame.event.get():
             if event.type == pygame.QUIT:
                return
                quit()
             if event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_ESCAPE:
                     running=False
                     pygame.quit()
                 elif event.key == pygame.K_c:
                     import CREDITS
                     CREDITS.main()
                


         
         
         spritegroup.update()
         screen.blit(background, (0, 0))
         spritegroup.draw(screen)
         draw_text(screen, "Congratulations!", 45, 500, 50)
         draw_text(screen, "You made it to your new planet", 30, 500,500)
         draw_text(screen, "Press C to continue", 30, 500, 650)
         pygame.display.flip()

         
    

if __name__ == '__main__': 
    main()
    pygame.quit()











