class Center:
    def __init__(self,x,y, r, m, color, force_x, force_y):
        self.x = x
        self.y = y
        self.r = r
        self.m = m
        self.color = color
        self.force_x = force_x
        self.force_y = force_y

    def apply_forces(self, balls):
        import math
        for ball in balls:
            dx = self.x - ball.x
            dy = self.y - ball.y
            forces = ball.forces 
            d = math.sqrt(dx*dx + dy*dy)
            if d != 0:
                F = self.m * ball.m / d * d                
                if dx != 0:
                    Fc = math.sqrt(F*F/((dy*dy/(dx*dx))+1))
                    ball.apply_force(self.force_x.reevaluate(dx/abs(dx)*Fc))
                if dy != 0:
                    Fc = math.sqrt(F*F/((dx*dx/(dy*dy))+1))
                    ball.apply_force(self.force_y.reevaluate(dy/abs(dy)*Fc))


    def draw(self, pygame, surface):
        pygame.draw.circle(surface,self.color,[self.x,self.y],self.r,0) 



