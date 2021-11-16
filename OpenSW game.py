import os
import pygame

class Player(object):
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 10, 10)
        self.hp = 3
    
    def move(self, speedx, speedy):
            self.move_single_axis(speedx, 0)
            self.move_single_axis(0, speedy)
            
    def move_single_axis(self, speedx, speedy):
        self.rect.x += speedx
        self.rect.y += speedy
        
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if speedx > 0:
                    self.rect.right = wall.rect.left
                if speedx < 0:
                    self.rect.left = wall.rect.right
                if speedy > 0:
                    self.rect.bottom = wall.rect.top
                if speedy < 0:
                    self.rect.top = wall.rect.bottom
        
        for trap in traps:
            if self.rect.colliderect(trap.rect):
                if speedx > 0:
                    self.rect.right = trap.rect.left - 5
                if speedx < 0:
                    self.rect.left = trap.rect.right + 5
                if speedy > 0:
                    self.rect.bottom = trap.rect.top - 5
                if speedy < 0:
                    self.rect.top = trap.rect.bottom + 5
                self.hp -= 1
                
    def delete(self):
        self.rect = pygame.Rect(x, y, 0, 0)
        
class End(object):
    def __init__(self, pos):
        ends.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)
    
    def delete(self):
        del ends[:]

class Wall(object):
    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)
    
    def delete(self):
        del walls[:]
        

class Trap(object):
    def __init__(self, pos):
        traps.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)
    
    def delete(self):
        del traps[:]

os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()

screen = pygame.display.set_mode((432, 432))

#map var
clock = pygame.time.Clock()
walls = []
traps = []
ends = []
lights = []

player1 = Player(20, 30)
player2 = Player(20, 392)

black = (0, 0, 0)

#map
level1 = [
    "WWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "W  E     TW WW TW         W",
    "W WWWWWT TW     T  T  W   W",
    "W WTTT   WT   T    T  W   W",
    "W      T  W  TW TT W  W   W",
    "W WWWW        W W  W  WT  W",
    "W      W   WTTT W    TWT  W",
    "W TTT  WWW WW      TT     W",
    "W T           W T     WT  W",
    "W   WT  WW TW T T     TW  W",
    "W T   W tW W  W WW   WTW  W",
    "W     W WT  W T  TWW  T   W",
    "W  WTTT                  EW",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "W  TTTTWWTTTTWWWWWWWWT   EW",
    "W       WT      T      TW W",
    "W TWWW TWT TT T     WTTTW W",
    "W          TW WWW   W W W W",
    "W WW  TWWWWWW WT      W T W",
    "W     TWTT       WWT TT   W",
    "W WWWW WT  TW   WWT     TWW",
    "W W    W   TW W      WWWT W",
    "W   WW   WWWWWW TT T      W",
    "W W    T      W WW WT  WT W",
    "W W TWWWWT T  W TT WWT W  W",
    "W E        T              W",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWW",
]

level2 = [
    "WWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "W      T    EW            W",
    "W TWT  W  T WW   WWWWWW   W",
    "W            W        W   W",
    "W WWW TWW  T W        W   W",
    "W  T     T   W        W   W",
    "WW W  W WWW TW   WWWWWW   W",
    "W    W      TW   W        W",
    "W TWWW  T W TW   W        W",
    "W W    W  T WW   W        W",
    "W    WWT WW  W   WWWWWW   W",
    "WWT WW   W  WW            W",
    "W W T  W WT  W            W",
    "W   T  W T   WWWWWWWWWWWWWW",
    "W W    T     W  T  TWW   EW",
    "W W WT TWT  WT  W      WT W",
    "W T        W      TWW  T  W",
    "W TWWT WW WTTW TT   W  W  W",
    "W    W  TW       TT       W",
    "W T     WTTWT WW    WTT W W",
    "WWWW WWW    W   T   W     W",
    "W     W  T    T    WT WTW W",
    "W TT W WWW  T W TW TW WT  W",
    "WEWWWT      T    W        W",
    "W WWWT W TTWWW TWW TW  W  W",
    "W  E   T       TW   T  W  W",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWW",
]

