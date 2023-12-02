from collections import deque


class Warehouse:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.obstacles = []
        self.robots = []
        self.goals = []  # Adicione uma lista de objetivos
        
    def add_goal(self, goal):
        """
        Adiciona um objetivo ao armazém.

        :param goal: A posição do objetivo.
        """
        self.goals.append(goal)

    def add_robot(self, robot):
        self.robots.append(robot)

    def is_valid_location(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height and (x, y) not in self.obstacles

    def add_obstacle(self, x, y):
        if self.is_valid_location(x, y):
            self.obstacles.append((x, y))

    def remove_obstacle(self, x, y):
        if (x, y) in self.obstacles:
            self.obstacles.remove((x, y))

    def heuristic(self, current, goal):
        return ((current[0] - goal[0]) ** 2 + (current[1] - goal[1]) ** 2) ** 0.5

    def find_path_a_star(self, start, goal):
        """
        Encontra o caminho usando o algoritmo A*.

        :param start: A posição inicial.
        :param goal: A posição final.
        :return: Lista de coordenadas representando o caminho ou None se nenhum caminho for encontrado.
        """
        queue = deque([(start, [])])
        visited = set()

        while queue:
            current, path = queue.popleft()
            x, y = current  # Descompacte a posição atual

            if (x, y) == goal:
                return path + [(x, y)]

            if current in visited:
                continue

            visited.add(current)

            moves = [(0, -1), (1, 0), (0, 1), (-1, 0)]

            for dx, dy in moves:
                new_x, new_y = x + dx, y + dy

                if self.is_valid_location(new_x, new_y):
                    new_path = path + [(x, y)]
                    queue.append(((new_x, new_y), new_path))

        return None

    def find_path_greedy(self, start, goal):
        """
        Encontra o caminho usando o algoritmo Greedy.

        :param start: A posição inicial.
        :param goal: A posição final.
        :return: Lista de coordenadas representando o caminho ou None se nenhum caminho for encontrado.
        """
        queue = deque([(start, [])])
        visited = set()

        while queue:
            current, path = queue.popleft()
            x, y = current  # Descompacte a posição atual

            if (x, y) == goal:
                return path + [(x, y)]

            if current in visited:
                continue

            visited.add(current)

            moves = [(0, -1), (1, 0), (0, 1), (-1, 0)]

            for dx, dy in moves:
                new_x, new_y = x + dx, y + dy

                if self.is_valid_location(new_x, new_y):
                    new_path = path + [(x, y)]
                    queue.append(((new_x, new_y), new_path))

        return None


    def find_path_bfs(self, start, goal):
        """
        Encontra o caminho usando o algoritmo Breadth-First Search (BFS).

        :param start: A posição inicial.
        :param goal: A posição final.
        :return: Lista de coordenadas representando o caminho ou None se nenhum caminho for encontrado.
        """
        queue = deque([(start, [])])
        visited = set()

        while queue:
            (x, y), path = queue.popleft()

            if (x, y) == goal:
                return path + [(x, y)]

            if (x, y) in visited:
                continue

            visited.add((x, y))

            moves = [(0, -1), (1, 0), (0, 1), (-1, 0)]

            for dx, dy in moves:
                new_x, new_y = x + dx, y + dy

                if self.is_valid_location(new_x, new_y) and (new_x, new_y) not in visited:
                    queue.append(((new_x, new_y), path + [(x, y)]))

        return None
