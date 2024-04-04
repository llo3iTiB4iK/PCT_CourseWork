import random


class Graph:
    def __init__(self, vertices, edges=None, edge_density=0.3, check_connectivity=True):
        self.V = vertices  # кількість вершин графа
        self.E = edges if edges else self.rand_gener(edge_density)  # список ребер графа
        if check_connectivity:
            while not self.is_connected():  # поки граф не зв'язний
                if edges:
                    raise Exception("Заданий граф не зв'язний")
                self.E = self.rand_gener(edge_density)  # перегенерувати ребра

    def __str__(self):
        edges = '\n'.join(f"{v1:^10}{v2:^10}{weight:^12}" for v1, v2, weight in self.E)
        return f"Вершини={self.V}\nРебра=\\\n Вершина1  Вершина2  Вага ребра\n{edges}\n"

    def rand_gener(self, density):  # функція випадкового генерування зважених ребер графа з заданою густиною ребер
        edges = []  # список ребер
        for v1 in range(1, self.V):
            for v2 in range(v1):
                # для всіх можливих пар різних вершин графа
                if random.random() <= density:  # якщо випадкове число від 0 до 1 не більше заданої густини ребер
                    edges.append((v1, v2, random.randint(5, 20)))  # з'єднати цю пару вершин
        return edges

    def is_connected(self):  # функція перевірки графа на зв'язність
        # перетворення списку ребер на список суміжності
        adjacency_list = {v:[] for v in range(self.V)}
        for v1, v2, weight in self.E:
            adjacency_list[v1].append(v2)
            adjacency_list[v2].append(v1)

        def dfs(node, visited_nodes):  # функція рекурсивного пошуку вглиб
            visited_nodes.add(node)
            for neighbor in adjacency_list[node]:
                if neighbor not in visited_nodes:
                    dfs(neighbor, visited_nodes)

        # виконуємо пошук в глибину з довільної вершини
        visited = set()
        dfs(0, visited)
        # якщо всі вершини були відвідані, то граф є зв'язним
        return len(visited) == self.V

    def kruskal(self):
        MST_edges = []  # ребра, що входять до MST
        components = {v: v for v in range(self.V)}  # спочатку кожна вершина є окремою компонентою зв'язності
        num_components = self.V  # кількість компонент
        for v1, v2, weight in sorted(self.E, key=lambda edge: edge[2]):  # для кожного ребра у порядку зростання ваги
            if components[v1] != components[v2]:  # якщо вершини лежать у різних компонентах зв'язності
                component_to_remove = components[v2]
                # об'єднати компоненти цих вершин
                for key, value in components.items():
                    if value == component_to_remove:
                        components[key] = components[v1]
                num_components -= 1
                MST_edges.append((v1, v2, weight))  # додати ребро до MST
                if num_components == 1:  # якщо залишилась одна компонента, MST знайдено
                    return Graph(vertices=self.V, edges=MST_edges, check_connectivity=False)
        raise Exception("Заданий граф не зв'язний")
