class Force:
    
    #value - coeficcient's value

    def __init__(self,direction, value):
        self.direction = direction
        self.value = value
        

    def reevaluate(self, param):
        
        return Force(self.direction, self.value*param)


