import pygame, random, sys, math
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
    
def UpdatePingPong(posx, posy, velocity, direcx, direcy):
    posx = posx + (velocity * direcx)
    posy = posy + (velocity * direcy)
    return [posx, posy]


def Colis(arect, brect, pingxdir, pongydir):   #COLLSION OBJECT
    returnArray = [pingxdir, pongydir]
    a = pygame.Rect(arect)
    b = pygame.Rect(brect) 
    if a.colliderect(b): 
        #returnArray = [0-pingxdir, 1-pongydir] #invert Direction? 
        returnArray = [0-pingxdir, math.atan(pongydir)]
    return returnArray

Init() #Init Window

Score = [0,0,0,0] #ScoreBoard Data
PlayerPosition= [50,50,50,50] #PLayer Padels
PlayerLives= [3,3,3,3]
Moving = [0, 0, 0, 0] # 0=stationary, 1=UP, 2=down

backimg = pygame.image.load('bg.jpg')

White = (255,255,255)
Black = (0,0,0,80)
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
PingPongSpeed = 2 #Ball Speed
PingPongDirection = [-1, (random.randint(-10, 11)/10)] #Ball Direction [x, ydirection]
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
                PTemp[1] = 1
          if event.type == pygame.MOUSEBUTTONUP:
              if event.button == 1:
                  PMove[2] = 0
              if event.button == 3: 
                  PMove[2] = 0
          if event.type == pygame.MOUSEBUTTONDOWN:
              if event.button == 1:
                  PMove[2] = 2
              if event.button == 3:
                  PMove[2] = 1
          if event.type == QUIT:
            GamePlaying = False
      for i in PMove:
            if PMove[i] == 1:
                PTemp[i] -= MOVESPEED
            if PMove[i] == 2:
                PTemp[i] += MOVESPEED
      #LOGIC
      P1RECT = (Boundary, ((Height * (PlayerPosition[0] / 100))-20), 5, 40)
      P2RECT = (Width-Boundary-5, ((Height * (PlayerPosition[1] / 100))-20), 5, 40)
      P3RECT = (((Width * (PlayerPosition[2] / 100))-20), 0, 40, 5)
      P4RECT = (((Width * (PlayerPosition[3] / 100))-20), Height-5, 40, 5)

      PingPongRect = (PingPong[0], PingPong[1], 4, 4)

      if PingPong[0] > Width - Boundary or PingPong[0] < Boundary or PingPong[1] < 0 or PingPong[1] > Height:
          PPDir = [-1, (random.randint(-10, 11)/10)]
          PPPos = [Width/2, Height/2]
          
      PPDir[0], PPDir[1] = Colis(P1RECT, (PingPong[0], PingPong[1], 4, 4), PingPongDirection[0], PingPongDirection[1])
      PPDir[0], PPDir[1] = Colis(P2RECT, (PingPong[0], PingPong[1], 4, 4), PingPongDirection[0], PingPongDirection[1])
      PPDir[0], PPDir[1] = Colis(P3RECT, (PingPong[0], PingPong[1], 4, 4), PingPongDirection[0], PingPongDirection[1])
      PPDir[0], PPDir[1] = Colis(P4RECT, (PingPong[0], PingPong[1], 4, 4), PingPongDirection[0], PingPongDirection[1])
      PPPos[0], PPPos[1] = UpdatePingPong(PingPong[0], PingPong[1], PingPongSpeed, PingPongDirection[0], PingPongDirection[1])
      #Draw Calls -------------------------------------------------------------------------------
      
      #                                     REPALCE RECTS WITH VARS
      windowSurface.blit(backimg, (0,0,Width,Height))
      pygame.draw.rect(windowSurface, (0,0,0,80), (Boundary,0,Width-(2*Boundary),Height)) #Clear board
      pygame.draw.rect(windowSurface, White, PingPongRect) #Ball

      pygame.draw.rect(windowSurface, Player1CL, P1RECT) #Player One
      pygame.draw.rect(windowSurface, Player2CL, P2RECT) #Player Two
      pygame.draw.rect(windowSurface, Player3CL, P3RECT) #Player Three
      pygame.draw.rect(windowSurface, Player4CL, P4RECT) #Player Four
      
      Render()

pygame.quit()
sys.exit()
