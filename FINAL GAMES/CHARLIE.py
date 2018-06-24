#/usr/bin/python
"""
A simple game of  whacking simple things with a hammer
"""


#import modules
import os, pygame
import sys
from random import choice


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY80 = (26, 26, 26)
YELLOW = (255, 255, 0)
GRAY = (204, 204, 204)

screen = pygame.display.set_mode((1000, 800))

background_music = "music.wav"
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")
music_folder = os.path.join(game_folder, "music")
background_music = "wind.wav"
hitting_music = "hitsound.wav"
clock = pygame.time.Clock()

def draw_shield_bar(surf, x, y, pct):
    if pct < 0:
        pct = 0
    BAR_LENGTH = 100
    BAR_HEIGHT = 20
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

#define the classes for our game objects
class Player(pygame.sprite.Sprite):
    '''controls the hammer sprite. This class is derived from the Pygame Sprite class'''
    def __init__(self):
        # we MUST call the Sprite init method on ourself
        pygame.sprite.Sprite.__init__(self) 
        #load the image resource
        self.image= pygame.image.load(os.path.join(img_folder, "hamerpin.png")).convert_alpha()
        # get the rectangle describing the loaded image
        self.rect=self.image.get_rect()
        #set the transparency colour to the background of the image
        self.image.set_colorkey(self.image.get_at((0, 0)), pygame.RLEACCEL)
        #copy the base image into a backup for restoring
        self.default=self.image
        self.default_rect=self.rect
        # define a flag sowe can tell what mode the hammer is in
        self.whack = 0
        
        # load a sound effect

    def update(self):
        '''The update method is called before redrawing the sprite each time
        It's our chance to control any time-related behaviour and check status.'''
        #move hammer to current mouse position
        pos = pygame.mouse.get_pos()
        self.rect.center = pos
        #check if we are supposed to be hitting something
        if self.whack:
            #if so, we move the sprite a little, and rotate the image 
            self.rect.move_ip(8, 12)
            self.image = pygame.transform.rotate(self.default, 45)


    def dowhack(self, target):
        "checks to see if hammer has hit a mike"
        if not self.whack:
            self.whack = 1
            hitrect = self.rect.inflate(-50, -50)
            return hitrect.colliderect(target.rect)

    def reset(self):
        '''put the hammer upright again and reset te flag''' 
        self.whack = 0
        self.image=self.default
    



