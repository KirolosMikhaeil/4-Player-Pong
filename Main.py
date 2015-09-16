import pygame, random, sys
from pygame.locals import *

def Ai():
    int = random.randint(0,100)
    bool = True
    if int == 1:
        bool = False
    return bool #Chance of faultering

def AiMatch(axisY, Aipos, PingX, PingY):
   #    MoveAxis | AiPlayer Position [percent] | PingPong Position
    if axisY:
        if Aipos < PingY and Ai():
            Aipos += MOVESPEED
        if Aipos > PingY and Ai():
            Aipos -= MOVESPEED
    else:
            if Aipos < PingX and Ai():
                Aipos += MOVESPEED
            if Aipos > PingX and Ai():
                Aipos -= MOVESPEED

    return Aipos

def Render():
    pygame.display.update()

def Init():
    pygame.init()
    pygame.display.set_caption('P!ng')
    #pygame.mouse.set_visible(False)
    
def Logic(a, b):
    return a, b


def Colis(arect, brect, pingxdir, pongydir):   #COLLSION OBJECT
    if arect.colliderect(brect):
        returnArray[0-pingxdir, 0-pongydir] #invert Direction? 
    return returnArray

Init() #Init Window

Score = [0,0,0,0] #ScoreBoard Data
PlayerPosition= [50,50,50,50] #PLayer Padels
PlayerLives= [3,3,3,3]
Moving = [0, 0, 0, 0] # 0=stationary, 1=UP, 2=down

backimg = pygame.image.load('bg.jpg')

White = (255,255,255)
Black = (0,0,0)
Player1CL = White
Player2CL = White
Player3CL = White
Player4CL = White

Width = 1280 #Screen
Height = 720
Boundary = 320 #Margin
FPS = 40

MOVESPEED = 0.4

PingPong = [475, 475] #Ball
PingPongSpeed = 1 #Ball Speed
PingPongDirection = [0, 0] #Ball Direction [x, ydirection]
GamePlaying = True #QuitEventArg

PPDir = PingPongDirection
PPPos = PingPong
PTemp = PlayerPosition
PMove = Moving

mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((Width, Height))
 

while GamePlaying: #Loop
      
      #Logic Calls
      #PingPong, PingPongSpeed, PingPongDirection = PingPongLogic(PingPong, PingPongSpeed, PingPongDirection)
      # Ai
      PTemp[3] = AiMatch(False, PTemp[3], PingPong[0], PingPong[1])
      #Input Call----------------------------------------------------------------
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
      PTemp[2], y =pygame.mouse.get_pos() #rel?
      PTemp[2] = PTemp[2] / Width
      for i in PMove:
            if PMove[i] == 1:
                PTemp[i] -= MOVESPEED
            if PMove[i] == 2:
                PTemp[i] += MOVESPEED
      #for i in PTemp:
      #    Set up Rect
      #    PPDir = Colis(None, (PingPong[0], PingPong[1], 4, 4), PingPongDirection[0], PingPongDirection[1])
      #Draw Calls -------------------------------------------------------------------------------
      
      #                                     REPALCE RECTS WITH VARS
      windowSurface.blit(backimg, (0,0,Width,Height))
      pygame.draw.rect(windowSurface, Black, (Boundary,0,Width-(2*Boundary),Height)) #Clear board
      pygame.draw.rect(windowSurface, White, (PingPong[0], PingPong[1], 4, 4)) #Ball

      pygame.draw.rect(windowSurface, Player1CL, (Boundary, ((Height * (PlayerPosition[0] / 100))-20), 5, 40)) #Player One
      pygame.draw.rect(windowSurface, Player2CL, (Width-Boundary-5, ((Height * (PlayerPosition[1] / 100))-20), 5, 40)) #Player Two
      pygame.draw.rect(windowSurface, Player3CL, (((Width * (PlayerPosition[2] / 100))-20), 0, 40, 5)) #Player Three
      pygame.draw.rect(windowSurface, Player4CL, (((Width * (PlayerPosition[3] / 100))-20), Height-5, 40, 5)) #Player Four
      
      Render()

pygame.quit()
sys.exit()
