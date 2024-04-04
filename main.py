from Graph import Graph
import time

if __name__ == '__main__':
    graph = Graph(vertices=10000)
    start_time = time.time()
    mst = graph.kruskal()
    execution_time = time.time() - start_time
    print(f'Час виконання послідовного алгоритму = {round(execution_time, 3)} сек.')
    # print(f'Граф:\n{graph}\nЙого найкоротше остовне дерево (MST):\n{mst}')
