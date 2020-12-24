import math
import pygame
import time

# ^  -y
#/ \
# | 
# |
# |     x
# ------ >
#       
 


class Area:
    def __init__(self,x,y,size_x,size_y, forces, color):
        self.forces = forces
        self.x = x
        self.y = y
        self.size_x = size_x
        self.size_y = size_y
    
    def apply_forces(self):
        for ball in balls:
            if self.x < ball.x < self.x + self.size and self.y < ball.y < self.y + size:
                ball.clear_forces()
                for force in self.forces:
                    ball.apply_force(force)

    def draw(self):




class Force:
    
    #value - coeficcient's value

    def __init__(self,direction, value):
        self.direction = direction
        self.value = value
        


class Ball:
    def __init__(self,x, y, r, m, surface, color):
        self.x = x;
        self.y = y;
        self.r = r;
        self.m = m;
        self.surface = surface
        self.color = color
        self.forces = []
    
    @property 
    def ax(self):
        return self.ax        

    @property 
    def ay(self):
        return self.ay 

        
    @property
    def vx(self):
        return self.vx

    @property
    def vy(self):
        return self.vy
    
    @property
    def v(self):
        return self.v

    @property
    def angle(self):
        return self.angle

    @vx.getter
    def vx(self):
        return self.__vx
    
    @vy.getter
    def vy(self):
        return self.__vy
    
    @v.getter
    def v(self):
        return math.sqrt(self.__vy**2 + self.__vx**2)
    
    @ax.getter
    def ax(self):
        s = sum([f.value for f in self.forces if f.direction == 'x'])
        return s/self.m
    
    @ay.getter
    def ay(self):
        s = sum([f.value for f in self.forces if f.direction == 'y'])
        return s/self.m



    #angle between V and OX

    @angle.getter
    def angle(self):
        add = 0
        if (self.vx < 0 and self.vy < 0) or (self.vx < 0 and self.vy > 0):
            add = math.pi

        if self.vx != 0 and self.vy != 0:
            return add + math.atan(self.vy/self.vx)
        if self.vx == 0 and self.vy != 0:
            return add + math.pi/2
        return 0

    @vx.setter
    def vx(self,vx):
        self.__vx = vx

    @vy.setter
    def vy(self,vy):
        self.__vy = vy

    def move(self):
        self.x += self.vx
        self.y += self.vy
        self.vx += self.ax/FPS
        self.vy += self.ay/FPS

    def checkIfCollides(self,other):
        if abs(other.x - self.x + other.vx) <= self.r:
            if abs(other.y - self.y + other.vy) <= self.r + 3:
                return True
        return False


    def collision(self,other):
        
        self.vx, other.vx = other.vx, self.vx 
        self.vy, other.vy = other.vy, self.vy


    def apply_force(self,force):
        self.forces.append(force)
    
    def clear_forces(self):
        self.forces = []



    def draw(self):
        pygame.draw.circle(self.surface,self.color,[self.x,self.y],self.r,0) 





def sign(num):
    if num == 0:
        return 0
    elif num > 0:
        return 1
    else:
        return -1

def runCollisions(balls):
    i = 0
    used = []

    for ball1 in balls:
        #print(i+1,ball1.angle)        
        j = 0
        for ball2 in balls:
            if i != j and ball1.checkIfCollides(ball2):
                ball1.collision(ball2)
            j+=1
        i+=1
    for ball in balls:
        if ball.x < 0+borders:
            ball.vx *= -1
            ball.vx /= energy_loss
            ball.x = 0+borders
        if ball.y < 0+borders:
            ball.vy *= -1
            ball.vy /= energy_loss
            ball.y = 0+borders
        if ball.x > width-borders:
            ball.vx *= -1
            ball.vx /= energy_loss
            ball.x = width-borders
        if ball.y > height-borders:
            ball.vy *= -1
            ball.vy /= energy_loss
            ball.y = height-borders
                


#variables

pygame.init()

InfoObject = pygame.display.Info()

width = int(InfoObject.current_w)
height = int(InfoObject.current_h)

gameDisplay = pygame.display.set_mode((width, height))
pygame.display.set_caption("zderzenia.py")
borders = 10
FPS = 30

energy_loss =2


ballx = Ball(500,500,10,20, gameDisplay,(250,0,0))
ballx.vx = -5
ballx.vy = -5
bally = Ball(0,0, 10, 20, gameDisplay,(0,250,0))
bally.vx = 10
bally.vy = 10


balls = [ ballx, bally]


for ball in balls:
    ball.apply_force(Force("y",ball.m * 10))




run = True

while run:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    gameDisplay.fill((0,0,0))
    pygame.draw.rect(gameDisplay,(0,0,125),[width/2, 0, width/2, height],0)


    for ball in balls:
        ball.move()
        ball.draw()
    runCollisions(balls)
    pygame.display.update()
    pygame.time.Clock().tick(FPS)




