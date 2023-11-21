import time

class Robot:
    def __init__(self, x, y, warehouse):
        self.x = x
        self.y = y
        self.direction = "N"
        self.warehouse = warehouse  # Adicione a referência ao Warehouse
        self.turning_time = 0  # Tempo de viragem
        self.start_time = None  # Registre o tempo de início da tarefa
        self.end_time = None  # Registre o tempo de término da tarefa

    def execute_turn(self, direction):
        if self.direction == direction:
            return 0  # Não há necessidade de virar
        else:
            self.direction = direction
            self.turning_time = 1.5  # Tempo para virar
            return self.turning_time

    def move_forward(self):
        if self.direction == "N":
            self.y -= 1
        elif self.direction == "S":
            self.y += 1
        elif self.direction == "E":
            self.x += 1
        elif self.direction == "W":
            self.x -= 1

        move_time = self.warehouse.calculate_move_time(self.x, self.y, self)
        print(f"Robô moveu-se para frente. Tempo de deslocação: {move_time} segundos")

    def turn_right(self):
        turn_time = self.execute_turn("E")
        print(f"Robô virou para a direita. Tempo de viragem: {turn_time} segundos")

    def turn_left(self):
        turn_time = self.execute_turn("W")
        print(f"Robô virou para a esquerda. Tempo de viragem: {turn_time} segundos")

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

    def start_task(self):
        self.start_time = time.time()

    def end_task(self):
        self.end_time = time.time()

    def task_duration(self):
        if self.start_time is not None and self.end_time is not None:
            return self.end_time - self.start_time
        else:
            return None