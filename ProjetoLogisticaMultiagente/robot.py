class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = "N"
        
    def move_forward(self):
        if self.direction == "N":
            self.y -= 1
        elif self.direction == "S":
            self.y += 1
        elif self.direction == "E":
            self.x += 1
        elif self.direction == "W":
            self.x += 1
    
    def turn_right(self):
        if self.direction == "N":
            self.direction == "E"
        elif self.direction == "E":
            self.direction == "S"
        elif self.direction == "S":
            self.direction == "W"
        elif self.direction == "W":
            self.direction == "N"
            
    def turn_left(self):
        if self.direction == "N":
            self.direction == "W"
        elif self.direction == "W":
            self.direction == "S"
        elif self.direction == "S":
            self.direction == "E"
        elif self.direction == "E":
            self.direction == "N"
        
    