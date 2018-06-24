

import pygame
import random
import os
from os import path

img_dir = path.join(path.dirname(__file__), 'img')
snd_dir = path.join(path.dirname(__file__), 'snd')

WIDTH = 1000
HEIGHT = 800
FPS = 30

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (216,191,216)
YELLOW = (255,255,0)

pygame.init()

# Voor geluid
pygame.mixer.init()  

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The game")
clock = pygame.time.Clock()

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')
time = 90
pygame.time.set_timer(pygame.USEREVENT + 1 , 1000)


#Load in grapahics
background = pygame.image.load(path.join(img_dir, 'AchtergrondoePl1000800.jpg')).convert()
background_rect = background.get_rect()
backgroundStart = pygame.image.load(path.join(img_dir, 'backgroundStart21000800.jpg')).convert()
backgroundStart_rect = background.get_rect()
backgroundPause = pygame.image.load(path.join(img_dir, 'cockpit1000800.jpg')).convert()
backgroundPause_rect = background.get_rect()
player_img = pygame.image.load(path.join(img_folder, 'PygameFigure.png')).convert()
mob_img = pygame.image.load(path.join(img_folder, 'meteorBrown_med001.png')).convert()


#EXPLOSION ANIMATION
explosion_anim = {}
explosion_anim['lg'] = []
explosion_anim['sm'] = []
for i in range(9):
    filename = 'regularExplosion0{}.png'.format(i)
    img = pygame.image.load(path.join(img_dir, filename)).convert()
    img.set_colorkey(BLACK)
    img_lg = pygame.transform.scale(img, (200, 200))
    explosion_anim['lg'].append(img_lg)
    img_sm = pygame.transform.scale(img, (50, 50))
    explosion_anim['sm'].append(img_sm)

class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image = explosion_anim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosion_anim[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = explosion_anim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, 'PygameFigure.png')).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 60
        self.rect.centerx = (WIDTH / 2)
        self.rect.bottom = HEIGHT - 10
        self.shield = 100

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed() #hier error
        if keystate[pygame.K_LEFT]:
            self.speedx = -7
        if keystate[pygame.K_RIGHT]:
            self.speedx = +7
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

mobs = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()  # om de sprites naast elkaar te laten bestaan in de game
player = Player()
all_sprites.add(player)

def show_go_screen():#Alleen aan het begin en eind van game om weer te beginnen
    screen.blit(backgroundStart, backgroundStart_rect)
    draw_text(screen, "ARMAGEDDON!", 64, WIDTH / 2, HEIGHT / 4)
    draw_text(screen, "Use the left and right arrow keys to evade the meteorites and press P to pause", 16,
              WIDTH / 2, HEIGHT / 2)
    draw_text(screen, "The earth has completely perished, survive 100 seconds to escape!", 20,
              WIDTH / 2, HEIGHT / 1.5)
    draw_text(screen, "Press any key to start", 18, WIDTH / 2, HEIGHT * 3 / 4)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False

def show_end_screen(): #Alleen aan het einde
    screen.blit(backgroundPause, backgroundPause_rect)
    draw_text(screen, "YOU SURVIVED!", 70, WIDTH/2, 200)
    draw_text(screen, "Press any key to continue", 40, WIDTH/2, 400)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                pygame.display.update()
                waiting = False

#def end():
#     paused = True
#     while paused:
#        show_end_screen()
#        for event in pygame.event.get():
#            if event.type == pygame.QUIT:
#                pygame.quit()
#            if event.type == pygame.KEYUP:
#               paused = False
#               quit()
#            
#     pygame.display.update()
#     clock.tick(15)

def show_pause_screen():#Terwijl op pauze
    screen.blit(backgroundPause, backgroundPause_rect)
    draw_text(screen, "PAUSED", 70, WIDTH/2, 100)
    draw_text(screen, "Are you afraid to continue?", 40, WIDTH / 2, 250)
    draw_text(screen, "Press C to continue or Q to Quit", 25, WIDTH/2, 400)


def pause():
     paused = True
     while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_c:
                   paused = False 
               elif event.key == pygame.K_q:
                   import menu
        show_pause_screen()
        pygame.display.update()
        clock.tick(15)

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
                show_go_screen()
                

def game_over():
    background = pygame.image.load(os.path.join(img_folder, "AchtergrondoePl1000800.jpg")).convert_alpha()
    background_rect = background.get_rect()
    screen.blit(background, background_rect)
    draw_text(screen, "GAME OVER", 60, 500, 300)
    draw_text(screen, "Press any key to start", 30, 500, 400)
    pygame.display.flip()
    wait_for_key()
    player.shield = 100
    pygame.display.update()


    
#piece of code to draw any text on the screen
font_name = pygame.font.match_font('OCR A Extended')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, PURPLE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


def newmob():
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)

