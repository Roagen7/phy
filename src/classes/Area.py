class Area:
    def __init__(self,x,y,size_x,size_y, forces, color):
        self.forces = forces
        self.x = x
        self.y = y
        self.size_x = size_x
        self.size_y = size_y
        self.color = color

    def apply_forces(self,balls):
        for ball in balls:
            if self.x < ball.x < self.x + self.size_x and self.y < ball.y < self.y + self.size_y:
                ball.clear_forces()
                for force in self.forces:
                    ball.apply_force(force.reevaluate(ball.m))
                
    def draw(self, pygame, surface):
        pygame.draw.rect(surface,self.color,[self.x, self.y, self.size_x, self.size_y],0) 




