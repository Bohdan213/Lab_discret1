from generate_graph import gnp_random_connected_graph
from algorithm_prima import prim
import csv

def main():
    data = []
    for i in range(10, 1000, 10):
        graph = gnp_random_connected_graph(i, 0,5)
        prim_time = prim(i, graph)
        kraskal_time = kraskal(i, graph)
        data.append((i, prim_time, kraskal_time))
    with open('rezults.csv', mode='w') as file:
        file_writer = csv.writer(file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        for rez in data:
            file_writer.writerow([rez[0], rez[1], rez[2]])

if __name__ == '__main__':
    main()
