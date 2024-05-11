from Graph import Graph

VERTICES = [500, 1000, 2000, 5000, 10000]
EDGE_DENSITIES = [0.1, 0.3, 0.5]
N_THREADS = [2, 4, 6, 8]
N_REPEATS = 20

if __name__ == '__main__':
    for vertices in VERTICES:
        for edge_density in EDGE_DENSITIES:
            print(f"Граф на {vertices} вершин, густина ребер = {edge_density}")
            graph = Graph(vertices=vertices, edge_density=edge_density)
            serial_times = []
            for _ in range(N_REPEATS):
                mst, exec_time = graph.find_mst(parallel=False)
                serial_times.append(exec_time)
            avg_exec_time_serial = round(sum(serial_times) / len(serial_times), 3)
            print(f'Середній час виконання послідовного алгоритму = {avg_exec_time_serial} сек.')
            for n_threads in N_THREADS:
                parallel_times = []
                for _ in range(N_REPEATS):
                    mst, exec_time = graph.find_mst(parallel=True, n_threads=n_threads)
                    parallel_times.append(exec_time)
                avg_exec_time_parallel = round(sum(parallel_times) / len(parallel_times), 3)
                print(f'Час виконання паралельного алгоритму ({n_threads} потоків) = {avg_exec_time_parallel} сек.')
                print(f'Прискорення: {round(avg_exec_time_serial/avg_exec_time_parallel, 3)}')
            print()

    # print(f'Граф:\n{graph}\nЙого найкоротше остовне дерево (MST):\n{mst}')