level3 = [
    "WWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "W    W    TW   TW    WE   W",
    "W W  T T     T    TW   TW W",
    "W W       WW  WWT  W  WWTEW",
    "W    W  W          T  W   W",
    "W WW   WWTTW  TT     W   WW",
    "W    T    W   WWW W WWW   W",
    "WWW TWWT  TWW  T  WW      W",
    "W     W    T     TWT TWT  W",
    "W  T WW TW   T WWW        W",
    "WT              W   TWT WWW",
    "WW TWT WW TW   WT W       W",
    "WE        TW  W     W   T W",
    "WWWWWWWWWWWWWW WW  WTT WT W",
    "W           W          T  W",
    "W  WWWWWWW  WWW  T TT     W",
    "W        W  W    W W W  TWW",
    "W        W  W TT   W   WW W",
    "W        W  W    W TT     W",
    "W  WWWWWWW  W  W      T   W",
    "W        W  W  T TT WW   TW",
    "W        W  W       WT W  W",
    "W        W  WWW T         W",
    "W  WWWWWWW  WT  T  W WTTT W",
    "W           W  TWT     T  W",
    "W           WE      WW    W",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWW",
]

check1 = True
check2 = True

#start
#level 1
if check1 == True and check2 == True:
    while 1:
        clock.tick(60)
        
        #level 1 range of function
        x = y = 0
        for row in level1:
            for col in row:
                if col == "W":
                    Wall((x, y))
                if col == "E":
                    End((x, y))
                    end_rect = pygame.Rect(x, y, 16, 16)
                if col == "T":
                    Trap((x, y))
                    trap_rect = pygame.Rect(x, y, 16, 16)
                x += 16
            y += 16
            x = 0
    
        #level 1 map create
        screen.fill((0, 0, 0))
        for wall in walls:
            pygame.draw.rect(screen, (255, 255, 255), wall.rect)
        for end in ends:
            pygame.draw.rect(screen, (255, 255, 0), end.rect)
        for trap in traps:
            pygame.draw.rect(screen, (255, 0, 0), trap.rect)
        pygame.draw.rect(screen, (255, 200, 0), player1.rect)
        pygame.draw.rect(screen, (255, 200, 0), player2.rect)
        pygame.display.flip()
    
        #level 1 quit ways
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                pygame.quit()
    
        #level 1 player's move
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            player1.move(-2.5, 0)
            player2.move(-2.5, 0)
        if key[pygame.K_RIGHT]:
            player1.move(2.5, 0)
            player2.move(2.5, 0)
        if key[pygame.K_UP]:
            player1.move(0, 2.5)
            player2.move(0, -2.5)
        if key[pygame.K_DOWN]:
            player1.move(0, -2.5)
            player2.move(0, 2.5)
    
        #level 1 function
        if player1.rect.colliderect(end_rect) or player2.rect.colliderect(end_rect):
            player1.rect.x = 20
            player1.rect.y = 400
            player2.rect.x = 20
            player2.rect.y = 400
            check1 = True
            check2 = False
            wall.delete()
            end.delete()
            trap.delete()
            break;
        if player1.rect.colliderect(trap_rect) or player2.rect.colliderect(trap_rect):
            player1.hp -= 1
            player2.hp -= 1
        if player1.hp <= 0 or player2.hp <= 0:
            pygame.quit()

        clock.tick(360)


