import math
from PriorityQueue import PriorityQueue
from PriorityQueue import Vertex


def square_matrix(g):
    return len(g) == len(g[0])


def valid_graph(g):
    size = len(g)
    for i in range(0, size):
        for j in range(0, size):
            if (g[i][i] != 0):
                print(f"El nodo de la fila {i} esta conectado con si mismo")
                return False

            if (g[i][j] != g[j][i]):
                # NOTE: podría optimizarse, aqui solo se valida la simetria diagonal
                print(f"El Nodo {i},{j} no es simetrico con {j},{i}")
                return False

    return True


# prueba 3
# nodo_fuente = 1

# names = [
#     'A','B'
# ]

# graph = [
#     #A  B 
#     [0, 1],  # A - 0
#     [1, 0],  # B - 1
# ]

# prueba 1
# nodo_fuente = 1

# names = [
#     'A','B','C','D','F','G','H','J'
# ]

# graph = [
#     #A  B  C  D  F  G  H  J
#     [0, 4, 2, 0, 0, 7, 0, 0],  # A - 0
#     [4, 0, 0, 2, 0, 0, 0, 0],  # B - 1
#     [2, 0, 0, 0, 8, 3, 0, 0],  # C - 2
#     [0, 2, 0, 0, 0, 5, 6, 0],  # D - 3
#     [0, 0, 8, 0, 0, 0, 0, 3],  # F - 4
#     [7, 0, 3, 5, 0, 0, 0, 4],  # G - 5
#     [0, 0, 0, 6, 0, 0, 0, 2],  # H - 6
#     [0, 0, 0, 0, 3, 4, 2, 0],  # J - 7
# ]

# prueba 2
nodo_fuente = 0

names = ['A', 'B', 'C', 'D', 'E']

graph = [
    #A  B  C  D  E
    [0, 6, 0, 1, 0],  # A
    [6, 0, 5, 2, 2],  # B
    [0, 5, 0, 0, 5],  # C
    [1, 2, 0, 0, 1],  # D
    [0, 2, 5, 1, 0],  # E
]

size = len(graph)

if (not square_matrix(graph)):
    print("La matriz ingresada no es cuadrada.")
    exit()

if (not valid_graph(graph)):
    print("El grafo ingresado no es valido.")
    exit()

dist = []
for i in range(size):
    dist.append(Vertex(nodo=i, distancia=99999999))

pq = PriorityQueue()
pq.enqueue(Vertex(nodo=nodo_fuente, distancia=0)) # primer termino

while not pq.is_empty():        
    u = pq.dequeue()

    for i, v in enumerate(graph[u.nodo]): # comparar sus adyacencias 
        foo = (u.distancia + v)           # nodo + adyasencia 

        if dist[i].distancia > foo and v != 0:
            dist[i].distancia = foo
            pq.enqueue(Vertex(nodo=i,padre=u.nodo,distancia=foo))

print(" === RES === ")
print("Nodo | Camino con el peso mas corto")
for i, v in enumerate(dist):
    if i != nodo_fuente:
        print(names[v.nodo], "|", v.distancia)
