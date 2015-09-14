import pygame, random, sys
from pygame.locals import *

def Ai():
    int = random.randint(0,100)
    bool = False
    if int == 1:
        bool = True
    return bool #Chance of faultering

def Render():
    pygame.display.update()

def Init():
    pygame.init()
    pygame.display.set_caption('P!ng')
    pygame.mouse.set_visible(False)
   
Init() #Init Window

Score = [0,0,0,0] #ScoreBoard Data
PlayerPosition= [50,50,50,50] #PLayer Padels

Width = 1280 #Screen
Height = 720
Boundary = 720 #Margin
PingPong = [375, 375] #Ball
GamePlaying = True #QuitEventArg

mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((Width, Height))
 

while GamePlaying: #Loop
       #Logic here
      for event in pygame.event.get():
        if event.type == QUIT:
            GamePlaying = False
      Render()

pygame.quit()
sys.exit()
