class Robot:
    def __init__(self, x, y, warehouse):
        self.x = x
        self.y = y
        self.direction = "N"
        self.warehouse = warehouse  # Adicione a referência ao Warehouse
        self.turning_time = 0  # Tempo de viragem
        
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
            self.direction = "E"
            self.turning_time = 1.5
        elif self.direction == "E":
            self.direction = "S"
            self.turning_time = 1.5
        elif self.direction == "S":
            self.direction = "W"
            self.turning_time = 1.5
        elif self.direction == "W":
            self.direction = "N"
            self.turning_time = 1.5
                
    def turn_left(self):
        if self.direction == "N":
            self.direction = "W"
            self.turning_time = 1.5
        elif self.direction == "W":
            self.direction = "S"
            self.turning_time = 1.5
        elif self.direction == "S":
            self.direction = "E"
            self.turning_time = 1.5
        elif self.direction == "E":
            self.direction = "N"
            self.turning_time = 1.5

        
    def move_to(self, x, y):
        # Registre a posição atual antes de se mover
        current_x, current_y = self.x, self.y

        # Verifique se o movimento é válido antes de atualizar a posição do robô
        if self.is_valid_move(x, y):
            self.x = x
            self.y = y

            # Calcule a direção em que o robô se moveu
            if x > current_x:
                movement_direction = "direita"
            elif x < current_x:
                movement_direction = "esquerda"
            elif y > current_y:
                movement_direction = "frente"
            elif y < current_y:
                movement_direction = "trás"
            else:
                movement_direction = "posição atual"

            print(f"Robô moveu-se para ({x}, {y}) na direção: {movement_direction}")
        else:
            print(f"O movimento para ({x}, {y}) não é válido. O robô permanece na posição atual ({self.x}, {self.y}).")

    def is_valid_move(self, x, y):
        # Implemente a lógica para verificar se o movimento é válido, considerando obstáculos, tempo de viragem e colisões com outros robôs.
        
        # Primeiro, verifique o tempo de viragem
        if self.turning_time > 0:
            return False  # O robô ainda está virando

        # Verifique se a nova posição está dentro dos limites do armazém
        if not (0 <= x < self.warehouse.width and 0 <= y < self.warehouse.height):
            return False  # Fora dos limites do armazém

        # Verifique se a nova posição não colide com obstáculos
        if (x, y) in self.warehouse.obstacles:
            return False  # Colisão com obstáculo

        # Verifique se a nova posição não colide com outros robôs
        for other_robot in self.warehouse.robots:
            if other_robot != self and (x, y) == (other_robot.x, other_robot.y):
                return False  # Colisão com outro robô

        # Verifique se o movimento é adjacente à posição atual
        current_x, current_y = self.x, self.y
        if abs(x - current_x) + abs(y - current_y) != 1:
            return False  # Não é um movimento adjacente

        return True  # Movimento válido

