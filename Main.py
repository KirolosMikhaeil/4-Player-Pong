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
   
def Colis():
    return None

Init() #Init Window

Score = [0,0,0,0] #ScoreBoard Data
PlayerPosition= [50,50,50,50] #PLayer Padels
Moving = [0, 0, 0, 0] # 0=stationary, 1=UP, 2=down

White = (255,255,255)
Black = (0,0,0)

Width = 1280 #Screen
Height = 620
Boundary = 360 #Margin
FPS = 40

PingPong = [375, 375] #Ball
PingPongSpeed = 0 #Ball Speed
PingPongDirection = 1 #Ball Direction
GamePlaying = True #QuitEventArg
PTemp = PlayerPosition
PMove = Moving

mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((Width, Height))
 

while GamePlaying: #Loop
       #Logic here
      pygame.draw.rect(windowSurface, Black, (0,0,Width,Height)) #Clear Screen

      pygame.draw.rect(windowSurface, White, (Boundary, ((Height * (PlayerPosition[0] / 100))-20), 5, 40)) #Player One
      pygame.draw.rect(windowSurface, White, (Width-Boundary-5, ((Height * (PlayerPosition[1] / 100))-20), 5, 40)) #Player Two
      pygame.draw.rect(windowSurface, White, (((Width * (PlayerPosition[2] / 100))-20), 0, 40, 5)) #Player Three
      pygame.draw.rect(windowSurface, White, (((Width * (PlayerPosition[3] / 100))-20), Height-5, 40, 5)) #Player Four
      for event in pygame.event.get():
          if event.type == pygame.KEYUP: 
            if event.key == K_s:
                PMove[0]=0
            if event.key == K_w:
                PMove[0]=0
            if event.key == K_DOWN:
                PMove[1]=0
            if event.key == K_UP:
                PMove[1]=0
          if event.type == pygame.KEYDOWN: 
            if event.key == K_s:
                PMove[0] = 2
            if event.key == K_w:
                PMove[0] = 1
            if event.key == K_DOWN:
                PTemp[1] = 2
            if event.key == K_UP:
                PTemp[1] -= 1
          if event.type == QUIT:
            GamePlaying = False

      for i in PMove:
            if PMove[i] == 1:
                PTemp[i] -= 1
            if PMove[i] == 2:
                PTemp[i] += 1
      Render()

pygame.quit()
sys.exit()
