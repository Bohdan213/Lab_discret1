from generate_graph import gnp_random_connected_graph
from queue import PriorityQueue
import timeit
import math

def prim(number, graphs):
    # a = input()
    # number, posibility = int(a.split()[0]), float(a.split()[1])
    # graphs = gnp_random_connected_graph(number, posibility)
    Graph = []
    for i in range(number):
        Graph.append([])
    for i in graphs:
        Graph[i[0]].append((i[1], i[2]))
        Graph[i[1]].append((i[0], i[2]))
    U = [False] * number
    dist = [math.inf] * number
    dist[0] = 0
    Q = PriorityQueue()
    Q.put((0, 0))
    start = timeit.default_timer()
    S = 0
    while not Q.empty():
        temp = Q.get()
        edge_len = temp[0]
        edge = temp[1]
        if U[edge]:
            continue
        S += edge_len
        U[edge] = True
        for i in range(len(Graph[edge])):
            cost = Graph[edge][i][1]
            v = Graph[edge][i][0]
            if U[v]:
                Q.put((cost, v))
    stop = timeit.default_timer()
    tm = stop - start
    return tm

if __name__ == '__main__':
    print(prim())