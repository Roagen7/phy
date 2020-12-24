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
        pass




