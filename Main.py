import pygame, random, sys, math, pygame.font, pygame.draw, string
from pygame.locals import *

full_screen = True



def Tail(now, array):
    a = array
    n = now
    for i in range[4, 20, -1]:
        a[i] = a[i-2]
    a[0] = n[0]
    a[1] = n[1]
    return a

def text(screen, message, size, pox, poy, color):
    fontobject=pygame.font.SysFont('Seogoe UI', size)
    if len(message) != 0:
        screen.blit(fontobject.render(message, 1, color),(pox, poy))

def text2(screen, message, size, pox, poy, color):
    fontobject=pygame.font.SysFont('Courier', size)
    if len(message) != 0:
        screen.blit(fontobject.render(message, 0, color),(pox, poy))

def pAi(stability, pindex):
    inx = 4
    inx -= PLife[pindex]
    s = stability / inx
    bool = True
    if random.randint(0,100) < s:
        bool = False
    return bool #Chance of faultering

def Ai(s):
    bool = True
    if random.randint(0,100) < s:
        bool = False
    return bool #Chance of faultering

def AiMatch(axisY, Aipos, PingX, PingY, pind):
   #    MoveAxis | AiPlayer Position [percent] | PingPong Position
    out = 0
    if pAi(10, pind):
        if axisY:
            if Aipos < PingY:
                if not Aipos < PingY-2 and Ai(2):
                    return 0
                out = 2
            if Aipos > PingY:
                if not Aipos > PingY-2 and Ai(2):
                    return 0
                out = 1
        else:
                if Aipos < PingX:
                    if not Aipos < PingX+2 and Ai(2):
                        return 0
                    out = 2
                elif Aipos > PingX:
                    if not Aipos > PingX+2 and Ai(2):
                        return 0
                    out = 1
                else:
                    out = 0
    else:
        out = 0
    return out

def Render():
    pygame.display.update()

def Init():
    pygame.init()
    pygame.display.set_caption('Glitch P!ng')
    surf = None
    if full_screen:
        surf = pygame.display.set_mode((Width, Height), HWSURFACE | FULLSCREEN | DOUBLEBUF)
    else:
        surf = pygame.display.set_mode((Width, Height))
    return surf
    #pygame.mouse.set_visible(False)
    
def UpdatePingPong(posx, posy, velocity, direcx, direcy):
    dist = (abs((Width/2)-posx) + abs((Height/2)-posy))/100
    v= velocity*1.2 - dist
    #Buggy Velocity from center thing

    posx = posx + (v * direcx)
    posy = posy + (v * direcy)
    return [posx, posy]


def Colis(arect, brect, pingxdir, pongydir, velocity, xybool, SCOREBOARD, INDEX):   #COLLSION OBJECT | xybool x=false, y=true
    v = velocity
    Score = SCOREBOARD
    returnArray = [pingxdir, pongydir, v, Score]
    a = pygame.Rect(arect)
    b = pygame.Rect(brect) 
    if a.colliderect(b): 
        Score[INDEX]+=15
        if(xybool):
            returnArray = [0-pingxdir, math.atan(pongydir), (v+0.3), Score]
        else:
            returnArray = [math.atan(pingxdir), 0-pongydir, (v+0.3), Score]
    return returnArray

def ForceCollison(pingxdir, pongydir, velocity, xybool, SCOREBOARD, INDEX): #Two player option
    v = velocity
    Score = SCOREBOARD
    returnArray = [pingxdir, pongydir, v, Score]
    Score[INDEX]+=15
    if(xybool):
        returnArray = [0-pingxdir, math.atan(pongydir), (v+0.3), Score]
    else:
        returnArray = [math.atan(pingxdir), 0-pongydir, (v+0.3), Score]
    return returnArray

GamemodeSetup = False #Due to bug
Gamemode = "Menu"
Score = [0,0,0,0] #ScoreBoard Data
PlayerPosition= [50,50,50,50] #PLayer Padels %
PlayerLives= [3,3,3,3]
Moving = [0, 0, 0, 0] # 0=stationary, 1=UP/left, 2=down/right

backimg = None
try:
    backimg = pygame.image.load('bg.jpg')
except:
    backimg = pygame.color.Color(0,0,0,0)

life = None
try:
    life = pygame.image.load('heart.png')
except:
    life = pygame.color.Color(0,0,0,0)

White = pygame.color.Color(255,255,255,100)
_2White = pygame.color.Color(255,120,0,70)
_3White = pygame.color.Color(255,0,0,40)
Black = pygame.color.Color(0,0,0,80)

Player1CL = White
Player2CL = White
Player3CL = White
Player4CL = White

