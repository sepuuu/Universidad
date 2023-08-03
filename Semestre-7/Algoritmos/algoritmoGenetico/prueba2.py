import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib.cm import ScalarMappable

N = 50  # tamaño del tablero
M = 100  # número de genes
##el numero de genes tiene que ser el doble de la dimension del tablero (hay que modificarlo)

# Matriz del tablero
matriz = np.zeros((N, N))

# Inicializa genes en posiciones aleatorias sin duplicados
genes = []
posiciones_ocupadas = set()
while len(genes) < M:
    gen = [random.uniform(0, 1) for _ in range(8)]
    suma = sum(gen)
    gen = [g / suma for g in gen]
    pos = (0, random.choice(range(N)))
    if pos not in posiciones_ocupadas:
        genes.append((gen, pos))
        posiciones_ocupadas.add(pos)

# Matriz de movimientos
movs = [(0, 1), (0, -1), (-1, 0), (1, 0), (-1, 1), (1, 1), (-1, -1), (1, -1)]

# Función para mover un gen de acuerdo a su ADN
def mover(gen, pos):
    x, y = pos
    for g in range(17):  # limite de pasos reducido
        idx = random.choices(range(8), weights=gen)[0]
        dx, dy = movs[idx]
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        x, y = nx, ny
        if x == N-1:  # zona objetivo ahora es la última columna
            break
    return (x, y)

# Función para evaluar la calidad de los genes
def evaluar_calidad(genes):
    distancias = []
    for gen, pos in genes:
        x, y = pos
        if x == N-1:  # zona objetivo ahora es la última columna
            distancia = 0
        else:
            distancia = N-1 - x  # distancia a la última columna
        distancias.append(distancia)
    return distancias

# Cruce de genes con selección de los mejores
def cruce(genes, distancias):
    orden = np.argsort(distancias)
    mejores_genes = [genes[i] for i in orden[:M//2]]
    nueva_gen = []
    for _ in range(M):
        gen1, gen2 = random.choices(mejores_genes, k=2)
        punto = random.choice(range(8))
        hijo = gen1[0][:punto] + gen2[0][punto:]
        suma = sum(hijo)
        hijo = [g / suma for g in hijo]
        pos_hijo = gen1[1]
        nueva_gen.append((hijo, pos_hijo))
    return nueva_gen

# Visualización de los datos con matplotlib
def graficar(genes, goal, generation):
    plt.clf()
    cmap = ScalarMappable(cmap='hsv').cmap
    colors = cmap(np.linspace(0, 1, generation + 1))
    for i, person in enumerate(genes):
        plt.plot(person[1][0], person[1][1], 'o', color=colors[i % generation])
    plt.plot([N-1, N-1], [0, N-1], 'b', linewidth=2)  # zona objetivo ahora es la última columna
    plt.xlim(0, N-1)
    plt.ylim(0, N-1)
    plt.title(f'Generation: {generation}')
    plt.pause(0.5)

# Ciclo principal
best_distance = float('inf')
best_gen = None
best_generation = 0

for generation in range(1, 21):
    print(f"Generación {generation}")
    genes = [(gen, mover(gen, pos)) for gen, pos in genes]
    distancias = evaluar_calidad(genes)
    graficar(genes, N-1, generation)
    genes = cruce(genes, distancias)

    distancias_finales = evaluar_calidad(genes)
    mejor_gen_idx = np.argmin(distancias_finales)
    mejor_gen = genes[mejor_gen_idx][0]
    mejor_distancia = distancias_finales[mejor_gen_idx]
    
    if mejor_distancia < best_distance:
        best_distance = mejor_distancia
        best_gen = mejor_gen
        best_generation = generation

print(f"El mejor gen encontrado es: {best_gen}")
print(f"Generación en la que se encontró el mejor gen: {best_generation}")
plt.legend(['Generation 1', 'Generation 2', 'Generation 3', 'Generation 4', 'Generation 5',
            'Generation 6', 'Generation 7', 'Generation 8', 'Generation 9', 'Generation 10',
            'Generation 11', 'Generation 12', 'Generation 13', 'Generation 14', 'Generation 15',
            'Generation 16', 'Generation 17', 'Generation 18', 'Generation 19', 'Generation 20'])
plt.show()
