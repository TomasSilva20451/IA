from robot import Robot
from warehouse import Warehouse

# Crie um armazém de 7x7
warehouse = Warehouse(7, 7)

# Adicione obstáculos
warehouse.add_obstacle(6, 1)
warehouse.add_obstacle(5, 1)

# Crie um robô na posição (0, 0)
robot = Robot(0, 0, warehouse)

start = (0, 0)
goal = (6, 6)

# Inicie a tarefa do robô
robot.start_task()

# Encontre o caminho inicial usando o método find_path da classe Warehouse
path = warehouse.find_path(start, goal)

# Verifique se o caminho foi encontrado
if path:
    print("Caminho encontrado:", path)
    
    # Inicialize a direção atual
    current_direction = None
    
    # Mova o robô ao longo do caminho
    for i in range(len(path)):
        x, y = path[i]

        if (x, y) in warehouse.obstacles:
            print(f"O robô colidiu com um obstáculo em ({x}, {y})")
        else:
            robot.move_to(x, y)
            
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
                    if direction != current_direction:
                        print(f"Robô moveu-se para ({x}, {y}) na direção: {direction}")
                        current_direction = direction
else:
    print("Não foi possível encontrar um caminho.")

    

# Encerre a tarefa do robô
robot.end_task()

# Calcule o tempo que o robô levou para realizar a tarefa
task_duration = robot.task_duration()

if task_duration is not None:
    print(f"O robô levou {task_duration:.6f} segundos para realizar a tarefa.")
else:
    print("O tempo da tarefa não pôde ser calculado.")
    
    
# Remova um obstáculo
warehouse.remove_obstacle(6, 1)
warehouse.remove_obstacle(5, 1)

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
