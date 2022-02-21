import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.style as style

# style.use('dark_background')
def draw_plots():
    style.use('seaborn-dark-palette')

    data = pd.read_csv('results.csv')
    # data = pd.read_csv('second_results.csv')
    
    plt.figure(1)

    plt.plot(data.edges, data.prim_1, 'b.-', label='Prim 0.1', color='green')
    plt.plot(data.edges, data.kruskal_1, 'b.-', label='Kruskal 0.1', color='red')
    plt.suptitle('(density: 0.1)')
    plt.title('Algorithm Comparison ', fontdict={
            'fontsize': 15, 'fontweight': 'bold'})
    plt.xlabel('Number of vertices')
    plt.ylabel('Time')
    plt.xticks([0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])
    # plt.xticks([10, 910, 1810, 2710, 3910])
    max_1 = max(max(data.kruskal_1), max(data.prim_1))
    plt.yticks([0, max_1/2, max_1])
    plt.legend()
    plt.figure(2)

    plt.plot(data.edges, data.prim_5, 'b.-', label='Prim 0.5', color='green')
    plt.plot(data.edges, data.kruskal_5, 'b.-',
            label='Kruskal 0.5', color='red')
    plt.suptitle('(density: 0.5)')
    plt.title('Algorithm Comparison ', fontdict={
            'fontsize': 15, 'fontweight': 'bold'})
    plt.xlabel('Number of vertices')
    plt.ylabel('Time')
    plt.xticks([0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])
    plt.xticks([10, 910, 1810, 2710, 3910])
    max_5 = max(max(data.kruskal_5), max(data.prim_5))
    plt.yticks([0, max_5/2, max_5])
    plt.legend()

    plt.figure(3)
    plt.plot(data.edges, data.prim_9, 'b.-', label='Prim 0.9', color='green')
    plt.plot(data.edges, data.kruskal_9, 'b.-', label='Kruskal 0.9', color='red')
    plt.suptitle('(density: 0.9)')
    plt.title('Algorithm Comparison ', fontdict={
            'fontsize': 15, 'fontweight': 'bold'})
    plt.xlabel('Number of vertices')
    plt.ylabel('Time')
    plt.xticks([0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])
    plt.xticks([10, 910, 1810, 2710, 3910])
    max_9 = max(max(data.kruskal_9), max(data.prim_9))
    plt.yticks([0, max_9/2, max_9])
    plt.legend()

    plt.figure(1).savefig('images/density1a.jpg')
    plt.figure(2).savefig('images/density5a.jpg')
    plt.figure(3).savefig('images/density9a.jpg')
    # plt.show()

if __name__ == '__main__':
    draw_plots()