class Mike(pygame.sprite.Sprite):
    """implements a Mike"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image= pygame.image.load(os.path.join(img_folder, "screwpin6.png")).convert_alpha()
        self.rect=self.image.get_rect()
        self.image.set_colorkey(self.image.get_at((0, 0)), pygame.RLEACCEL)
        self.default=self.image
        self.default_rect=self.rect
        # timer of 0 is default and means the Mike is not visible
        self.timer=0
        # if whacked = 0 it means nobody has hit this Mike
        self.whacked=0
        # a list of the possible locations for Mike to pop up at
        self.locations=[(88, 430), (733, 570), (733, 430), (88, 430), (733, 230), (88, 230), (733, 570), (270, 590), (733, 570), (733, 430), (88, 430), (560, 590), (88, 230), (270, 590), (733, 430), (560, 590), (88, 230), (410, 590), (560, 590), (410, 590)]
    def appear(self):
        '''pops out of hole'''
        # set the timer
        #if you change this value, you will also have to alter the update method
        self.timer=80
        #use the Randome.choice() function to select a location from the list
        self.loc=choice(self.locations)

    def update(self):
        '''run housekeeping'''
        #check to see that a Mike should be on te screen
        if self.timer:
            # the Mike exists and is visible
            # decrement counter to count down
            self.timer -= 1
            if self.timer > 60:
                #appearing
                xpos, ypos=self.loc
                height=self.default.get_height()
                #workout what fraction of the image we should draw
                y=(height/20)*(self.timer-60)
                #copy that surface from the backup to the main sprite image
                self.image=self.default.subsurface(0,0,self.default.get_width(),height-y)
                self.rect.left=xpos
                #adjustthe Y position so it pops up
                self.rect.top=ypos+y
            if self.timer == 0:
                #finished - disappear it
                self.rect=self.default_rect
            if self.timer < 12:
                #vanishing
                # like appearing, butin reverse
                xpos, ypos=self.loc
                height=self.default.get_height()
                y=(height/12)*self.timer
                self.image=self.default.subsurface(0,0,self.default.get_width(),y)
                self.rect.left=xpos
                self.rect.top=ypos-y+height 
            if self.whacked:
                #make him suffer
                self.whacked += 1
                #if he is hit, we can use the flag as a counter and spin the sprite through 360 degrees
                if self.whacked >= 10:
                    self.whacked = 0
                    self.image = self.default
                else:
                    self.image =pygame.transform.rotate(self.default, self.whacked*36)
                
                
    def is_hit(self):
        """things todo when object is hit"""
        self.whacked=1
        #make Mike squeal
        
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
                game_intro()
                

def game_over():
    background = pygame.image.load(os.path.join(img_folder, "background3.png")).convert_alpha()
    background_rect = background.get_rect()
    screen.blit(background, background_rect)
    draw_text(screen, "GAME OVER", 60, 500, 300)
    draw_text(screen, "Press any key to start", 30, 500, 400)
    pygame.display.flip()
    wait_for_key()


          
def main():
    """the main game logic"""
#Initialize Everything
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(os.path.join(music_folder, background_music))
    screen = pygame.display.set_mode((1000, 800))
    pygame.display.set_caption('Doomsday')
    pygame.mouse.set_visible(0)
    background = pygame.image.load(os.path.join(img_folder, "background3.png")).convert_alpha()
    BGCOLOR = (0, 0, 0)
    # set up a controlling timer for the game
    clock = pygame.time.Clock()
    pygame.time.set_timer(pygame.USEREVENT + 1 , 1000)
    countdown = 90
    hammer = Player()
    mike=Mike()
    score=0
    #add the sprites to a rendering group
    spritegroup= pygame.sprite.RenderPlain(( mike,  hammer))
    start_ticks=pygame.time.get_ticks()
    running=True
    pygame.mixer.music.play(loops =- 1)


    # control loop
   
    while running:
        #adjust this timer to make the game harder or easier
        clock.tick(80)
        #check what events Pygame has caught
        for event in pygame.event.get():
            if event.type == pygame.QUIT or countdown == 0:
                running=False
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running=False
                    pygame.quit()
                elif event.key == pygame.K_p:
                    pause()
            elif event.type == pygame.USEREVENT + 1:
                countdown -= 1
            elif event.type == pygame.MOUSEBUTTONDOWN:
                #button means the hammer is being used
                    if hammer.dowhack(mike):
                        mike.is_hit()
                        score += 4
                        print(score)
                
            elif event.type is pygame.MOUSEBUTTONUP:
                hammer.reset()
    #does a mike exist? if not, we should have one
        if mike.timer==0:
            mike.appear()
            
        seconds=(pygame.time.get_ticks()-start_ticks)/1000
        if score>=100:
            import Shooter
        if countdown<=0 and score>=100:
            import Shooter
        if countdown<=0 and score<=100:
            game_over()
            wait_for_key()
    

    #refresh the screen by drawing everything again
        #call the update methods of all the sprites in the group
        spritegroup.update()
        #redrawthe background
        screen.blit(background, (0, 0))
        #draw everything
        spritegroup.draw(screen)
        draw_text(screen, "TIMER " + str(countdown), 30, 900, 30)
        draw_shield_bar(screen, 20, 20, score)
        #flip the buffer
        pygame.display.flip()

def show_pause_screen():
    background = pygame.image.load(os.path.join(img_folder, "background3.png")).convert_alpha()
    background_rect = background.get_rect()
    screen.blit(background, background_rect)
    draw_text(screen, "PAUSED", 70, 500, 100)
    draw_text(screen, "Are you afraid to continue?", 40, 500, 250)
    draw_text(screen, "Press C to continue or Q to Quit", 20, 500, 400)

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
            clock.tick(60)

       

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
            if action == main():
                main()
                pygame.quit()
        else:
            pygame.draw.rect(screen, ic,(x,y,w,h))
        
def game_intro():
    pygame.init()
    intro=True
    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type  == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                intro=False
                main()
                pygame.display.flip()
                
        pygame.display.set_caption('Doomsday')
        background = pygame.image.load(os.path.join(img_folder, "backgroundhouse2.png")).convert_alpha()
        

        screen.blit(background, (0, 0))
        mouse = pygame.mouse.get_pos()
        
        draw_text(screen, "PROTECT YOUR HOUSE", 39, 500, 55)
        draw_text(screen, "Hit as many screws as possible", 32, 500, 92)
        draw_text (screen, "Press any key to start", 30, 480, 300)
        draw_text (screen, "Press P to pause", 30, 480, 340)
        
        pygame.display.flip()
        clock.tick(15)
    pygame.quit()
    quit()

    



game_intro()
main()
pygame.quit()
quit()
quit()
