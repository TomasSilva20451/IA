import time
import matplotlib.pyplot as plt
import numpy as np
from robot import Robot
from warehouse import Warehouse

# Função para criar um cenário
def create_scenario(warehouse, robot, goal):
    # Adicionar obstáculos
    warehouse.add_obstacle(2, 2)
    warehouse.add_obstacle(3, 3)
    warehouse.add_obstacle(4, 4)

    # Adicionar o robô ao armazém
    warehouse.add_robot(robot)

    # Adicionar o objetivo ao armazém
    warehouse.add_goal(goal)

# Função para medir o tempo de execução e o comprimento do caminho
def measure_performance(algorithm, warehouse, start, goal):
    start_time = time.time()
    path = algorithm(start, goal)
    end_time = time.time()

    return end_time - start_time, len(path) - 1 if path else None

# Função para executar os algoritmos e gerar estatísticas
def run_algorithms(warehouse, start, goal):
    algorithms = [
        ("A*", warehouse.find_path_a_star),
        ("Greedy", warehouse.find_path_greedy),
        ("BFS", warehouse.find_path_bfs),
    ]

    results = {}

    for name, algorithm in algorithms:
        execution_time, path_length = measure_performance(algorithm, warehouse, start, goal)
        results[name] = {"execution_time": execution_time, "path_length": path_length}

    return results

# Função para plotar gráficos
def plot_results(results):
    labels = list(results.keys())
    execution_times = [result["execution_time"] for result in results.values()]
    path_lengths = [result["path_length"] for result in results.values()]

    # Gráfico de barras para o tempo de execução
    plt.figure(figsize=(10, 5))
    plt.bar(labels, execution_times, color=['blue', 'orange', 'green'])
    plt.xlabel('Algoritmo')
    plt.ylabel('Tempo de Execução (s)')
    plt.title('Desempenho dos Algoritmos')
    plt.show()

    # Gráfico de barras para o comprimento do caminho
    plt.figure(figsize=(10, 5))
    plt.bar(labels, path_lengths, color=['blue', 'orange', 'green'])
    plt.xlabel('Algoritmo')
    plt.ylabel('Comprimento do Caminho')
    plt.title('Comprimento do Caminho Encontrado pelos Algoritmos')
    plt.show()

# Configuração do cenário
warehouse = Warehouse(7, 7)  # Ajustar o tamanho do armazém para acomodar o novo cenário
robot = Robot(0, 0, warehouse)
start = (0, 0)
goal = (6, 6)

create_scenario(warehouse, robot, goal)
results = run_algorithms(warehouse, start, goal)
plot_results(results)