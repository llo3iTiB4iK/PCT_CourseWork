from sort import merge_sort, merge_sort_parallel


def kruskal(E, components, num_components, parallel=False, pool=None, n_threads=None):
    MST_edges = []  # ребра, що входять до MST
    for v1, v2, weight in (merge_sort_parallel(E, pool, n_threads) if parallel else merge_sort(E)):  # для кожного ребра у порядку зростання ваги
        if components[v1] != components[v2]:  # якщо вершини лежать у різних компонентах зв'язності
            component_to_remove = components[v2]
            # об'єднати компоненти цих вершин
            for key, value in components.items():
                if value == component_to_remove:
                    components[key] = components[v1]
            MST_edges.append((v1, v2, weight))  # додати ребро до MST
            num_components -= 1
            if num_components == 1:  # якщо залишилась одна компонента, MST знайдено
                return MST_edges
