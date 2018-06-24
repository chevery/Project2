#import pygame
import pygame
from pygame.locals import *

#RANDOM
import random
from random import randint

        


#initialize game engine
pygame.init()

window_width= 1000
window_height= 800
animation_increment=10
clock_tick_rate=20

#Open a window
size = (window_width, window_height)
screen = pygame.display.set_mode(size)

#Set title to the window
pygame.display.set_caption("Lightning World")


#######

######
#class Player(pygame.sprite.Sprite):
    #def __init__(self):
        #super(Player, self).__init__()
       # self.surf = pygame.Surface((75, 25))
      #  self.surf.fill((255,255,255))
     #   self.rect = self.surf.get_rect()

    #def update(self, pressed_keys):
        #if pressed_keys[K_UP]:
         #   self.rect.move_ip(0, -5)
        #if pressed_keys[K_DOWN]:
        #    self.rect.move_ip(0, 5)
        #if pressed_keys[K_LEFT]:
         #   self.rect.move_ip(-5, 0)
        #if pressed_keys[K_RIGHT]:
         #   self.rect.move_ip(5, 0)
            
#######
#Initialize values for color (RGB format)
WHITE=(255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
BLACK=(0,0,0)
BROWN=(165,42,42)
Groundbrown=(115,46,7)
Dark_Blue = (17,30,108)
Gainsboro = (220,220,220)
grey = (128,128,128)
waterkleur = (64,164,223)


###################
#randomgetallen
randomboom1 = (randint(1, window_width/10*2))
randomboom2 = (randint(window_width/10*3, window_width/10*5.5))
randomschuilplaats1 = (randint(1, window_width/10*2.5))
randomschuilplaats2 = (randint(randomschuilplaats1 + 100, window_width/10*5))
randomobstakel = (randint(randomschuilplaats1 + 90, randomschuilplaats2 - 10))
randomwaterlijn = (randint(0,window_width/10*2))
randomwaterlijn2 = (randint(window_width/10*3, window_width/10*5.5))
randomwaterlijn3 = (randint(0,window_width/10*5.5))
######################
#Variables voor de vormen

    #De grond vanaf links
grond1X = 0
grond1Y = window_height/8*7.5
grond1width = window_width/10*6
grond1height = window_height/8*0.5

    #De andere gedeelte van de grond
grond2X = window_width/10*7
grond2Y = window_height/8*7.5
grond2width = window_width/10*3
grond2height = window_height/8*0.5



##################
    #boom1 - onderkant
boom1X = randomboom1
boom1Y = window_height/8*5.9
boom1width = window_width/10*0.3
boom1height = window_height*0.2
    #boom1 - 1e driehoek
boomdriehoek1links = boom1X - boom1width* 1 , boom1Y
boomdriehoek1up = boom1X + boom1width * 0.5 , boom1Y - boom1height
boomdriehoek1rechts = boom1X + boom1width*2, boom1Y
    #boom1 2e driehoek
boomdriehoek2links = boom1X - boom1width* 1 , boom1Y *0.9
boomdriehoek2up = boom1X + boom1width * 0.5 , boom1Y  - boom1height *1.1
boomdriehoek2rechts =  boom1X + boom1width*2 ,boom1Y * 0.9

    #boom2 - onderkant
boom2X = randomboom2
boom2Y = window_height/8*5.9
boom2width = window_width/10*0.3
boom2height = window_height*0.2
    #boom1 - 1e driehoek
boom2driehoek1links = boom2X - boom2width* 1 , boom2Y
boom2driehoek1up = boom2X + boom2width * 0.5 , boom2Y - boom2height
boom2driehoek1rechts = boom2X + boom2width*2, boom2Y
    #boom1 2e driehoek
boom2driehoek2links = boom2X - boom2width* 1 , boom2Y *0.9
boom2driehoek2up = boom2X + boom2width * 0.5 , boom2Y  - boom2height *1.1
boom2driehoek2rechts =  boom2X + boom2width*2 ,boom2Y * 0.9



#################
    #Huis - begane grond (end game)
HuisX = window_width/10*8.3
HuisY = window_height/8*6.3
huiswidth = window_width/10*1.5
huisheight = window_height/8*1.2

    #Huis - dak
huisdaklinks = HuisX - huiswidth*0.18 , HuisY
huisdakup = HuisX + huiswidth * 0.48, HuisY - huisheight
huisdakrechts = HuisX + huiswidth *1.18, HuisY

    #Huis - raam1
huisraam1X = HuisX * 1.02
huisraam1Y = HuisY * 1.02
huisraam1width = huiswidth/ 10 * 2
huisraam1height = huisraam1width

    #Huis - raam2
huisraam2X = HuisX * 1.02
huisraam2Y = HuisY * 1.1
huisraam2width = huiswidth/ 10 * 2
huisraam2height = huisraam1width

    #Huis - raam3
huisraam3X = HuisX * 1.12
huisraam3Y = HuisY * 1.02
huisraam3width = huiswidth/ 10 * 2
huisraam3height = huisraam1width

    #Huis -raam4
huisraam4X = HuisX * 1.12
huisraam4Y = HuisY * 1.1
huisraam4width = huiswidth/ 10 * 2
huisraam4height = huisraam1width

    #Huis - deur
huisdeurX = huisraam1X * 1.05
huisdeurY = HuisY * 1.1
huisdeurwidth = huisraam4width
huisdeurheight = huisheight*0.48

    #Huis - deurknop
huisdeurknopX = int(huisdeurX *1.01 )
huisdeurknopY = int(huisdeurY* 1.05)
huisdeurknopradius = int(4)
huisdeurknopwidth = int(3)

################# 
    #schuilplaats1 - linkerkant
schuilplaatsXL = randomschuilplaats1
schuilplaatsYL = window_height/8*6.8
schuilplaatswidthL = window_width/10*0.2
schuilplaatsheightL = window_height*0.088

    #schuilplaats1 - rechterkant
schuilplaatsXR = schuilplaatsXL+80
schuilplaatsYR = window_height/8*6.8
schuilplaatswidthR= window_width/10*0.2
schuilplaatsheightR = window_height*0.088

    #schuilplaats1 - bovenkant
schuilplaatsXU = schuilplaatsXL
schuilplaatsYU = schuilplaatsYL - schuilplaatswidthL
schuilplaatswidthU = schuilplaatsheightL * 1.43
schuilplaatsheightU = schuilplaatswidthL


    #schuilplaats2
schuilplaats2XL = randomschuilplaats2
schuilplaats2YL = window_height/8*6.8
schuilplaats2widthL = window_width/10*0.2
schuilplaats2heightL = window_height*0.088

    #schuilplaats1 - rechterkant
schuilplaats2XR = schuilplaats2XL+80
schuilplaats2YR = window_height/8*6.8
schuilplaats2widthR= window_width/10*0.2
schuilplaats2heightR = window_height*0.088

    #schuilplaats1 - bovenkant
schuilplaats2XU = schuilplaats2XL
schuilplaats2YU = schuilplaats2YL - schuilplaats2widthL
schuilplaats2widthU = schuilplaats2heightL * 1.43
schuilplaats2heightU = schuilplaats2widthL



############
    #obstakel - over heen springen
obstakelX = randomobstakel
obstakelY = schuilplaatsYL * 1.05
obstakelwidth = schuilplaatswidthL
obstakelheight = schuilplaatsYL *0.054

###############

    #wolk1 helemaal onder

wolkonderX = 100
wolkonderY = window_height/8*2*1.1
wolkonderwidth = window_width / 10 * 2
wolkonderheight = window_height / 80

    #wolk2 helemaal links
wolkcirkel1X = wolkonderX*8/9
wolkcirkel1Y = int(window_height / 8*2*0.9)
wolkcirkel1radius = int(window_width/ 20 )
wolkcirkel1width = wolkcirkel1radius

    #wolk2 
wolkcirkel2X = wolkcirkel1X *1.2
wolkcirkel2Y = int(wolkcirkel1Y *0.93)
wolkcirkel2radius = int(window_width/ 20 )
wolkcirkel2width = wolkcirkel2radius

    #wolk3 
wolkcirkel3X = wolkcirkel2X *1.2
wolkcirkel3Y = int(wolkcirkel2Y*0.93)
wolkcirkel3radius = int(window_width/20)
wolkcirkel3width = wolkcirkel3radius


    #wolk4 links beneden
wolkcirkel4X = wolkcirkel3X *1.2
wolkcirkel4Y = int(wolkcirkel3Y)
wolkcirkel4radius = int(window_width/15)
wolkcirkel4width = wolkcirkel4radius

    #wolk5 midden links beneden
wolkcirkel5X = wolkcirkel3X
wolkcirkel5Y = int(wolkcirkel1Y)
wolkcirkel5radius = int(window_width/20)
wolkcirkel5width = wolkcirkel5radius

    #wolk6 midden beneden
wolkcirkel6X = wolkcirkel4X *1.2
wolkcirkel6Y = int(wolkcirkel1Y)
wolkcirkel6radius = int(window_width/20)
wolkcirkel6width = wolkcirkel6radius


    #wolk7 
wolkcirkel7X = wolkcirkel6X
wolkcirkel7Y = int(wolkcirkel3Y)
wolkcirkel7radius = int(window_width/20)
wolkcirkel7width = wolkcirkel7radius

    #wolk8 
wolkcirkel8X = wolkcirkel6X
wolkcirkel8Y = int(wolkcirkel2Y)
wolkcirkel8radius = int(window_width/20)
wolkcirkel8width = wolkcirkel8radius

    #wolk9 midden links beneden
wolkcirkel9X = wolkcirkel4X
wolkcirkel9Y = int(wolkcirkel6Y)
wolkcirkel9radius = int(window_width/20)
wolkcirkel9width = wolkcirkel9radius

wolkcirkel10X = wolkcirkel4X
wolkcirkel10Y = int(wolkcirkel3Y*0.93)
wolkcirkel10radius = int(window_width/20)
wolkcirkel10width = wolkcirkel10radius

#############
    #plasje water
waterlijnX = randomwaterlijn
waterlijnY = window_height/8*7.501
waterlijnwidth = window_width/10*0.15
waterlijnheight = window_height/8*0.5

    #plasje water2
waterlijn2X = randomwaterlijn2
waterlijn2Y = window_height/8*7.501
waterlijn2width = window_width/10*0.15
waterlijn2height = window_height/8*0.5

    #plasje water3
waterlijn3X = randomwaterlijn3
waterlijn3Y = window_height/8*7.501
waterlijn3width = window_width/10*0.15
waterlijn3height = window_height/8*0.5

############
normale_wolk = pygame.image.load("cloud.png")
stormwolk = pygame.image.load("thunder.png")
x = (window_width/10)
y = (window_height/8)





##############

clock = pygame.time.Clock()
screen.fill(Dark_Blue)
#player = Player()"""
running = True

def draw_tree():
    pygame.draw.rect(screen, BROWN, [boom1X, boom1Y, boom1width, boom1height])
    pygame.draw.rect(screen, BLACK, [boom1X, boom1Y, boom1width, boom1height],2)
    pygame.draw.polygon(screen, GREEN, [boomdriehoek1links, boomdriehoek1up, boomdriehoek1rechts])
    pygame.draw.polygon(screen, BLACK, [boomdriehoek1links, boomdriehoek1up, boomdriehoek1rechts],2)
    pygame.draw.polygon(screen, GREEN, [boomdriehoek2links, boomdriehoek2up, boomdriehoek2rechts])
    pygame.draw.polygon(screen, BLACK, [boomdriehoek2links, boomdriehoek2up, boomdriehoek2rechts],2)
    pygame.draw.rect(screen, BROWN, [boom2X, boom2Y, boom2width, boom2height])
    pygame.draw.rect(screen, BLACK, [boom2X, boom2Y, boom2width, boom2height],2)
    pygame.draw.polygon(screen, GREEN, [boom2driehoek1links, boom2driehoek1up, boom2driehoek1rechts])
    pygame.draw.polygon(screen, BLACK, [boom2driehoek1links, boom2driehoek1up, boom2driehoek1rechts],2)
    pygame.draw.polygon(screen, GREEN, [boom2driehoek2links, boom2driehoek2up, boom2driehoek2rechts])
    pygame.draw.polygon(screen, BLACK, [boom2driehoek2links, boom2driehoek2up, boom2driehoek2rechts],2)
    
def draw_ground():
    pygame.draw.rect(screen, Groundbrown, [grond1X, grond1Y, grond1width , grond1height ])
    pygame.draw.rect(screen, Groundbrown, [grond2X, grond2Y ,grond2width , grond2height ])
    pygame.draw.rect(screen, BLACK, [grond1X, grond1Y, grond1width , grond1height ],2)
    pygame.draw.rect(screen, BLACK, [grond2X, grond2Y ,grond2width , grond2height ],2)

def draw_hideout():
    pygame.draw.rect(screen, Gainsboro, [schuilplaatsXL, schuilplaatsYL, schuilplaatswidthL, schuilplaatsheightL])
    pygame.draw.rect(screen, Gainsboro, [schuilplaatsXR, schuilplaatsYR, schuilplaatswidthR, schuilplaatsheightR])
    pygame.draw.rect(screen, BLACK, [schuilplaatsXL, schuilplaatsYL, schuilplaatswidthL, schuilplaatsheightL],2)
    pygame.draw.rect(screen, BLACK, [schuilplaatsXR, schuilplaatsYR, schuilplaatswidthR, schuilplaatsheightR],2)
    pygame.draw.rect(screen, Gainsboro, [schuilplaatsXU, schuilplaatsYU, schuilplaatswidthU, schuilplaatsheightU])
    pygame.draw.rect(screen, BLACK, [schuilplaatsXU, schuilplaatsYU, schuilplaatswidthU, schuilplaatsheightU],2)
    pygame.draw.rect(screen, Gainsboro, [schuilplaats2XL, schuilplaats2YL, schuilplaats2widthL, schuilplaats2heightL])
    pygame.draw.rect(screen, Gainsboro, [schuilplaats2XR, schuilplaats2YR, schuilplaats2widthR, schuilplaats2heightR])
    pygame.draw.rect(screen, Gainsboro, [schuilplaats2XU, schuilplaats2YU, schuilplaats2widthU, schuilplaats2heightU])
    pygame.draw.rect(screen, BLACK, [schuilplaats2XU, schuilplaats2YU, schuilplaats2widthU, schuilplaats2heightU],2)
    pygame.draw.rect(screen, BLACK, [schuilplaats2XL, schuilplaats2YL, schuilplaats2widthL, schuilplaats2heightL],2)
    pygame.draw.rect(screen, BLACK, [schuilplaats2XR, schuilplaats2YR, schuilplaats2widthR, schuilplaats2heightR],2)


def draw_obstakel():
    pygame.draw.rect(screen, grey, [obstakelX, obstakelY, obstakelwidth, obstakelheight])
    pygame.draw.rect(screen, BLACK, [obstakelX, obstakelY, obstakelwidth, obstakelheight],2)

    
def draw_house():
    pygame.draw.rect(screen, RED, [HuisX, HuisY, huiswidth, huisheight])
    pygame.draw.rect(screen, BLACK, [HuisX, HuisY, huiswidth, huisheight],2)
    pygame.draw.polygon(screen, BLUE, [huisdaklinks, huisdakup, huisdakrechts])
    pygame.draw.polygon(screen, BLACK, [huisdaklinks, huisdakup, huisdakrechts],2)
    pygame.draw.rect(screen, BLACK, [huisraam1X, huisraam1Y, huisraam1width, huisraam1height])
    pygame.draw.rect(screen, BLACK, [huisraam2X, huisraam2Y, huisraam2width, huisraam2height])
    pygame.draw.rect(screen, BLACK, [huisraam3X, huisraam3Y, huisraam3width, huisraam3height])
    pygame.draw.rect(screen, BLACK, [huisraam4X, huisraam4Y, huisraam4width, huisraam4height])
    pygame.draw.rect(screen, WHITE, [huisdeurX, huisdeurY, huisdeurwidth, huisdeurheight])
    pygame.draw.rect(screen, BLACK, [huisdeurX, huisdeurY, huisdeurwidth, huisdeurheight],2)
    pygame.draw.circle(screen, BLACK, (huisdeurknopX, huisdeurknopY), huisdeurknopradius, huisdeurknopwidth)



def water():
    pygame.draw.rect(screen, waterkleur, [waterlijnX, waterlijnY, waterlijnwidth, waterlijnheight])
    pygame.draw.rect(screen, waterkleur, [waterlijn2X, waterlijn2Y, waterlijn2width, waterlijn2height])
    pygame.draw.rect(screen, waterkleur, [waterlijn3X, waterlijn3Y, waterlijn3width, waterlijn3height])

    
#def draw_cloud():
 #   pygame.draw.ellipse(screen, grey, [wolkonderX, wolkonderY, wolkonderwidth, wolkonderheight])
  #  pygame.draw.ellipse(screen, grey, [wolkcirkel1X, wolkcirkel1Y, wolkcirkel1radius, wolkcirkel1width])
   # pygame.draw.ellipse(screen, grey, [wolkcirkel2X, wolkcirkel2Y, wolkcirkel2radius, wolkcirkel2width])
    #pygame.draw.ellipse(screen, grey, [wolkcirkel3X, wolkcirkel3Y, wolkcirkel3radius, wolkcirkel3width])
    #pygame.draw.ellipse(screen, grey, [wolkcirkel4X, wolkcirkel4Y, wolkcirkel4radius, wolkcirkel4width])
#    pygame.draw.ellipse(screen, grey, [wolkcirkel5X, wolkcirkel5Y, wolkcirkel5radius, wolkcirkel5width])
 #   pygame.draw.ellipse(screen, grey, [wolkcirkel6X, wolkcirkel6Y, wolkcirkel6radius, wolkcirkel6width])
  #  pygame.draw.ellipse(screen, grey, [wolkcirkel7X, wolkcirkel7Y, wolkcirkel7radius, wolkcirkel7width])
   # pygame.draw.ellipse(screen, grey, [wolkcirkel8X, wolkcirkel8Y, wolkcirkel8radius, wolkcirkel8width])
    #pygame.draw.ellipse(screen, grey, [wolkcirkel9X, wolkcirkel9Y, wolkcirkel9radius, wolkcirkel9width])
    #pygame.draw.ellipse(screen, grey, [wolkcirkel10X, wolkcirkel10Y, wolkcirkel10radius, wolkcirkel10width])


    
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False


    #pressed_keys = pygame.key.get_pressed()
    #player.update(pressed_keys)

    #screen.blit(player.surf, (400,300))


    draw_ground()
    draw_tree()
    draw_hideout()
    draw_house()
    draw_obstakel()
    water()
    screen.blit(normale_wolk,(x,y))
    
    
    
    pygame.display.flip()
    clock.tick(clock_tick_rate)
