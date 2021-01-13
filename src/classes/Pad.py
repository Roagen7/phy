class Pad:
    def __init__(self, x1, y1, x2, y2, t):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.t = t

    @property
    def angle(self):
        return self.angle

    @angle.getter
    def angle(self):
        import math
        
        if self.y2 == self.y1:
            return 0
        if self.x2 == self.x1:
            return math.pi/2

        deg = math.atan(abs((self.y2-self.y1)/(self.x2-self.x1)))


        if (self.x2 - self.x1) * (self.y2 - self.y1) < 0:
            return math.pi - deg



        return deg

    def bounce(self,balls):
        import math

        for ball in balls:
            if ball.deflect:
                continue
            if self.x1 == self.x2:
                if min(self.y1, self.y2) < ball.y < max(self.y1,self.y2):
                    if abs(self.x1 - ball.x) < ball.r  + ball.v:
                        ball.vx *= -1
                        ball.deflect = True 
                continue
            
            if self.y1 == self.y2:
                if min(self.x1, self.x2) < ball.x < max(self.x1, self.x2):
                    if abs(self.y1 - ball.y) < ball.r + ball.v:
                        ball.vy *= -1
                        ball.deflect = True
                continue

            if ( min(self.x1, self.x2) < ball.x < max(self.x2,self.x1) ) and ( min(self.y1, self.y2) < ball.y < max(self.y1,self.y2) ):  
                                    
                a = (self.y2-self.y1)/(self.x2-self.x1)
                b = self.y1 - (a * self.x1)

                if(abs(ball.y - ball.x * a - b) < ball.r + ball.v):
                    #if abs(ball.y - b - a * ball.x)/math.sqrt(a*a + 1) < abs(ball.y + ball.vy - b - a * (ball.x + ball.vx))/math.sqrt(a*a+1):
                    #    return

                    change_angle = math.pi/2 - (self.angle - ball.angle)
                    ball.angle += 2*(self.angle-ball.angle)
                    ball.deflect = True
                    continue
                    #ball.move()
                    #ball.vx *= -1
                    #ball.vy *= -1



        
    
    def draw(self,pygame,screen):
        pygame.draw.line(screen, (250,250,250), (self.x1, self.y1), (self.x2, self.y2), self.t)






