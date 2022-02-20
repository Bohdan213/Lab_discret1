from generate_graph import gnp_random_connected_graph
import timeit

"""

Крок 1. Упорядкувати множину ребер у порядку зростання ваг: e1, e2, e3, …, em.

Крок 2. Утворити розбиття множини вершин на одноелементні підмножини: {{v1}, {v2}, …, {vn}}.

Крок 3. Вибирати таке чергове ребро з упорядкованої послідовності ребер, що його кінці містяться в різних
множинах розбиття (це забезпечить відсутність простих циклів). Якщо вибрано ребро ei = {v, w}, то
множини розбиття, які містять вершини v та w, об’єднують в одну множину.

Крок 4. Якщо вже вибрано (n–1) ребро (у такому разі всі підмножини розбиття об’єднаються в одну), то
зупинитись, бо вибрані ребра утворюють мінімальний каркас. Інакше перейти до кроку 3.

"""


def kruskal(graph, vert, vertices):
    #sorting the graph
    graph = sorted(graph, key=lambda item: item[2])
    vertices = [set([elem]) for elem in sorted(vertices)]
    biggest_subset = 0
    sum = 0
    while biggest_subset <= vert-1:
        break_1 = False
        for elem in graph:
            break_1 = False
            if len(vertices) == 1:
                return sum
            for n1, vert1 in enumerate(vertices):
                if elem[0] in vert1 and not break_1:
                    for n2, vert2 in enumerate(vertices):
                        if elem[1] in vert2 and vert2 != vert1:
                            vertices.pop(min(n2,n1))
                            vertices.pop(max(n2,n1)-1)
                            vertices.append(vert1.union(vert2))
                            biggest_subset+=1
                            sum += elem[2]
                            break_1 = True
                            break


def main():
    graph = []
    generated = gnp_random_connected_graph(500, 0.5)
    vert = set()
    for elem in generated:
        vert.add(elem[0])
        vert.add(elem[1])
        graph.append([elem[0], elem[1], elem[2]])
    vert_len = len(vert)
    print(f'Number of vertices = {vert_len}')
    start = timeit.default_timer()
    print(kruskal(graph, vert_len, list(vert)))
    stop = timeit.default_timer()
    print(f'Algorithm time: {stop - start}')


if __name__ == '__main__':
    main()