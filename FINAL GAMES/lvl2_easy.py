from random import randint
import pygame
from pygame import *
import os

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

BG_MUSIC = "music.ogg"
game_folder = os.path.dirname(__file__)
music_folder = os.path.join(game_folder, "music")
img_folder = os.path.join(game_folder, "img")

#random = ()
#score = 0
loop =  9
time.Clock
##########bliksemmomenten
bliksem1 = randint(10, 30)
bliksem2 = randint (15, 45)
bliksem3 = randint (45, 60)
bliksem4 = randint (45, 100)
bliksem5 = randint(45,100)
bliksem6 = randint(80,150)
bliksem7 = randint(80,150)
bliksem8 = randint(80,150)
bliksem9 = randint(80,150)


countdown = randint(2,5)

wolkrandom = randint(275, 500)

class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)

def simple_camera(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    return Rect(-l+HALF_WIDTH, -t+HALF_HEIGHT, w, h)

def complex_camera(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t, _, _ = -l+HALF_WIDTH, -t+HALF_HEIGHT, w, h

    l = min(0, l)                           # stop scrolling at the left edge
    l = max(-(camera.width-WIN_WIDTH), l)   # stop scrolling at the right edge
    t = max(-(camera.height-WIN_HEIGHT), t) # stop scrolling at the bottom
    t = min(0, t)                           # stop scrolling at the top
    return Rect(l, t, w, h)

class Speler(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
            

def draw_shield_bar(surf, x, y, pct):
    if pct < 0:
        pct = 0
    BAR_LENGTH = 100
    BAR_HEIGHT = 15
    fill = (pct / 100) * BAR_LENGTH
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    if pct > 70:
        pygame.draw.rect(surf, GREEN, fill_rect)
    elif pct > 40:
        pygame.draw.rect(surf, YELLOW, fill_rect)
    else:
        pygame.draw.rect(surf, RED, fill_rect)
    pygame.draw.rect(surf, WHITE, outline_rect, 2)

class Player(Speler):
    def __init__(self, x, y):
        Speler.__init__(self)
        self.xvel = 0
        self.yvel = 0
        self.onGround = False
        self.image = pygame.image.load(os.path.join(img_folder, "img.png")).convert_alpha()
        self.x = x
        self.y = y
        self.rect = Rect(x, y, 37, 37)
        self.Hearts = 100
        PLAYER_HEALTH = self.Hearts
       # draw_player_health(pygame.display.set_mode((DISPLAY)), 10, 10, PLAYER_HEALTH)
        self.time = 150
        self.muntjes = 0



        
    def update(self, up, down, left, right, running, platforms):
        if up:
            # only jump if on the ground
            if self.onGround: self.yvel -= 10
        if down:
            pass
        if running:
            self.xvel = 7
        if left:
            self.xvel = -7 #was -8
        if right:
            self.xvel = 7  #was 8
        if not self.onGround:
            # only accelerate with gravity if in the air
            self.yvel += 0.4
            # max falling speed
            if self.yvel > 100: self.yvel = 100
        if not(left or right):
            self.xvel = 0
        # increment in x direction
        self.rect.left += self.xvel
        # do x-axis collisions
        self.collide(self.xvel, 0, platforms)
        self.collider(self.xvel, 0, platforming)
        self.waterrider(self.xvel, 0, watering)
        # increment in y direction
        self.rect.top += self.yvel
        # assuming we're in the air
        self.onGround = False;
        # do y-axis collisions
        self.collide(0, self.yvel, platforms)
        self.collider(0, self.yvel, platforming)
        self.waterrider(self.yvel, 0, watering)


    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if isinstance(p, ExitBlock) and self.muntjes == 0:
                    import CHARLIE
                if xvel > 0:
                    self.rect.right = p.rect.left
                if xvel < 0:
                    self.rect.left = p.rect.right
                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.yvel = 0
                if yvel < 0:
                    self.rect.top = p.rect.bottom
                    
    def collider(self, xvel, yvel, platforming):
        for i in platforming:
            if pygame.sprite.collide_rect(self, i):
                if xvel > 0:
                    #self.reset = 0
                    #self.reset = self.reset + 10
                    i.kill()
                if xvel < 0:
                    i.kill()
                if yvel > 0:
                    i.kill()
                if yvel < 0:
                    i.kill()


    def waterrider(self, xvel, yvel, watering):
        for z in watering:
            if pygame.sprite.collide_rect(self, z):
                if xvel > 0:
                    player.rect = Rect(0,0, 37, 37)
                    r.rect = Rect (80,0,287,184)
                    self.Hearts = self.Hearts -20
                    seconds = 0
                if xvel < 0:
                    player.rect = Rect(0,0, 37, 37)
                    r.rect = Rect (80,0,287,184)
                    self.Hearts = self.Hearts -20
                    seconds = 0
                if yvel > 0:
                    player.rect = Rect(0,0, 37, 37)
                    r.rect = Rect (80,0,287,184)
                    self.Hearts = self.Hearts -20
                    seconds = 0
                if yvel < 0:
                    player.rect = Rect(0,0, 37, 37)
                    r.rect = Rect (80,0,287,184)
                    self.Hearts = self.Hearts -20
                    seconds = 0


        
class Platform(Speler):
    def __init__(self, x, y):
        Speler.__init__(self)
        self.image = Surface((37, 37))
        self.image.convert()
        self.image.fill(Color(115,46,7))
        self.rect = Rect(x, y, 37, 37)

        

    def update(self):
        pass

class ExitBlock(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y+30)
        self.image = Surface((10, 10))
        self.image.fill(Color("#ac6316"))

        

class Boom(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = Surface((37, 37))
        self.image.convert()
        self.image.fill(Color(115,46,7))
        self.rect = Rect(x, y, 37, 37)

class Storm(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = Surface((287, 184))
        self.image.convert()
        self.image.fill(Color(115,46,7))
        self.rect = Rect(x, y, 287, 184) #37,37

class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = Surface((37, 37))
        self.image.convert_alpha()
        self.image.fill(Color(115,46,7))
        self.rect = Rect(x, y, 37, 37)

      
def new():
    messagebox.showinfo("test","test")

    
GREEN = (0,200,0)
bright_green = (0,255,0)
YELLOW = (255,255,0)
RED = (200,0,0)
bright_red = (255,0,0)
WHITE = (255,255,255)
"""def draw_player_health(surf, x, y, pct):
    if player.Hearts< 0:
        player.Hearts = 0
    BAR_LENGTH = 100
    BAR_HEIGHT = 20
    fill = pct * BAR_LENGTH
    outline_rect = pygame.Rect(x,y,BAR_LENGTH,BAR_HEIGHT)
    fill_rect = pygame.Rect(x,y,fill,BAR_HEIGHT)
    if player.Hearts > 4:
        col = GREEN
    elif player.Hearts > 2:
        col = YELLOW
    else:
        col = RED
    pygame.draw.rect(surf, col, fill_rect)
    pygame.draw.rect(surf, WHITE, outline_rect, 2)"""
    


global cameraX, cameraY
pygame.init()
screen = pygame.display.set_mode(DISPLAY, FLAGS, DEPTH)
pygame.display.set_caption("Use arrows to move!")
timer = pygame.time.Clock()
clock = time.Clock()
FPS = 60
seconds = 0
font_name = font.match_font("OCR A Extended")
font = font.Font(font_name,int(20) )
time.set_timer(USEREVENT +1 , 1000)
hearts = 5
tijd = 200
tijd =- 1

up = down = left = right = running = False
bg = Surface((37,37))
bg.convert()
bg.fill(Color(20,20,20))
entities = pygame.sprite.Group()
player = Player(37, 37)
platforms = []
platforming = []
watering = []
uitroepteken = pygame.image.load(os.path.join(img_folder, "uitroepteken.png")).convert_alpha()
apocalypse = pygame.image.load(os.path.join(img_folder, "apocalypse.jpg")).convert_alpha()


x = y = 0
level = [
    "                                               I                                                                                      ",
    "                           R                 STT                                                                                    ",
    "                                                    I             T        STT    TTT                                               ",
    "                                                I                                         I                                         ",
    "      I                                   TTTTTT  T            T            I           STT                                         ",
    "   TTTT                   I                      T    T           T        TTTT                                                     ",
    "                        STT                                                                                                            ",
    "              T                 T                                       I              TTTT                                         ",
    "   TTT     T                              T                     T                                                                      ",
    "    I        I      I    TTTT                 I      I            T  STT                               I                        I      ",
    "        TI  T  TT     TT           T                   TTT                                 T  T    T    TT        I       T       T    ",
    "         TI   T T   T T   I                                            I                                   T      T             I  ",
    "    I  T  T  T  T  T  T  T          C    TT          I               TTT   C             TTTTT                             T           T ",
    "      T  T  T   T   T                            STT                                         C                                  T    ",
    "              B                            B              T                                            B                           B",
    "T                             I                              T    T            T                                            H       ",
    "    TT                                  T        TTT                                                                                ",
    "                    STT                          T             T           STT         T  T                                        ",
    "      T                    T W W     T           I        T     W       I      T                           T                        ",
    "                                                                                       I  I                                   E   ",
    "GGGGGGGGGGGGGGGGGGGGGGGG  WGGG  W  GGGGGGGGGGGGGGG   TGGGGGGGGG WGWGGGGGGGGGGGGGGGGGG  G  G  GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG",
    "PPPPPPPPPPPPPPPPPPPPPPPPP  PPP  P  PPPPPPPPPPPPPPP  PPPPPPPPPP  P  PPPPPPPPPPPPPPPPPP  P  P  PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",]
# build the level

for row in level:
    for col in row:
        if col == "P":
            p = Platform(x, y)
            p.image = pygame.image.load(os.path.join(img_folder, "Groundbrown6.png")).convert_alpha()
            platforms.append(p)
            entities.add(p)
        if col == "T":
            t = Platform(x, y)
            t.image = pygame.image.load(os.path.join(img_folder, "steen.png")).convert_alpha()
            platforms.append(t)
            entities.add(t)
        if col == "E":
            e = ExitBlock(x, y)
            platforms.append(e)
            entities.add(e)
        if col == "H":
            h = Boom(x, y)
            h.image = pygame.image.load(os.path.join(img_folder, "Huis.png")).convert_alpha()
            platforms.append(h)
            entities.add(h)
        if col == "B":
            b = Boom(x, y)
            b.image = pygame.image.load(os.path.join(img_folder, "booma.png")).convert_alpha()
            entities.add(b)
        if col == "C":
            c = Boom(x, y)
            c.image = pygame.image.load(os.path.join(img_folder, "boomb.png")).convert_alpha()
            entities.add(c)
        if col == "G":
            g = Boom(x, y)
            g.image = pygame.image.load(os.path.join(img_folder, "gras.png")).convert_alpha()
            entities.add(g)
            g.rect = Rect(x,  770, 37, 37)
        if col == "W":
            w = Boom(x, y)
            w.image = pygame.image.load(os.path.join(img_folder, "bliksemwater.png")).convert_alpha()
            watering.append(w)
            entities.add(w)
            w.rect = Rect(x, y, 100, 100)
        if col == "S":
            s = Boom(x, y)
            s.image = pygame.image.load(os.path.join(img_folder, "Schuilplaats.png")).convert_alpha()
            entities.add(s)
        if col == "I":
            i = Coin(x, y)
            i.image = pygame.image.load(os.path.join(img_folder, "munt.png")).convert_alpha()
            platforming.append(i)
            entities.add(i)
        if col == "L":
            l = Boom(x, y)
            l.image = pygame.image.load(os.path.join(img_folder, "hartjes.png")).convert_alpha()   
            entities.add(l)
        if col == "R":
            r = Storm(player.xvel, y)
            klokje = 1
            r.image = pygame.image.load(os.path.join(img_folder, "cloud.png")).convert_alpha()
            entities.add(r)    

            
        
        x += 37
    y += 37
    x = 0

total_level_width  = len(level[0])*37
total_level_height = len(level)*37
camera = Camera(complex_camera, total_level_width, total_level_height)
entities.add(player)
radius = r.rect.right-r.rect.left
black = (0,0,0)

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

def show_pause_screen():
    screen.blit(startpicture, (100,50))
    draw_text(screen, "PAUSED", 70, WIN_WIDTH/2, 100)
    draw_text(screen, "Are u afraid to continue?", 40, WIN_WIDTH/1.9, 250)
    draw_text(screen, "Press C to continue or Q to Quit", 20, WIN_WIDTH/2, 400)

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
            clock.tick(FPS)
            
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
        
#####variables voor the main menu
#msg = 
#x_positie =
#y_positie =
#width_positie =
#height_positie =
#ic =
#ac =

pygame.mixer.music.load(os.path.join(music_folder, BG_MUSIC))


def game():
    global seconds
    global bliksem1
    global bliksem2
    global bliksem3
    global bliksem4
    global bliksem5
    global bliksem6
    global bliksem7
    global bliksem8
    global bliksem9
    global loop
    global up
    global down
    global left
    global right
    global running
    global platforms
    global player
    global r


    while 1:
        timer.tick(60)




        for e in pygame.event.get():
            if e.type == QUIT:
                raise SystemExit("QUIT")
            if player.time == 0 or player.Hearts == 0:
                show_end_screen()
                import lvl2_easy1
                mixer.music.play(loops =- 1)
                lvl2_easy1.show_go_screen()
                lvl2_easy1.game()
            if e.type == KEYDOWN and e.key == K_ESCAPE:
                raise SystemExit ("ESCAPE")
            if e.type == USEREVENT + 1:
                seconds += 1
                player.time -= 1
            if e.type == KEYDOWN and e.key == K_p:
                pause()
            if e.type == KEYDOWN and e.key == K_UP:
                up = True
            if e.type == KEYDOWN and e.key == K_DOWN:
                down = True
            if e.type == KEYDOWN and e.key == K_LEFT:
                left = True
            if e.type == KEYDOWN and e.key == K_RIGHT:
                right = True
            if e.type == KEYDOWN and e.key == K_SPACE:
                running = True

            if e.type == KEYUP and e.key == K_UP:
                up = False
            if e.type == KEYUP and e.key == K_DOWN:
                down = False
            if e.type == KEYUP and e.key == K_RIGHT:
                right = False
            if e.type == KEYUP and e.key == K_LEFT:
                left = False
            
                

        # draw background
        for y in range(37):
            for x in range(37):
                screen.blit(bg, (x * 37, y * 37))
                
        #tijs = 450
        #tijn = 500
        #tijs = tijs + 1
        #tijn = tijn + 1
        #klokje += 1
        #kentucky = True
        #yawn = 80
        #zonder = False

        player.muntjes = (len(entities) - 382)
       # pygame.mixer.music.play(loops =- 1)


        if seconds >= bliksem1 and seconds <= bliksem1 or seconds >= bliksem2 and seconds <= bliksem2 or seconds >= bliksem3 and seconds <= bliksem3 or seconds >= bliksem4 and seconds <= bliksem4 or seconds >= bliksem5 and seconds <= bliksem5 or seconds >= bliksem6 and seconds <= bliksem6 or seconds >= bliksem7 and seconds <= bliksem7 or seconds >= bliksem8 and seconds <= bliksem8 or seconds >= bliksem9 and seconds <= bliksem9 :
            r.image = pygame.image.load(os.path.join(img_folder, "thunder.png")).convert_alpha()
            if player.rect.right >= 746 and player.rect.right <=906 and player.rect.top <= 740 and player.rect.top >= 666:
             #   if r.rect.left -90 < player.rect.right and r.rect.right +90 > player.rect.right:
              #      player.rect = Rect(0,0, 37, 37)
               #     player.hearts = player.hearts -1
               print ("player is safe")
            elif player.rect.right >= 903 and player.rect.right <=1052 and player.rect.top <= 296 and player.rect.top >= 259:
                #if r.rect.left -90 < player.rect.right and r.rect.right +90 > player.rect.right:
                #    player.rect = Rect(0,0, 37, 37)
                 #   player.hearts = player.hearts -1
                 print ("player is safe")
            elif player.rect.right >= 1669 and player.rect.right <=1829 and player.rect.top <= 111 and player.rect.top >= 74:
                       ## if r.rect.left -90 < player.rect.right and r.rect.right +90 > player.rect.right:
                         #   player.rect = Rect(0,0, 37, 37)
                          #  player.hearts = player.hearts -1
                print ("player is safe")
            elif player.rect.right >= 1813 and player.rect.right <=1985 and player.rect.top <= 555 and player.rect.top >= 518:
                           # if r.rect.left -90 < player.rect.right and r.rect.right +90 > player.rect.right:
                            #    player.rect = Rect(0,0, 37, 37)
                             #   player.hearts = player.hearts -1
                print ("player is safe")
            elif player.rect.right >= 2561 and player.rect.right <=2721 and player.rect.top <= 407 and player.rect.top >= 370:
                              #  if r.rect.left -90 < player.rect.right and r.rect.right +90 > player.rect.right:
                               #     player.rect = Rect(0,0, 37, 37)
                                #    player.hearts = player.hearts -1
                print ("player is safe")
            elif player.rect.right >= 2779 and player.rect.right <=2947 and player.rect.top <= 740 and player.rect.top >= 666:
                                 #   if r.rect.left -90 < player.rect.right and r.rect.right +90 > player.rect.right:
                                  #      player.rect = Rect(0,0, 37, 37)
                                   #     player.hearts = player.hearts -1
                print ("player is safe")
            elif player.rect.right >= 2779 and player.rect.right <=2947 and player.rect.top <= 148 and player.rect.top >= 11:
                                    #    if r.rect.left -90 < player.rect.right and r.rect.right +90 > player.rect.right:
                                     #       player.rect = Rect(0,0, 37, 37)
                                      #      player.hearts = player.hearts -1
                print ("player is safe")
            elif player.rect.right >= 3266 and player.rect.right <=3418 and player.rect.top <= 222 and player.rect.top >= 185:
                print ("player is safe")
            elif r.rect.left  < player.rect.left and (r.rect.right ) > player.rect.right:
                    player.rect = Rect(0,0, 37, 37)
                    player.Hearts = player.Hearts -20
                    r.rect = Rect (80,0,287,184)
                    seconds = 0
           # if r.rect.left -90  >= 1052 and r.rect.right + 90 <= 1444:
             #   w.image = pygame.image.load(os.path.join(img_folder, "bliksemwater.png")).convert_alpha()
            #    entities.add(w)
         #   elif r.rect.left -90 >= 2377 and r.rect.right + 90 <= 2593:
          #      w.image = pygame.image.load(os.path.join(img_folder, "bliksemwater.png")).convert_alpha()            
           #     entities.add(w)
        else:
            r.image = pygame.image.load(os.path.join(img_folder, "cloud.png")).convert_alpha()

        if seconds >= bliksem1-2 and seconds <= bliksem1-2 or seconds >= bliksem2-2 and seconds <= bliksem2-2 or seconds >= bliksem3-2 and seconds <= bliksem3-2 or seconds >= bliksem4-2 and seconds <= bliksem4-2 or seconds >= bliksem5-2 and seconds <= bliksem5-2 or seconds >= bliksem6-2 and seconds <= bliksem6-2 or seconds >= bliksem7-2 and seconds <= bliksem7-2 or seconds >= bliksem8-2 and seconds <= bliksem8-2 or seconds >= bliksem9-2 and seconds <= bliksem9-2:
            r.image.blit(uitroepteken, [110,70])

        if seconds >= bliksem1-4 and seconds <= bliksem1-4 or seconds >= bliksem2-4 and seconds <= bliksem2-4 or seconds >= bliksem3-4 and seconds <= bliksem3-4 or seconds >= bliksem4-4 and seconds <= bliksem4-4 or seconds >= bliksem5-4 and seconds <= bliksem5-4 or seconds >= bliksem6-4 and seconds <= bliksem6-4 or seconds >= bliksem7-4 and seconds <= bliksem7-4 or seconds >= bliksem8-4 and seconds <= bliksem8-4 or seconds >= bliksem9-4 and seconds <= bliksem9-4 :
            r.image.blit(uitroepteken, [110,70])

        wolkrandom = randint(275, 450)

        if r.rect.left <= player.rect.left - wolkrandom * 1.4:
            loop = + 9
        #if r.rect.left <= camera.state.left:
        #    loop = + 9
        if r.rect.right > player.rect.right + wolkrandom* 1.4:
            loop =  -7
        
        r.rect.right += loop
       # draw_text(screen, str(score), 18, WIDTH / 2, 10)
        draw_shield_bar(screen, 5, 5, player.Hearts)
            
        #print ("wolk links" + str(r.rect.left))
        #print ("wolk rechts" + str(r.rect.right))
       # print("wolk rechts - links : " + str(r.rect.right - r.rect.left))
       # print ("speler top" + str(player.rect.top))
        
    ## de 1e hideout
        ##speler rechts > 746 and <= 906 
        ##speler top 740
        ##speler top max 666 dus als de top van de speler tussen 666 en 740 zit
    ## de 2e hideout
        ##speler top 296
        ## speler rechts > 903 and <=1052
        ##speler top <=296  >=259 
    ## water part
        ##if > 1052 en <=1444  dan bliksemwater

    ##3e hideout
        ## speler top 111-37 (74) dus >= 74 en <= 111
        ## speler rechts  > 1669 and   <= 1829

    ##4e hideout
        ## rects > 1813 and <= 1985
        ## top <=555 and >= 518

    ##5e hideout
        ##rechts > 2561 and <= 2721
        ##top <= 407 and >= 370

    ##or 2e water
        # > 2377 and <=2593
        
        
    ##6e hideout
        ##rechts > 2779 and < 2947
        ## top <= 740 and >= 666
        
    ##7e hideout
        # rechts> 2779 and < 2947
        # top <= 148 >= 11

    ##8e hideout
        # rects >= 3266 and <=3418
        # top <= 222 and >= 185


        timer_display = font.render("Time: " + str (player.time), 1 ,WHITE)
        amount_muntjes_display = font.render("Coins: " + str(player.muntjes), 1, WHITE)

        screen.blit(amount_muntjes_display, (10, 60))
        screen.blit(timer_display, (10, 35))
        
        
        if player.rect.bottom > WIN_HEIGHT:
            player.rect = Rect(0,0, 37, 37)
            player.Hearts = player.Hearts - 20
            r.rect = Rect (80,0,287,184)
            seconds = 0
        if player.Hearts == 0:
            seconds = 0
            


        #pygame.draw.ellipse (r.image, (255,255,255), [r.rect.left, r.rect.right, radius,radius ])
                
        camera.update(player)
        
        # update player, draw everything else
        player.update(up, down, left, right, running, platforms)
        for e in entities:
            screen.blit(e.image, camera.apply(e))

        pygame.display.update()

