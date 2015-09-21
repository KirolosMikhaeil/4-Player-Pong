import pygame, random, sys, math
from pygame.locals import *

def Ai():
    bool = True
    if random.randint(0,100) == 1:
        bool = False
    return bool #Chance of faultering

def AiMatch(axisY, Aipos, PingX, PingY):
   #    MoveAxis | AiPlayer Position [percent] | PingPong Position
    out = 0
    if Ai():
        if axisY:
            if Aipos < PingY:
                out = 1
            if Aipos > PingY:
                out = 2
        else:
                if Aipos < PingX:
                    out = 1
                elif Aipos > PingX:
                    out = 2
                else:
                    out = 0
    else:
        out = 0

    return out

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


def Colis(arect, brect, pingxdir, pongydir, velocity, xybool, SCOREBOARD, INDEX):   #COLLSION OBJECT | xybool x=false, y=true
    v = velocity
    Score = SCOREBOARD
    returnArray = [pingxdir, pongydir, v, Score]
    a = pygame.Rect(arect)
    b = pygame.Rect(brect) 
    if a.colliderect(b): 
        Score[INDEX]+=15
        #returnArray = [0-pingxdir, 1-pongydir] #invert Direction? 
        if(xybool):
            returnArray = [0-pingxdir, math.atan(pongydir), (v+0.1), Score]
        else:
            returnArray = [math.atan(pingxdir), 0-pongydir, (v+0.1), Score]
    return returnArray


Init() #Init Window

Score = [0,0,0,0] #ScoreBoard Data
PlayerPosition= [50,50,50,50] #PLayer Padels %
PlayerLives= [3,3,3,3]
Moving = [0, 0, 0, 0] # 0=stationary, 1=UP/left, 2=down/right

backimg = None
try:
    backimg = pygame.image.load('bg.jpg')
except:
    try:
        backimg = pygame.image.load('bg.jpeg')
    except:
        backimg = pygame.image.load('bg.png')

White = pygame.color.Color(255,255,255,100)
_2White = pygame.color.Color(255,120,0,70)
_3White = pygame.color.Color(255,0,0,40)
Black = pygame.color.Color(0,0,0,80)
Player1CL = White
Player2CL = White
Player3CL = White
Player4CL = White

RESET = False
Width = 1280 #Screen
Height = 720
Boundary = 320 #Margin
FPS = 40

MOVESPEED = 1 #Paddle speed

PingPong = [475, 475] #Ball
PingPongSpeed = 4 #Ball Speed
PingPongDirection = [-1, (random.randint(-10, 11)/10)] #Ball Direction [x direction, y direction]
GamePlaying = True #QuitEventArg

ScoreAdd = Score
PPDir = PingPongDirection
PPPos = PingPong
PTemp = PlayerPosition
PMove = Moving
PLife = PlayerLives

mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((Width, Height))
while GamePlaying: #Loop
      
      # Ai
      PMove[3] = AiMatch(False, PTemp[3], PingPong[0], PingPong[1])
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
                PMove[1] = 2
            if event.key == K_UP:
                PMove[1] = 1
          if event.type == pygame.MOUSEBUTTONUP:
              if event.button == 1:
                  PMove[2] = 0
              if event.button == 3: 
                  PMove[2] = 0
          if event.type == pygame.MOUSEBUTTONDOWN:
              if event.button == 1:  
                  PMove[2] = 1       
              if event.button == 3:
                  PMove[2] = 2
          if event.type == QUIT:
            GamePlaying = False

      for i in PMove:
            if PMove[i] == 1:
                PTemp[i] -= MOVESPEED  #Error here with top player
            if PMove[i] == 2:
                PTemp[i] += MOVESPEED
      #LOGIC
      P1RECT = (Boundary, ((Height * (PlayerPosition[0] / 100))-20), 5, 40)
      P2RECT = (Width-Boundary-5, ((Height * (PlayerPosition[1] / 100))-20), 5, 40)
      P3RECT = (((Width * (PlayerPosition[2] / 100))-20), 0, 40, 5)
      P4RECT = (((Width * (PlayerPosition[3] / 100))-20), Height-5, 40, 5)

      PingPongRect = (PingPong[0], PingPong[1], 4, 4)

      if PingPong[0] > Width - Boundary:
          PLife[1]-=1
          ScoreAdd[1] -= 50
          RESET = True
      if PingPong[0] < Boundary:
          PLife[0]-=1
          ScoreAdd[0] -= 50
          RESET = True
      if PingPong[1] < 0:
          PLife[3]-=1
          ScoreAdd[3] -= 50
          RESET = True
      if PingPong[1] > Height:
          PLife[2]-=1
          ScoreAdd[2] -= 3
          RESET = True

      if RESET:
          PPDir[0] = -1
          PPDir[1] = random.randint(-10, 11)/10
          PPPos[0] = Width/2
          PPPos[1] = Height/2
          RESET = False
      
      for i in PLife:
          if i == 0:
              if PLife[i] == 3:
                  Player1CL = White
                  ScoreAdd[0] += 3

              elif PLife[i] == 2:
                  Player1CL = _2White
                  ScoreAdd[0] += 2

              elif PLife[i] == 1:
                  Player1CL = _3White
                  ScoreAdd[0] += 1

              elif PLife[i] == 0:
                  Player1CL = Black
          elif i == 1:
              if PLife[i] == 3:
                  Player2CL = White
                  ScoreAdd[1] += 3

              elif PLife[i] == 2:
                  Player2CL = _2White
                  ScoreAdd[1] += 2

              elif PLife[i] == 1:
                  Player2CL = _3White
                  ScoreAdd[1] += 1

              elif PLife[i] == 0:
                  Player2CL = Black
          elif i == 2:
              if PLife[i] == 3:
                  Player3CL = White
                  ScoreAdd[2] += 3

              elif PLife[i] == 2:
                  Player3CL = _2White
                  ScoreAdd[2] += 2

              elif PLife[i] == 1:
                  Player3CL = _3White
                  ScoreAdd[2] += 1

              elif PLife[i] == 0:
                  Player3CL = Black
          elif i == 3:
              if PLife[i] == 3:
                  Player4CL = White
                  ScoreAdd[3] += 3

              elif PLife[i] == 2:
                  Player4CL = _2White
                  ScoreAdd[3] += 2

              elif PLife[i] == 1:
                  Player4CL = _3White
                  ScoreAdd[3] += 1

              elif PLife[i] == 0:
                  Player4CL = Black

      PPDir[0], PPDir[1], PingPongSpeed, ScoreAdd = Colis(P1RECT, (PingPong[0], PingPong[1], 4, 4), PingPongDirection[0], PingPongDirection[1], PingPongSpeed, True, Score, 0)
      PPDir[0], PPDir[1], PingPongSpeed, ScoreAdd = Colis(P2RECT, (PingPong[0], PingPong[1], 4, 4), PingPongDirection[0], PingPongDirection[1], PingPongSpeed, True, Score, 1)
      PPDir[0], PPDir[1], PingPongSpeed, ScoreAdd = Colis(P3RECT, (PingPong[0], PingPong[1], 4, 4), PingPongDirection[0], PingPongDirection[1], PingPongSpeed, False, Score, 2)
      PPDir[0], PPDir[1], PingPongSpeed, ScoreAdd = Colis(P4RECT, (PingPong[0], PingPong[1], 4, 4), PingPongDirection[0], PingPongDirection[1], PingPongSpeed, False, Score, 3)
      PPPos[0], PPPos[1] = UpdatePingPong(PingPong[0], PingPong[1], PingPongSpeed, PingPongDirection[0], PingPongDirection[1])
      #Draw Calls -------------------------------------------------------------------------------
      
      #                                     REPALCE RECTS WITH VARS
      windowSurface.blit(backimg, (0,0,Width,Height))
      pygame.draw.rect(windowSurface, pygame.color.Color(0,0,0,80), (Boundary,0,Width-(2*Boundary),Height)) #Clear board
      pygame.draw.rect(windowSurface, White, PingPongRect) #Ball

      pygame.draw.rect(windowSurface, Player1CL, P1RECT, 0) #Player One
      pygame.draw.rect(windowSurface, Player2CL, P2RECT, 0) #Player Two
      pygame.draw.rect(windowSurface, Player3CL, P3RECT, 0) #Player Three
      pygame.draw.rect(windowSurface, Player4CL, P4RECT, 0) #Player Four
      
      Render()

pygame.quit()
sys.exit()
