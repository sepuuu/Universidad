import numpy as np
import random
import matplotlib.pyplot as plt

N = 25 # tamaño del tablero
M = 50 # número de genes
P = 0.05 # probabilidad de mutación

# Matriz del tablero
matriz = np.zeros((N, N))

# Inicializa genes con distribución uniforme de movimientos
genes = []
for _ in range(M):
    gen = list(range(8)) * (20 // 8)  # repite la lista de movimientos hasta alcanzar 20 elementos
    random.shuffle(gen)  # desordena aleatoriamente los movimientos
    genes.append((gen, (0, random.choice(range(N)))))

# Función para mover un gen de acuerdo a su ADN
def mover(gen, pos):
    movs = [(0, 1), (0, -1), (-1, 0), (1, 0), (-1, 1), (1, 1), (-1, -1), (1, -1)]
    x, y = pos
    for i in range(20):  # limite de pasos
        g = gen[i%8]    # repite los pasos en el gen después de 8
        dx, dy = movs[g]
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= N or ny < 0 or ny >= N: continue
        x, y = nx, ny
    return (x, y), i + 1  # devuelve la posición final y el número de pasos

# Cruce de genes con selección de los mejores
def cruce(genes):
    genes.sort(key=lambda x: x[1][0] + 1 / x[2], reverse=True)  # ordena por fitness
    sobrevivientes = genes[:M//2]  # toma la mitad superior
    nueva_gen = []
    fitness_total = sum(x[1][0] + 1 / x[2] for x in sobrevivientes)
    for _ in range(M):
        r = random.uniform(0, fitness_total)
        acum = 0
        for gen in sobrevivientes:
            if acum + gen[1][0] + 1 / gen[2] > r:
                padre1 = gen
                break
            acum += gen[1][0] + 1 / gen[2]
        r = random.uniform(0, fitness_total)
        acum = 0
        for gen in sobrevivientes:
            if acum + gen[1][0] + 1 / gen[2] > r:
                padre2 = gen
                break
            acum += gen[1][0] + 1 / gen[2]
        punto = random.choice(range(8))
        hijo = padre1[0][:punto] + padre2[0][punto:]
        # Añade mutación
        if random.random() < P:
            hijo[random.choice(range(8))] = random.choice(range(8))
        nueva_gen.append((hijo, (0, random.choice(range(N)))))
    return nueva_gen

# Visualización de los datos con matplotlib
def graficar(genes):
    tablero = np.zeros((N, N))
    for gen, pos, _ in genes:
        tablero[pos] = 1
    plt.imshow(tablero, cmap='gray')
    plt.show()

# Ciclo principal
mejor_gen = None
for generacion in range(20):
    print(f"Generación {generacion}")
    genes = [(gen, *mover(gen, pos)) for gen, pos in genes]
    graficar(genes)
    genes = cruce(genes)
    if mejor_gen is None or genes[0][1][0] > mejor_gen[1][0]:
        mejor_gen = genes[0]

print("Mejor gen:", mejor_gen)
