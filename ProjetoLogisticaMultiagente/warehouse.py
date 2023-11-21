# warehouse.py
from collections import deque

class Warehouse:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.obstacles = []  # Lista para armazenar as coordenadas dos obstáculos
        self.robots = []  # Lista para armazenar os robôs

    def add_robot(self, robot):
        self.robots.append(robot)

    def remove_robot(self, robot):
        if robot in self.robots:
            self.robots.remove(robot)

    def is_valid_location(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height and (x, y) not in self.obstacles

    def add_obstacle(self, x, y):
        if self.is_valid_location(x, y):
            self.obstacles.append((x, y))

    def remove_obstacle(self, x, y):
        if (x, y) in self.obstacles:
            self.obstacles.remove((x, y))

    def calculate_move_time(self, x, y, robot):
        movement_time = 1  # Tempo de deslocação padrão

        # Considere a rotação no tempo de deslocação
        if robot.turning_time > 0:
            movement_time += robot.turning_time

        return movement_time

    def find_path(self, start, goal):
        queue = deque([(start, [])])
        visited = set()

        while queue:
            (x, y), path = queue.popleft()

            if (x, y) == goal:
                return path + [(x, y)]

            if (x, y) in visited:
                continue

            visited.add((x, y))

            # Movimentos possíveis: para frente, para a direita, para trás, para a esquerda
            moves = [(0, -1), (1, 0), (0, 1), (-1, 0)]

            for dx, dy in moves:
                new_x, new_y = x + dx, y + dy

                if self.is_valid_location(new_x, new_y):
                    new_path = path + [(x, y)]
                    queue.append(((new_x, new_y), new_path))

        return None  # Caminho não encontrado