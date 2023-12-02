import random
import time
from robot import Robot
from warehouse import Warehouse


NUM_SIMULATIONS = 10  # Número de simulações para média
WAREHOUSE_WIDTH = 7
WAREHOUSE_HEIGHT = 7
NUM_ROBOTS = 2

def simulate_warehouse_scenario(warehouse, robots, algorithm_name):
    total_durations = []

    for _ in range(NUM_SIMULATIONS):
        for robot in robots:
            start_time = time.time()

            # Gere tarefas aleatórias para o robô
            tasks = generate_random_tasks(warehouse)
            for task in tasks:
                goal_x, goal_y = task
                robot.move_to_with_algorithm(goal_x, goal_y, algorithm_name)

            end_time = time.time()
            task_duration = end_time - start_time
            total_durations.append(task_duration)

            print(f"Tempo total para o robô {robot}: {task_duration:.6f} segundos")

    avg_duration = sum(total_durations) / len(total_durations)
    print(f"\nMédia de tempo para {NUM_SIMULATIONS} simulações: {avg_duration:.6f} segundos")




def generate_random_tasks(warehouse):
    # Gere tarefas aleatórias, por exemplo, recolher objetos e entregá-los
    tasks = []
    num_tasks = random.randint(1, 5)  # Número aleatório de tarefas por robô

    for _ in range(num_tasks):
        goal_x = random.randint(0, warehouse.width - 1)
        goal_y = random.randint(0, warehouse.height - 1)
        tasks.append((goal_x, goal_y))

    return tasks

# Exemplo de uso da função de simulação
warehouse = Warehouse(WAREHOUSE_WIDTH, WAREHOUSE_HEIGHT)
robots = [Robot(random.randint(0, WAREHOUSE_WIDTH - 1), random.randint(0, WAREHOUSE_HEIGHT - 1), warehouse) for _ in range(NUM_ROBOTS)]

for robot in robots:
    warehouse.add_robot(robot)

# Execute a simulação
simulate_warehouse_scenario(warehouse, robots, "a_star")


