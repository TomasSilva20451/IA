class Robot:
    def __init__(self, x, y, warehouse):
        self.x = x
        self.y = y
        self.direction = "N"
        self.warehouse = warehouse  # Adicione a referência ao Warehouse
        
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
        
    def move_to(self, x, y):
        # Verifique se o movimento é válido antes de atualizar a posição do robô
        if self.is_valid_move(x, y):
            self.x = x
            self.y = y
        else:
            print(f"O movimento para ({x}, {y}) não é válido. O robô permanece na posição atual ({self.x}, {self.y}).")

    def is_valid_move(self, x, y):
        # Implemente a lógica para verificar se o movimento é válido
        # Isso pode incluir a verificação de colisões com obstáculos, limites do armazém, etc.
        # Retorne True se o movimento for válido e False caso contrário
        # Por exemplo, você pode verificar se a nova posição é válida no armazém
        return 0 <= x < self.warehouse.width and 0 <= y < self.warehouse.height and (x, y) not in self.warehouse.obstacles