from robot import Robot
from warehouse import Warehouse

# Cria um armazém com dimensões 7x7
warehouse = Warehouse(7, 7)
warehouse.add_obstacle(6, 1)  # Adiciona obstáculos ao armazém
warehouse.add_obstacle(5, 1)

# Cria um robô na posição inicial (0, 0) no armazém
robot = Robot(0, 0, warehouse)

start = (0, 0)
goal = (6, 6)

# Inicia a contagem de tempo para a tarefa
robot.start_task()

algorithm_choice = "a_star"
# Encontra o caminho usando o algoritmo A* do ponto A ao ponto B
path = warehouse.find_path_a_star(start, goal)

if path:
    print("Caminho encontrado:", path)

    # total_time_to_goal = 0  # Inicialize o tempo total ao chegar ao ponto B

    current_direction = None

    # Itera sobre cada passo do caminho
    for i in range(len(path)):
        x, y = path[i]

        if (x, y) in warehouse.obstacles:
            print(f"O robô colidiu com um obstáculo em ({x}, {y})")
        else:
            # Move o robô para a próxima posição no caminho usando o algoritmo escolhido
            robot.move_to_with_algorithm(x, y, algorithm_choice)

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
                        print(
                            f"Robô moveu-se para ({x}, {y}) na direção: {direction}")
                        current_direction = direction

    # Imprime informações sobre o caminho encontrado
    print("Comprimento do caminho:", len(path))
    print(f"Tempo total: {robot.total_time_elapsed} unidade(s)")
else:
    print("Não foi possível encontrar um caminho.")

# Finaliza a tarefa e calcula a duração total
robot.end_task()
task_duration = robot.task_duration()

if task_duration is not None:
    print(f"O robô levou {task_duration:.6f} segundos para realizar a tarefa.")
else:
    print("O tempo da tarefa não pôde ser calculado.")

# Remove obstáculos do armazém
warehouse.remove_obstacle(6, 1)
warehouse.remove_obstacle(5, 1)

# Encontra um novo caminho após a remoção de obstáculos
new_path = warehouse.find_path_a_star((robot.x, robot.y), goal)

if new_path:
    print("Caminho encontrado após a remoção de obstáculos:", new_path)

    # Move o robô ao longo do novo caminho
    for step in new_path:
        x, y = step
        robot.move_to(x, y)
        print(f"Robô moveu-se para ({x}, {y})")

    print(f"O robô chegou ao ponto B ({goal[0]}, {goal[1]})")
else:
    print("Não foi possível encontrar um caminho após a remoção de obstáculos.")
