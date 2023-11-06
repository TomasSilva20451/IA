from robot import Robot
from warehouse import Warehouse

# Crie um armazém de 7x7
warehouse = Warehouse(7, 7)

# Adicione obstáculos
warehouse.add_obstacle(6, 1)

# Crie um robô na posição (0, 0)
robot = Robot(0, 0, warehouse)

start = (0, 0)
goal = (6, 6)

# Encontre o caminho inicial usando o método find_path da classe Warehouse
path = warehouse.find_path(start, goal)

# Verifique se o caminho foi encontrado
if path:
    print("Caminho encontrado:", path)
    
    # Mova o robô ao longo do caminho
    for step in path:
        x, y = step
        
        # Verifique se a próxima posição contém um obstáculo
        if (x, y) in warehouse.obstacles:
            print(f"O robô colidiu com um obstáculo em ({x}, {y})")
        else:
            robot.move_to(x, y)
            print(f"Robô moveu se para ({x}, {y})")
else:
    print("Não foi possível encontrar um caminho.")
    
# Remova um obstáculo
#warehouse.remove_obstacle(6, 1)

# Reencontre o caminho após a remoção de obstáculos
new_path = warehouse.find_path((robot.x, robot.y), goal)


if new_path:
    print("Caminho encontrado após a remoção de obstáculos:", new_path)

    # Mova o robô ao longo do novo caminho
    for step in new_path:
        x, y = step
        robot.move_to(x, y)
        print(f"Robô moveu-se para ({x}, {y})")

    print(f"O robô chegou ao ponto B ({goal[0]}, {goal[1]})")
else:
    print("Não foi possível encontrar um caminho após a remoção de obstáculos.")
