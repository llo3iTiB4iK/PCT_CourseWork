import random
import time
from kruskal import kruskal
import multiprocessing
import networkx as nx
import matplotlib.pyplot as plt


def gener_weight(max_weight):
    return random.randint(1, max_weight)


class Graph:
    def __init__(self, vertices, edges=None, edge_density=0.1):
        self.V = vertices  # кількість вершин графа
        self.E = edges if edges else self.rand_gener(edge_density)  # список ребер графа

    def __str__(self):
        edges = '\n'.join(f"{v1:^10}{v2:^10}{weight:^12}" for v1, v2, weight in self.E)
        return f"Вершини={self.V}\nРебра=\\\n Вершина1  Вершина2  Вага ребра\n{edges}\n"

    def rand_gener(self, density):  # функція випадкового генерування зважених ребер графа з заданою густиною ребер
        max_edge_weight = max(self.V // 10, 20)
        edges = [(v1, v1 + 1, gener_weight(max_edge_weight)) for v1 in range(self.V - 1)]  # список ребер такий, що гарантує зв'язність
        for v1 in range(1, self.V):
            for v2 in range(v1 - 1):
                # для всіх можливих пар різних вершин графа
                if random.random() <= density:  # якщо випадкове число від 0 до 1 не більше заданої густини ребер
                    edges.append((v1, v2, gener_weight(max_edge_weight)))  # з'єднати цю пару вершин
        return edges

    def find_mst(self, parallel, n_threads=10):
        if parallel:
            with multiprocessing.Pool(processes=n_threads) as executor:
                start_time = time.time()
                edges = kruskal(self.E, {v: v for v in range(self.V)}, self.V, True, executor, n_threads)
                stop_time = time.time()
        else:
            start_time = time.time()
            edges = kruskal(self.E, {v: v for v in range(self.V)}, self.V)
            stop_time = time.time()
        return Graph(self.V, edges), stop_time-start_time

    def to_networkx(self):
        G = nx.Graph()
        G.add_nodes_from(range(self.V))
        G.add_weighted_edges_from(self.E)
        return G

    def visualize_with_mst(self, mst):
        G = self.to_networkx()
        mst_G = mst.to_networkx()
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True)
        nx.draw_networkx_edges(mst_G, pos, edge_color='red')
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.show()