#level 2        
if check1 == True and check2 == False:
    while 1:
        clock.tick(60)
        x = y = 0
        for row in level2:
            for col in row:
                if col == "W":
                    Wall((x, y))
                if col == "E":
                    End((x, y))
                    end_rect = pygame.Rect(x, y, 16, 16)
                if col == "T":
                    Trap((x, y))
                    trap_rect = pygame.Rect(x, y, 16, 16)
                x += 16
            y += 16
            x = 0
    
        #level 2 map create
        screen.fill((0, 0, 0))
        for wall in walls:
            pygame.draw.rect(screen, (255, 255, 255), wall.rect)
        for end in ends:
            pygame.draw.rect(screen, (255, 255, 0), end.rect)
        for trap in traps:
            pygame.draw.rect(screen, (255, 0, 0), trap.rect)
        pygame.draw.rect(screen, (255, 200, 0), player1.rect)
        pygame.draw.rect(screen, (255, 200, 0), player2.rect)
        pygame.display.flip()
        
        #level 2 quit ways
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                pygame.quit()
    
        #level 2 player's move
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            player1.move(-2.5, 0)
            player2.move(0, 2.5)
        if key[pygame.K_RIGHT]:
            player1.move(2.5, 0)
            player2.move(0, -2.5)
        if key[pygame.K_UP]:
            player1.move(0, -2.5)
            player2.move(2.5, 0)
        if key[pygame.K_DOWN]:
            player1.move(0, 2.5)
            player2.move(-2.5, 0)
        
        #level 2 function
        if player1.rect.colliderect(end_rect) or player2.rect.colliderect(end_rect):
            player1.rect.x = 400
            player1.rect.y = 30
            player2.rect.x = 400
            player2.rect.y = 30
            check1 = False
            check2 = True
            wall.delete()
            end.delete()
            trap.delete()
            break;
        if player1.rect.colliderect(trap_rect) or player2.rect.colliderect(trap_rect):
            player1.hp -= 1
            player2.hp -= 1
        if player1.hp == 0 or player2.hp == 0:
            pygame.quit()

        clock.tick(360)


#level 3
if check1 == False and check2 == True:
    while 1:
        
        clock.tick(60)
        
        #level 3 range of function
        x = y = 0
        for row in level3:
            for col in row:
                if col == "W":
                    Wall((x, y))
                if col == "E":
                    End((x, y))
                    end_rect = pygame.Rect(x, y, 16, 16)
                if col == "T":
                    Trap((x, y))
                    trap_rect = pygame.Rect(x, y, 16, 16)
                x += 16
            y += 16
            x = 0

        #level 3 map create
        screen.fill((0, 0, 0))
        for wall in walls:
            pygame.draw.rect(screen, (255, 255, 255), wall.rect)
        for end in ends:
            pygame.draw.rect(screen, (255, 255, 0), end.rect)
        for trap in traps:
            pygame.draw.rect(screen, (255, 0, 0), trap.rect)
        pygame.draw.rect(screen, (255, 200, 0), player1.rect)
        pygame.draw.rect(screen, (255, 200, 0), player2.rect)
        pygame.display.flip()
        
    
        #level 3 quit ways
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                pygame.quit()
    
        #level 3 player's move
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            player1.move(-2.5, 0)
            player2.move(0, 2.5)
        if key[pygame.K_RIGHT]:
            player1.move(2.5, 0)
            player2.move(0, -2.5)
        if key[pygame.K_UP]:
            player1.move(0, -2.5)
            player2.move(2.5, 0)
        if key[pygame.K_DOWN]:
            player1.move(0, 2.5)
            player2.move(-2.5, 0)
    
        #level 3 function
        if player1.rect.colliderect(end_rect) or player2.rect.colliderect(end_rect):
            check1 = False
            check2 = False
            wall.delete()
            end.delete()
            trap.delete()
            player1.delete()
            player2.delete()
            break;            
        if player1.rect.colliderect(trap_rect) or player2.rect.colliderect(trap_rect):
            player1.hp -= 1
            player2.hp -= 1
        if player1.hp == 0 or player2.hp == 0:
            pygame.quit()
    
        clock.tick(360)

#game clear
if check1 == False and check2 == False:
    while 1:
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render('Game Clear', True, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (216, 216)
        clock.tick(60)
        screen.fill((0, 0, 0))
        screen.blit(text, textRect)
        
    
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                pygame.quit()
        clock.tick(360)

pygame.quit()