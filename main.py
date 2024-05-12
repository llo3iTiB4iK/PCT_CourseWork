from Graph import Graph

if __name__ == '__main__':
    graph = Graph(vertices=int(input("Введіть кількість вершин -> ")), edge_density=float(input("Введіть густину ребер (від 0 до 1) -> ")))
    mst, _ = graph.find_mst(parallel=bool(input("Послідовний (0) чи паралельний (1) алгоритм? -> ")))
    print(f'Граф:\n{graph}\nЙого найкоротше остовне дерево (MST):\n{mst}')
    graph.visualize_with_mst(mst)
