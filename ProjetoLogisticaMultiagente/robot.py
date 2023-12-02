import time


class Robot:
    def __init__(self, x, y, warehouse):
        # Inicialização das coordenadas x e y do robô
        self.x = x
        self.y = y
        # Inicialização da direção inicial do robô para "N" (Norte)
        self.direction = "N"
        # Associação do robô ao armazém em que está localizado
        self.warehouse = warehouse
        # Inicialização do tempo de viragem
        self.turning_time = 0
        # Inicialização dos tempos de início e fim da execução do robô
        self.start_time = None
        self.end_time = None
        # Indicação se o robô está carregando um objeto
        self.is_carrying_object = False
        # Custo de movimento - define o custo para mover uma unidade na grade do armazém
        self.move_cost = 1  # Custo de movimento
        # Custo de viragem - define o custo adicional associado à mudança de direção
        self.turn_cost = 1.5  # Custo de viragem
        # Tempo total decorrido desde o início da execução do robô
        self.total_time_elapsed = 0

    def __str__(self):
        # Retorna uma representação de string das coordenadas do robô
        return f"({self.x}, {self.y})"

    def move_forward(self, print_movement=True):
        # Verifica se o robô está atualmente em processo de viragem
        if self.turning_time > 0:
            # Se estiver virando, exibe uma mensagem indicando o tempo restante de viragem
            if print_movement:
                print(
                    f"O robô está virando. Tempo restante: {self.turning_time} segundos.")
            self.turning_time -= 1  # Reduz o tempo de viragem
            return

        # Move o robô para frente com base na sua direção atual
        if self.direction == "N":
            self.y -= 1
        elif self.direction == "S":
            self.y += 1
        elif self.direction == "E":
            self.x += 1
        elif self.direction == "W":
            self.x -= 1
        # Define o tempo de viragem após o movimento para frente
        self.turning_time = self.turn_cost  # Tempo de viragem

        # Exibe a mensagem de movimento se print_movement for True
        if print_movement:
            self.print_movement("frente")

    def turn_right(self, print_movement=True):
        # Atualiza a direção do robô para a direita (sentido horário)
        self.direction = {"N": "E", "E": "S",
                          "S": "W", "W": "N"}[self.direction]
        self.turning_time = self.turn_cost  # Define o tempo de viragem

        # Ajusta a direção e o tempo de viragem específicos para a direção final após virar à direita
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

        # Exibe a mensagem de movimento se print_movement for True
        if print_movement:
            self.print_movement("direita")

    def turn_left(self, print_movement=True):
        # Atualiza a direção do robô para a esquerda (sentido anti-horário)
        self.direction = {"N": "W", "W": "S",
                          "S": "E", "E": "N"}[self.direction]
        self.turning_time = self.turn_cost  # Define o tempo de viragem

        # Ajusta a direção e o tempo de viragem específicos para a direção final após virar à esquerda
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

        # Exibe a mensagem de movimento se print_movement for True
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
        # Verifica se o robô está atualmente em processo de viragem
        if self.turning_time > 0:
            print(
                f"O robô está virando. Tempo restante: {self.turning_time} segundos.")
            return

        # Verifica se o robô já está na posição de destino
        if (x, y) == (self.x, self.y):
            print(f"O robô já está na posição ({x}, {y}).")
            return

        # Verifica se o movimento para a nova posição é válido
        if not self.is_valid_move(x, y):
            print(
                f"O movimento para ({x}, {y}) não é válido. O robô permanece na posição atual ({self.x}, {self.y}).")
            return

        # Executa o movimento para a nova posição válida
        self.move_to_valid(x, y)

    def is_valid_move(self, x, y):

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
        # Salva as coordenadas atuais antes de atualizar a posição do robô
        current_x, current_y = self.x, self.y

        # Atualiza a posição do robô para as novas coordenadas
        self.x = x
        self.y = y

        # Determina a direção do movimento com base nas coordenadas antigas e novas
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

        # Calcula o tempo total considerando o tempo de viragem e a marcha trás, se aplicável
        total_time = self.turning_time + self.move_cost
        if movement_direction == "trás":
            total_time += self.move_cost * 2  # Adicione o tempo de marcha trás

        # Atualiza o tempo total decorrido
        self.total_time_elapsed += total_time  # Armazene o tempo total

        # Exibe uma mensagem indicando o movimento e o tempo total
        print(
            f"Robô moveu-se para ({x}, {y}) na direção: {movement_direction}. Tempo total: {total_time} unidade(s) de tempo.")
        # Retorna o tempo total, que pode ser útil para rastrear ou registar
        return total_time

    def move_to_with_algorithm(self, x, y, algorithm_name):
        """
        Move o robô para as coordenadas especificadas usando um algoritmo de busca.

        Parâmetros:
            x (int): Coordenada x do destino.
            y (int): Coordenada y do destino.
            algorithm_name (str): Nome do algoritmo a ser utilizado (a_star, greedy, bfs).

        Retorna:
            None

        Comentários:
            - Verifica se o algoritmo fornecido é reconhecido (a_star, greedy, bfs).
            - Obtém o caminho usando o algoritmo escolhido.
            - Move o robô para cada posição no caminho, verificando colisões com obstáculos.
            - Exibe mensagens de movimento e colisão.
            - Caso o caminho não seja encontrado, exibe uma mensagem indicando a falha.
        """
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
        """
        Inicia a contagem do tempo de uma tarefa.

        Parâmetros:
            None

        Retorna:
            None

        Comentários:
            - Registra o tempo de início da tarefa.
        """
        self.start_time = time.time()

    def end_task(self):
        """
        Encerra a contagem do tempo de uma tarefa.

        Parâmetros:
            None

        Retorna:
            None

        Comentários:
            - Registra o tempo de término da tarefa.
        """
        self.end_time = time.time()

    def task_duration(self):
        """
        Calcula a duração total da tarefa.

        Parâmetros:
            None

        Retorna:
            float: Duração total da tarefa em segundos, ou None se o tempo de início ou término não estiver definido.

        Comentários:
            - Calcula a diferença entre o tempo de término e o tempo de início para obter a duração da tarefa.
        """
        if self.start_time is not None and self.end_time is not None:
            return self.end_time - self.start_time
        else:
            return None

    def pick_up_object(self):
        """
        Simula o robô pegando um objeto.

        Parâmetros:
            None

        Retorna:
            None

        Comentários:
            - Verifica se o robô já está carregando um objeto.
            - Atualiza o estado do robô para indicar que está carregando um objeto.
        """
        if self.is_carrying_object:
            print("O robô já está carregando um objeto.")
        else:
            self.is_carrying_object = True
            print("O robô pegou um objeto.")

    def deliver_object(self, x, y):
        """
        Simula o robô entregando um objeto em uma posição específica.

        Parâmetros:
            x (int): Coordenada x da posição de entrega.
            y (int): Coordenada y da posição de entrega.

        Retorna:
            None

        Comentários:
            - Verifica se o robô está carregando um objeto.
            - Se a posição de entrega for a mesma que a posição atual do robô, o objeto é entregue na posição atual.
            - Caso contrário, o robô se move para a posição de entrega antes de entregar o objeto.
            - Atualiza o estado do robô para indicar que não está mais carregando um objeto.
        """

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
