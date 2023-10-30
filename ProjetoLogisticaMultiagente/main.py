from robot import Robot
from warehouse import Warehouse

# Crie um armazém de 5x5
warehouse = Warehouse(5, 5)

# Adicione obstáculos
warehouse.add_obstacle(1, 2)
warehouse.add_obstacle(2, 2)

# Crie um robô na posição (0, 0)
robot = Robot(0, 0)

# Movimente o robô
robot.move_forward()
robot.turn_right()
robot.move_forward()

# Verifique se a nova posição é válida
if warehouse.is_valid_location(robot.x, robot.y):
    print(f"Nova posição do robô: ({robot.x}, {robot.y})")
else:
    print("O robô colidiu com um obstáculo.")

# Remova um obstáculo
warehouse.remove_obstacle(1, 2)
