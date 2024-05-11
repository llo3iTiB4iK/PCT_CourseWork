import random
import time
from Kruskal import kruskal
import multiprocessing
from sort import merge_sort, merge_sort_parallel


def gener_weight():
    return random.randint(1, 100)


class Graph:
    def __init__(self, vertices, edges=None, edge_density=0.3):
        self.V = vertices  # кількість вершин графа
        self.E = edges if edges else self.rand_gener(edge_density)  # список ребер графа

    def __str__(self):
        edges = '\n'.join(f"{v1:^10}{v2:^10}{weight:^12}" for v1, v2, weight in self.E)
        return f"Вершини={self.V}\nРебра=\\\n Вершина1  Вершина2  Вага ребра\n{edges}\n"

    def rand_gener(self, density):  # функція випадкового генерування зважених ребер графа з заданою густиною ребер
        edges = [(v1, v1 + 1, gener_weight()) for v1 in range(self.V - 1)]  # список ребер такий, що гарантує зв'язність
        for v1 in range(1, self.V):
            for v2 in range(v1 - 1):
                # для всіх можливих пар різних вершин графа
                if random.random() <= density:  # якщо випадкове число від 0 до 1 не більше заданої густини ребер
                    edges.append((v1, v2, gener_weight()))  # з'єднати цю пару вершин
        return edges

    def find_mst(self, parallel, n_threads=10):
        if parallel:
            with multiprocessing.Pool(processes=n_threads) as executor:
                start_time = time.time()
                edges = kruskal(merge_sort_parallel, self.E, {v: v for v in range(self.V)}, self.V, executor, n_threads)
                stop_time = time.time()
        else:
            start_time = time.time()
            edges = kruskal(merge_sort, self.E, {v: v for v in range(self.V)}, self.V)
            stop_time = time.time()
        return Graph(self.V, edges), stop_time-start_time
