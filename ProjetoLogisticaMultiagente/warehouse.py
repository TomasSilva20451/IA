# No arquivo warehouse.py
class Warehouse:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.obstacles = []  # Lista para armazenar as coordenadas dos obstáculos

    def is_valid_location(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height and (x, y) not in self.obstacles

    def add_obstacle(self, x, y):
        if self.is_valid_location(x, y):
            self.obstacles.append((x, y))

    def remove_obstacle(self, x, y):
        if (x, y) in self.obstacles:
            self.obstacles.remove((x, y))