RESET = False
Width = 1280
Boundary = 320
if full_screen:
    Width = 1280 #Screen
    Boundary = 320
else:
    Width = 720
    Boundary = 0
Height = 720
FPS = 40

windowSurface = Init() #Init Window

MOVESPEED = 1 #Paddle speed

PingPong = [475, 475] #Ball 
PingPongTail = [475, 475, 475, 475, 475, 475, 475, 475, 475, 475, 475, 475, 475, 475, 475, 475, 475, 475, 475, 475] #Ball Tail
PingPongSpeed = 10 #Ball Speed
PingPongDirection = [(random.randint(-10, 11)/10), (random.randint(-10, 11)/10)] #Ball Direction [x direction, y direction]
GamePlaying = True #QuitEventArg

MenuHighLight = 0

GlitchPos = [0,0,0,0,0][0] # gp[][0] = x; gp[][1] = y
MLG = False
MLGC= (0,0,0)
MLGLevel = 0;
MLGMax = 122

ScoreAdd = Score
PPDir = PingPongDirection
PPPos = PingPong
PPPosT = PingPongTail
PTemp = PlayerPosition
PMove = Moving
PLife = PlayerLives

l = 0
p = 0
mainClock = pygame.time.Clock()
#windowSurface = pygame.display.set_mode((Width, Height))
pygame.mixer.init()
music = pygame.mixer.music.load("Music.wav")
die = pygame.mixer.Sound("die.wav")
pygame.mixer.music.play(-1)
while GamePlaying: #Loop
      
      p = random.randint(0,5)
      if p == 0:
          pygame.display.set_caption('Glitch P!ng')
      if p == 1:
          pygame.display.set_caption('gl!Th pong')
      if p == 2:
          pygame.display.set_caption('Gl!tc( P)ng')
      if p == 3:
          pygame.display.set_caption('Gl!tCh Ping')
      if p == 4:
          pygame.display.set_caption('gLiTch PiNg')
      else:
          pygame.display.set_caption('Glitch P0ng') 

      if Gamemode.lower() == "menu" or Gamemode.lower() == "2 player":
        windowSurface.blit(backimg, (0,0,Width,Height))
        pygame.draw.rect(windowSurface, pygame.color.Color(0,0,0,80), (Width/2-150,Boundary/2,300,600))

        if p == 0:
            text(windowSurface, "Glitch P1ng", 48, 50, 50, (255,255,255))
        if p == 1:
            text(windowSurface, "Gl!tch PIng", 48, 50, 50, (255,255,255))
        if p == 2:
            text(windowSurface, "Glitch P!ng", 48, 50, 50, (255,255,255))
        if p == 3:
            text(windowSurface, "Glitch P)ng", 48, 50, 50, (255,255,255))
        if p > 3:
            text(windowSurface, "Gl1tch P0ng", 48, 50, 50, (255,255,255))
        text(windowSurface, "Menu", 36, Width/2-40, Height/2-140, (255,255,255))
        text(windowSurface, "Play:", 18, Width/2-20, Height/2-80, (255,255,255))
        text(windowSurface, "2 Player [Press |\]", 18, Width/2-60, Height/2-20, (255,255,255))
        text(windowSurface, "3 Player [Press Enter]", 18, Width/2-60, Height/2, (255,255,255))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN: 
                if event.key == K_RETURN:
                    Gamemode = "4 Player"
                if event.key == K_SLASH:
                    Gamemode = "2 Player"
                if event.key == K_SLASH:
                    GamemodeSetup = True
                if event.key == K_ESCAPE:
                    GamePlaying = False
                if event.type == QUIT:
                    GamePlaying = False
        #DRAW MENU
        Render()
      if Gamemode.lower() == "4 player":
          if GamemodeSetup == True:
                MOVESPEED = 1 
                PPPos = [475, 475] #Ball 
                PPPosT = [475, 475, 475, 475, 475, 475, 475, 475, 475, 475, 475, 475, 475, 475, 475, 475, 475, 475, 475, 475] #Ball Tail
                PingPongSpeed = 10 
                PPPDir = [(random.randint(-10, 11)/10), (random.randint(-10, 11)/10)] #Ball Direction [x direction, y direction]
                MLG = False
                MLGLevel = 0
                ScoreAdd = [0,0,0,0] 
                PTemp = [50,50,50,50] 
                PLife = [3,3,3,3]
                PMove = [0, 0, 0, 0] 
                GamemodeSetup = False
          else:
              l = AiMatch(False, ((Width * (PlayerPosition[3] / 100))-20), PingPong[0], PingPong[1], 3)
              if PLife[3] > 0:
                PMove[3]= l
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
                    if event.key == K_ESCAPE:
                        Gamemode = "Menu"
                    if event.key == K_m:
                        if MLG:
                            MLG = False
                        else:
                            MLG = True
                  if event.type == pygame.KEYDOWN: 
                    if event.key == K_s and PLife[0] > 0:
                        PMove[0] = 2
                    if event.key == K_w and PLife[0] > 0:
                        PMove[0] = 1
                    if event.key == K_DOWN and PLife[1] > 0:
                        PMove[1] = 2
                    if event.key == K_UP and PLife[1] > 0:
                        PMove[1] = 1
                  if event.type == pygame.MOUSEBUTTONUP:
                      if event.button == 1:
                          PMove[2] = 0
                      if event.button == 3: 
                          PMove[2] = 0
                  if event.type == pygame.MOUSEBUTTONDOWN:
                      if event.button == 1 and PLife[2] > 0:  
                          PMove[2] = 1       
                      if event.button == 3 and PLife[2] > 0:
                          PMove[2] = 2
                  if event.type == QUIT:
                    Gamemode = "Menu"

              for i in range(0,4):
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

              if(PingPongSpeed > 15):
                  PingPongSpeed = 15;

              if PingPong[0] > Width - Boundary:
                  if PLife[1] <= 0:
                      PPDir[0], PPDir[1], PingPongSpeed, ScoreAdd = ForceCollison(PingPongDirection[0], PingPongDirection[1], PingPongSpeed, True, Score, 1) 
                  else:
                      PLife[1]-=1
                      pygame.mixer.Sound.play(die)
                      ScoreAdd[1] -= 50
                      if MLGLevel < 1:
                        MLGLevel += 0.1
                      RESET = True
              if PingPong[0] < Boundary:
                  if PLife[0] <= 0:
                      PPDir[0], PPDir[1], PingPongSpeed, ScoreAdd = ForceCollison(PingPongDirection[0], PingPongDirection[1], PingPongSpeed, True, Score, 1) 
                  else:
                      PLife[0]-=1
                      pygame.mixer.Sound.play(die)
                      ScoreAdd[0] -= 50
                      if MLGLevel < 1:
                        MLGLevel += 0.1
                      RESET = True
              if PingPong[1] < 0:
                  if PLife[2] <= 0:
                      PPDir[0], PPDir[1], PingPongSpeed, ScoreAdd = ForceCollison(PingPongDirection[0], PingPongDirection[1], PingPongSpeed, False, Score, 1) 
                  else:
                      PLife[2]-=1
                      pygame.mixer.Sound.play(die)
                      ScoreAdd[2] -= 50
                      if MLGLevel < 1:
                        MLGLevel += 0.1
                      RESET = True
              if PingPong[1] > Height:
                  if PLife[3] <= 0:
                      PPDir[0], PPDir[1], PingPongSpeed, ScoreAdd = ForceCollison(PingPongDirection[0], PingPongDirection[1], PingPongSpeed, False, Score, 1) 
                  else:
                      PLife[3]-=1
                      pygame.mixer.Sound.play(die)
                      ScoreAdd[3] -= 3
                      if MLGLevel < 1:
                        MLGLevel += 0.1
                      RESET = True
              if RESET:
                  PPDir[0] = random.randint(-10, 11)/10
                  PPDir[1] = random.randint(-10, 11)/10
                  PPPos[0] = Width/2
                  PPPos[1] = Height/2
                  RESET = False

              if MLG:
                  MLGC = (random.randint(0,int(MLGLevel*MLGMax)),random.randint(0,int(MLGLevel*MLGMax)),random.randint(0,int(MLGLevel*MLGMax)))
              
              if PLife[0] == 3:
                          Player1CL = White
                          ScoreAdd[0] += 3

              elif PLife[0] == 2:
                          Player1CL = _2White
                          ScoreAdd[0] += 2

              elif PLife[0] == 1:
                          Player1CL = _3White
                          ScoreAdd[0] += 1

              else:
                          Player1CL = Black
                          

              if PLife[1] == 3:
                          Player2CL = White
                          ScoreAdd[1] += 3

              elif PLife[1] == 2:
                          Player2CL = _2White
                          ScoreAdd[1] += 2

              elif PLife[1] == 1:
                          Player2CL = _3White
                          ScoreAdd[1] += 1

              else:
                          Player2CL = Black
                          

              if PLife[2] == 3:
                          Player3CL = White
                          ScoreAdd[2] += 3

              elif PLife[2] == 2:
                          Player3CL = _2White
                          ScoreAdd[2] += 2

              elif PLife[2] == 1:
                          Player3CL = _3White
                          ScoreAdd[2] += 1

              else:
                          Player3CL = Black
                          

              if PLife[3] == 3:
                          Player4CL = White
                          ScoreAdd[3] += 3
              elif PLife[3] == 2:
                          Player4CL = _2White
                          ScoreAdd[3] += 2

              elif PLife[i] == 1:
                          Player4CL = _3White
                          ScoreAdd[3] += 1

              else:
                          Player4CL = Black
                          
              #PPPosT = Tail(PPPos, PPPosT)
              PPDir[0], PPDir[1], PingPongSpeed, ScoreAdd = Colis(P1RECT, (PingPong[0], PingPong[1], 4, 4), PingPongDirection[0], PingPongDirection[1], PingPongSpeed, True, Score, 0)
              PPDir[0], PPDir[1], PingPongSpeed, ScoreAdd = Colis(P2RECT, (PingPong[0], PingPong[1], 4, 4), PingPongDirection[0], PingPongDirection[1], PingPongSpeed, True, Score, 1)
              PPDir[0], PPDir[1], PingPongSpeed, ScoreAdd = Colis(P3RECT, (PingPong[0], PingPong[1], 4, 4), PingPongDirection[0], PingPongDirection[1], PingPongSpeed, False, Score, 2)
              PPDir[0], PPDir[1], PingPongSpeed, ScoreAdd = Colis(P4RECT, (PingPong[0], PingPong[1], 4, 4), PingPongDirection[0], PingPongDirection[1], PingPongSpeed, False, Score, 3)
              PPPos[0], PPPos[1] = UpdatePingPong(PingPong[0], PingPong[1], PingPongSpeed, PingPongDirection[0], PingPongDirection[1])
              #Draw Calls -------------------------------------------------------------------------------
      
              #                                     Tail VARS
              #pygame.draw.rect(windowSurface, pygame.color.Color(0,0,0,80), (PPPosT[0], PPPosT[1], 4, 4))
              #pygame.draw.rect(windowSurface, pygame.color.Color(0,0,0,80), (PPPosT[2], PPPosT[3], 4, 4))
              #pygame.draw.rect(windowSurface, pygame.color.Color(0,0,0,80), (PPPosT[4], PPPosT[5], 4, 4))
              #pygame.draw.rect(windowSurface, pygame.color.Color(0,0,0,80), (PPPosT[6], PPPosT[7], 4, 4))
              #pygame.draw.rect(windowSurface, pygame.color.Color(0,0,0,80), (PPPosT[8], PPPosT[9], 4, 4))

              windowSurface.blit(backimg, (0,0,Width,Height))
              if(MLG):
                  pygame.draw.rect(windowSurface, MLGC, (Boundary,0,Width-(2*Boundary),Height)) #MLG effects board
              else:
                pygame.draw.rect(windowSurface, pygame.color.Color(0,0,0,80), (Boundary,0,Width-(2*Boundary),Height)) #Clear board

              if full_screen:
                  text2(windowSurface, "Score", 18, 20, 20, (255,255,255))
                  text2(windowSurface, "Heafty Lefty: "+str(Score[0]), 18, 20, 40, (255,255,255))
                  text2(windowSurface, "Always Right: "+str(Score[1]), 18, 20, 60, (255,255,255))
                  text2(windowSurface, "Mr.MsytMouse: "+str(Score[2]), 18, 20, 80, (255,255,255))
                  text2(windowSurface, "Allan the Ai: "+str(Score[3]), 18, 20, 100, (255,255,255))

                  text2(windowSurface, "Lives:", 18, 20, 140, (255,255,255))
                  text2(windowSurface, "Heafty Lefty: ", 18, 20, 160, (255,255,255))
                  text2(windowSurface, "Always Right: ", 18, 20, 180, (255,255,255))
                  text2(windowSurface, "Mr.MsytMouse: ", 18, 20, 200, (255,255,255))
                  text2(windowSurface, "Allan the Ai: ", 18, 20, 220, (255,255,255))
                  for i in range(0,4):
                    for lives in range(0, PLife[i]):
                        windowSurface.blit(life, (180+(lives*20),161+(i*22),16,16))
                  
              pygame.draw.rect(windowSurface, White, PingPongRect) #Ball

              pygame.draw.rect(windowSurface, Player1CL, P1RECT, 0) #Player One
              pygame.draw.rect(windowSurface, Player2CL, P2RECT, 0) #Player Two
              pygame.draw.rect(windowSurface, Player3CL, P3RECT, 0) #Player Three
              pygame.draw.rect(windowSurface, Player4CL, P4RECT, 0) #Player Four
      
              Render()

pygame.quit()
sys.exit()