def draw_shield_bar(surf, x, y, pct):
    if pct < 0:
        pct = 0
    BAR_LENGTH = 100
    BAR_HEIGHT = 10
    fill = (pct/100)* BAR_LENGTH
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    if pct > 70:
        pygame.draw.rect(surf, GREEN, fill_rect)
    elif pct > 40:
        pygame.draw.rect(surf, YELLOW, fill_rect)
    else:
        pygame.draw.rect(surf, RED, fill_rect)
    pygame.draw.rect(surf, WHITE, outline_rect, 2)

    

#class Player(pygame.sprite.Sprite):

    #def __init__(self):
        #pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.image.load(os.path.join(img_folder, 'PygameFigure.png')).convert()
        #self.image.set_colorkey(BLACK)
        #self.rect = self.image.get_rect()
        #self.radius = 60
        #self.rect.centerx = (WIDTH / 2)
        #self.rect.bottom = HEIGHT - 10
        #self.shield = 100

    #def update(self):
      #  self.speedx = 0
       # keystate = pygame.key.get_pressed() #hier error
        #if keystate[pygame.K_LEFT]:
           # self.speedx = -7
        #if keystate[pygame.K_RIGHT]:
          # self.speedx = +7
        #self.rect.x += self.speedx
        #if self.rect.right > WIDTH:
          #  self.rect.right = WIDTH
        #if self.rect.left < 0:
          #  self.rect.left = 0

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_orig = pygame.transform.scale(mob_img, (55,55))
        self.image_orig.set_colorkey(BLACK)
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.radius = 20
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(5, 10)
        self.speedx = random.randrange(-2, 2)
        self.rot = 0
        self.rot_speed = random.randrange(-8, 8)
        self.last_update = pygame.time.get_ticks()

    def rotate (self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.rot = (self.rot + self.rot_speed) % 360
            new_image = pygame.transform.rotate(self.image_orig, self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center

    def update(self):
        self.rotate()
        self.rect.x += self.speedx 
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(6, 12)
            self.speedx = random.randrange(-2, 2)
            
#load all game sounds
explosion_sound = pygame.mixer.Sound(path.join(snd_dir, 'Explosion.wav'))
ship_explosion = pygame.mixer.Sound(path.join(snd_dir, 'shipExplosion1.wav'))
launch_sound = pygame.mixer.Sound(path.join(snd_dir, 'launch.wav'))
pygame.mixer.music.load(path.join(snd_dir, 'soundtrackoe.wav'))



#score

#time = 90
#pygame.time.set_timer(pygame.USEREVENT + 1 , 1000)

#game loop
running = True
start = True #heette start

launch_sound.play()

pygame.mixer.music.play(loops=-1)

while running:

    if start: #heette start
        show_go_screen()
        start = False

        for i in range (12):
            newmob()

    #To pause it for the launch sound to play
    if time <  0:
          show_end_screen()
          import END_GAME
          END_GAME.main()

          

    clock.tick(FPS)          #fps
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            pygame.mixer.quit()

        if event.type == pygame.USEREVENT + 1:
            time -= 1

    #update score (= aantal seconden dat het spel draait
    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running=False
                pygame.quit()
            elif event.key == pygame.K_p:
                pause()

    #if score > 100:
      #  end()
      #  pygame.mixer.quit()

    #score=(int)((pygame.time.get_ticks()-start_ticks)/1000)

    # update
    all_sprites.update()

    # Where the mob hits the player
    hits = pygame.sprite.spritecollide (player, mobs, True, pygame.sprite.collide_circle)
    for hit in  hits:
        explosion_sound.play()
        player.shield -= 20
        expl = Explosion(hit.rect.center, 'sm')
        all_sprites.add(expl)
        newmob()
        if player.shield <= 0:
            expl = Explosion(hit.rect.center, 'lg')
            all_sprites.add(expl)
            ship_explosion.play()
            game_over()
            time = 90
            mobs = pygame.sprite.Group()
            all_sprites = pygame.sprite.Group()  # om de sprites naast elkaar te laten bestaan in de game
            player = Player()
            all_sprites.add(player)
            for i in range(12):
                newmob()
            pygame.display.update()



 #   for hit in hits:
 #       explosion_sound.play()
 #       player.shield -= 20
 #       expl = Explosion(hit.rect.center, 'sm')
 #       all_sprites.add(expl)
 #       newmob()
 #       if player.shield <= 0:
 #           expl = Explosion(hit.rect.center, 'lg')
 #           all_sprites.add(expl)
 #          ship_explosion.play()
 #           game_over()
 #           
 #           show_go_screen()
 #          game_over = False
 #           time = 150
 #          all_sprites = pygame.sprite.Group()
 #           mobs = pygame.sprite.Group()
 #           player = Player()
 #           all_sprites.add(player)
 #           shield = 100
 #           for i in range(12):
 #               m = Mob()
 #               all_sprites.add(m)
 #               mobs.add(m)
        
    #DRAW / RENDER
    screen.fill(BLUE)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    draw_text(screen, "TIME " + str(time), 22, 55, 30)
    draw_shield_bar(screen, 5, 10, player.shield)
    
    pygame.display.flip()

pygame.quit
pygame.mixer.quit()

