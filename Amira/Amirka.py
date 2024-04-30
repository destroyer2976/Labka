import pygame 
from pygame.locals import *
import sys
import random,time

pygame.init()
FPS=60
frampersec=pygame.time.Clock()
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
BLACK=(0,0,0)
WHITE=(255,255,255)

font= pygame.font.SysFont("Verdana", 60)
smallfont= pygame.font.SysFont("Verdana",20)
gameov= font.render("Game Over", True, BLACK)

backgr= pygame.image.load("/Users/zasulan/Downloads/fornastrgit/Amira/AnimatedStreet — копия.png")
musika=pygame.mixer.Sound("/Users/zasulan/Downloads/fornastrgit/Amira/background — копия.wav").play()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 1000
speed=5
score=0
count=0
 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")
 
 
class parent(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        momimage = pygame.image.load("/Users/zasulan/Downloads/fornastrgit/Amira/photo_2024-04-08 17.15.12.jpeg")
        self.image = pygame.transform.scale(momimage, (80, 80))
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(40,SCREEN_WIDTH-40),0) 
 
      def move(self):
        global score
        self.rect.move_ip(0,speed)
        if (self.rect.top> 600):
            score +=1
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)
 
 
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        Amirkaimage = pygame.image.load("/Users/zasulan/Downloads/fornastrgit/Amira/Amirun.jpeg")
        self.image = pygame.transform.scale(Amirkaimage, (80, 80))
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
 
    def move(self):
        pressed_keys = pygame.key.get_pressed()
       #if pressed_keys[K_UP]:
            #self.rect.move_ip(0, -5)
       #if pressed_keys[K_DOWN]:
            #self.rect.move_ip(0,5)
         
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)

class coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        yoyimage = pygame.image.load("/Users/zasulan/Downloads/fornastrgit/Amira/kinder.jpg")
        self.image = pygame.transform.scale(yoyimage, (65, 65))
        self.rect= self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40),0)
    
    def move(self):
        
        self.rect.move_ip(0,speed)
        if (self.rect.top> 600):
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)
         
P1 = Player()
E1 = parent()
C1=coin()

parents=pygame.sprite.Group()
parents.add(E1)
coinies=pygame.sprite.Group()
coinies.add(C1)
all_sprites=pygame.sprite.Group()
all_sprites.add(E1)
all_sprites.add(P1)
all_sprites.add(C1)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED,1000)

 
while True:     
    for event in pygame.event.get(): 
        if event.type == INC_SPEED:
            speed+=0.5   

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
     
    DISPLAYSURF.blit(backgr,(0,0))
    scores= smallfont.render(str(score),True, BLACK)
    counts=smallfont.render(str(count),True,BLACK)
    DISPLAYSURF.blit(scores,(10,10))
    DISPLAYSURF.blit(counts,(390,10))

    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
    if pygame.sprite.spritecollideany(P1,coinies):
       pygame.mixer.Sound("/Users/zasulan/Downloads/fornastrgit/Amira/collect-5930 — копия.mp3").play()
    
       for bonus in coinies:
        bonus.rect.top =0
        bonus.rect.center = (random.randint(30,370),0)
        count+=1

    pygame.display.flip()

    collision_found = False
    for parent in parents:
        if pygame.sprite.spritecollideany(parent, coinies):
           collision_found = True
           break 

    if not collision_found:
        pass

    if pygame.sprite.spritecollideany(P1,parents):
        pygame.mixer.Sound('/Users/zasulan/Downloads/fornastrgit/Amira/crash — копия.wav').play()
        time.sleep(0.5)

        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(gameov,(30,250))
    
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
             
        time.sleep(2)
        pygame.quit()
        sys.exit()
        
         
    pygame.display.update()
    frampersec.tick(FPS)



