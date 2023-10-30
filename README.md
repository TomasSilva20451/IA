# IA -  Desenvolvimento de um Sistema de Logística Inteligente com Múltiplos Agentes

**Introdução:**
O objetivo deste trabalho é criar um ambiente multiagente que simula um sistema de logística em um armazém. O sistema envolve vários robôs autônomos colaborando para entregar produtos do ponto de origem ao destino no menor tempo possível. Os robôs devem lidar com desafios como distâncias, curvas, tempo de viragem, detecção de outros robôs e otimização de trajetos.

**Tecnologias e Linguagens de Programação:**
* Linguagem de programação: Python
* Bibliotecas: Numpy, Matplotlib (para visualização)
* Algoritmos de pesquisa: Pesquisa em Largura, A* (A-estrela), Busca Gulosa

**Implementação do Programa:**
O sistema será implementado em Python, uma linguagem de programação versátil e amplamente utilizada para desenvolvimento de IA. Para visualização e teste, podem ser utilizadas bibliotecas como Matplotlib e Numpy.

**Descrição do Ambiente:**
O ambiente do sistema é um armazém com diferentes locais, representados por coordenadas no plano. Os robôs devem mover-se do ponto de origem até o ponto de destino, evitando colisões com outros robôs e otimizando o tempo.

**Detalhes do Ambiente:**
* Distâncias: Cada unidade de distância equivale a uma unidade de tempo.
* Tempo de Viragem: 90 graus equivalem a 1,5 unidades de tempo; 180 graus equivalem a 3 unidades de tempo.
* Marcha à Ré: Envolve parar antes de inverter e consumir tempo.
* Sensores: Os robôs têm sensores e câmeras que lhes permitem detectar outros robôs.
* Direções: Os robôs podem mover-se nas direções Norte, Sul, Leste e Oeste.
* Custo: Cada estado tem um custo associado.

**Algoritmos de Busca:**
Para encontrar o caminho mais eficiente entre pontos A e B, você pode usar os seguintes algoritmos de busca:
* 		Pesquisa em Largura (BFS): Algoritmo não informado que explora todas as opções a partir de um estado inicial.
* 		*A (A-estrela)**: Algoritmo de busca informada que utiliza uma heurística para priorizar os estados mais promissores.
* 		Busca Gulosa: Outro algoritmo de busca informada que seleciona o próximo estado com base apenas na heurística.

**Heurística:**
A distância de Manhattan pode ser usada como heurística para estimar o custo de alcançar o objetivo a partir de um estado.
Desenvolvimento do Trabalho:
O trabalho pode ser dividido em fases, começando com um ambiente simples, um único agente e um único robô. Conforme o desenvolvimento avança, você pode aumentar a complexidade do ambiente, adicionando mais agentes, robôs e obstáculos, o que exigirá uma adaptação nos algoritmos e heurísticas.

**Resultados e Conclusão:**
O programa deve ser capaz de calcular o tempo que os robôs demoram para chegar de A a B, considerando diferentes cenários e obstáculos. Os resultados obtidos podem ser usados para avaliar a eficácia do sistema de logística multiagente em termos de tempo e eficiência.

**Conclusão:**
O desenvolvimento de um sistema de logística multiagente envolve a implementação de algoritmos de busca, adaptação a diferentes cenários e a otimização de trajetos. O uso de Python e algoritmos como Pesquisa em Largura, A* e Busca Gulosa facilitará o desenvolvimento desse sistema inteligente de logística.
