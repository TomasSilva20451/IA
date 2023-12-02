import time


class Robot:
    def __init__(self, x, y, warehouse):
        self.x = x
        self.y = y
        self.direction = "N"
        self.warehouse = warehouse
        self.turning_time = 0
        self.start_time = None
        self.end_time = None
        self.is_carrying_object = False
        self.move_cost = 1  # Custo de movimento
        self.turn_cost = 1.5  # Custo de viragem
        self.total_time_elapsed = 0  # Adicione esta linha

    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def move_forward(self, print_movement=True):
        if self.turning_time > 0:
            if print_movement:
                print(
                    f"O robô está virando. Tempo restante: {self.turning_time} segundos.")
            self.turning_time -= 1  # Reduz o tempo de viragem
            return

        if self.direction == "N":
            self.y -= 1
        elif self.direction == "S":
            self.y += 1
        elif self.direction == "E":
            self.x += 1
        elif self.direction == "W":
            self.x -= 1
        self.turning_time = self.turn_cost  # Tempo de viragem
        if print_movement:
            self.print_movement("frente")

    def turn_right(self, print_movement=True):
        self.direction = {"N": "E", "E": "S",
                          "S": "W", "W": "N"}[self.direction]
        self.turning_time = self.turn_cost

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

        if print_movement:
            self.print_movement("direita")

    def turn_left(self, print_movement=True):
        self.direction = {"N": "W", "W": "S",
                          "S": "E", "E": "N"}[self.direction]
        self.turning_time = self.turn_cost

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

        if print_movement:
            self.print_movement("esquerda")
            
    def print_movement(self, movement_direction):
        # Método para imprimir mensagens de movimento
        total_time = self.turning_time + self.move_cost
        if movement_direction == "trás":
            total_time += self.move_cost * 2  # Adicione o tempo de marcha tras

        print(
            f"Robô moveu-se para ({self.x}, {self.y}) na direção: {movement_direction}. Tempo total: {total_time} unidade(s) de tempo.")

    def move_to(self, x, y):
        if self.turning_time > 0:
            print(
                f"O robô está virando. Tempo restante: {self.turning_time} segundos.")
            return

        if (x, y) == (self.x, self.y):
            print(f"O robô já está na posição ({x}, {y}).")
            return

        if not self.is_valid_move(x, y):
            print(
                f"O movimento para ({x}, {y}) não é válido. O robô permanece na posição atual ({self.x}, {self.y}).")
            return

        self.move_to_valid(x, y)

    def is_valid_move(self, x, y):
        # Implemente a lógica para verificar se o movimento é válido, considerando obstáculos, tempo de viragem e colisões com outros robôs.

        # Primeiro, verifique o tempo de viragem
        if self.turning_time > 0:
            return False  # O robô ainda está virando

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

        # Verifique se a nova posição está dentro dos limites do armazém após verificar obstáculos e outros robôs
        if not (0 <= x < self.warehouse.width and 0 <= y < self.warehouse.height):
            return False  # Fora dos limites do armazém

        return True  # Movimento válido

    def move_to_valid(self, x, y):
        # Movimento é válido, atualize a posição do robô
        current_x, current_y = self.x, self.y

        self.x = x
        self.y = y

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

        # Atualize o tempo total de movimento considerando o tempo de viragem e a marcha atrás
        total_time = self.turning_time + self.move_cost
        if movement_direction == "trás":
            total_time += self.move_cost * 2  # Adicione o tempo de marcha à ré

        self.total_time_elapsed += total_time  # Armazene o tempo total

        print(
            f"Robô moveu-se para ({x}, {y}) na direção: {movement_direction}. Tempo total: {total_time} unidade(s) de tempo.")
        return total_time  # Retorne o tempo total

    def move_to_with_algorithm(self, x, y, algorithm_name):
        if algorithm_name == "a_star":
            path = self.warehouse.find_path_a_star((self.x, self.y), (x, y))
        elif algorithm_name == "greedy":
            path = self.warehouse.find_path_greedy((self.x, self.y), (x, y))
        elif algorithm_name == "bfs":
            path = self.warehouse.find_path_bfs((self.x, self.y), (x, y))
        else:
            print("Algoritmo não reconhecido")
            return

        if path:
            for i in range(len(path)):
                x, y = path[i]

                if (x, y) in self.warehouse.obstacles:
                    print(f"O robô colidiu com um obstáculo em ({x}, {y})")
                else:
                    self.move_to_valid(x, y)

                    if i != len(path) - 1:
                        x_next, y_next = path[i + 1]
                        dx = x_next - x
                        dy = y_next - y

                        direction = None

                        if dx == 1:
                            direction = "direita"
                        elif dx == -1:
                            direction = "esquerda"
                        elif dy == 1:
                            direction = "frente"
                        elif dy == -1:
                            direction = "trás"

                        if direction:
                            print(
                                f"Robô moveu-se para ({x}, {y}) na direção: {direction}")
        else:
            print("Não foi possível encontrar um caminho.")

    def start_task(self):
        self.start_time = time.time()

    def end_task(self):
        self.end_time = time.time()

    def task_duration(self):
        if self.start_time is not None and self.end_time is not None:
            return self.end_time - self.start_time
        else:
            return None

    def pick_up_object(self):
        if self.is_carrying_object:
            print("O robô já está carregando um objeto.")
        else:
            self.is_carrying_object = True
            print("O robô pegou um objeto.")

    def deliver_object(self, x, y):
        if not self.is_carrying_object:
            print("O robô não está carregando um objeto para entregar.")
            return

        if (x, y) == (self.x, self.y):
            self.is_carrying_object = False
            print("O robô entregou o objeto na posição atual.")
        else:
            print(
                "O robô não pode entregar o objeto nesta posição. Movendo-se para a posição desejada.")
            self.move_to(x, y)
            self.is_carrying_object = False
            print("O robô entregou o objeto na posição desejada.")
