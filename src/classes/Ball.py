
class Ball:
    def __init__(self,x, y, r, m,  color, FPS):
        self.x = x;
        self.y = y;
        self.r = r;
        self.m = m;
        #self.surface = surface
        self.color = color
        self.forces = []
        self.FPS = FPS
    
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
        self.vx += self.ax/self.FPS
        self.vy += self.ay/self.FPS
        self.clear_forces()

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

    def draw(self, pygame, surface):
        pygame.draw.circle(surface,self.color,[self.x,self.y],self.r,0) 



