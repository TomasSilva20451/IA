from collections import deque

class Warehouse:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.obstacles = []
        self.robots = []

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
        return abs(current[0] - goal[0]) + abs(current[1] - goal[1])

    def find_path_a_star(self, start, goal):
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

                if self.is_valid_location(new_x, new_y):
                    new_path = path + [(x, y)]
                    queue.append(((new_x, new_y), new_path))

        return None

    def find_path_greedy(self, start, goal):
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
            moves.sort(key=lambda move: self.heuristic((x + move[0], y + move[1]), goal))

            for dx, dy in moves:
                new_x, new_y = x + dx, y + dy

                if self.is_valid_location(new_x, new_y):
                    new_path = path + [(x, y)]
                    queue.append(((new_x, new_y), new_path))

        return None

    def find_path_bfs(self, start, goal):
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

                if self.is_valid_location(new_x, new_y):
                    new_path = path + [(x, y)]
                    queue.append(((new_x, new_y), new_path))

        return None
