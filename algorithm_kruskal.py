"""
Kruskal algorithm
"""

from generate_graph import gnp_random_connected_graph

"""
The algorithm used in my implementation

Step 1. Arrange the set of edges in ascending order of weights: e1, e2, e3,…, em.

Step 2. Divide the set of vertices into one-element subsets: {{v1}, {v2},…, {vn}}.

Step 3. Select such an next edge from an ordered sequence of edges that its ends
are contained in different. multiple partitions (this will ensure the absence of
simple cycles). If the edge ei = {v, w} is selected, then
split sets containing vertices v and w are combined into one set.

Step 4. If (n – 1) edge is already selected (in this case all subsets of
partition will be combined into one), then
stop because the selected ribs form a minimal frame. Otherwise, go to step 3.

- from a lecture by Yurii Shcherbyna.
"""


def kruskal(graph: list):
    """
    Kruskal algorithm.
    returns minimum spanning tree cost.
    """
    vert_set = set()
    for elem in graph:
        vert_set.add(elem[0])
        vert_set.add(elem[1])
    vertices = list(vert_set)
    graph = sorted(graph, key=lambda item: item[2])
    vertices = [set([elem]) for elem in sorted(vertices)]
    sum = 0
    while 1:
        break_1 = False
        for elem in graph:
            break_1 = False
            if len(vertices) == 1:
                return sum
            for n1, vert1 in enumerate(vertices):
                if elem[0] in vert1 and not break_1:
                    for n2, vert2 in enumerate(vertices):
                        if elem[1] in vert2 and vert2 != vert1:
                            vertices.pop(min(n2, n1))
                            vertices.pop(max(n2, n1)-1)
                            vertices.append(vert1.union(vert2))
                            sum += elem[2]
                            break_1 = True
                            break


def timer_kruskal(graph):
    """
    Timer for Kruskall's algorithm
    """
    import timeit
    start = timeit.default_timer()
    kruskal(graph)
    stop = timeit.default_timer()
    return stop - start


def main():
    """
    Main function
    """
    generated = gnp_random_connected_graph(500, 0.5)
    print(timer_kruskal(generated))


if __name__ == '__main__':
    main()
