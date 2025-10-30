import random
from collections import Counter
import copy
from itertools import combinations
from matplotlib import pyplot as plt
from time import time
from z3 import Solver, Bool, Or, Sum, sat, If
import json
import numpy as np
import os


def get_subsets_of_size(my_list, size):
    return list(combinations(my_list, size))


def count_time(func, arg):
    start_time = time()
    func_res = func(arg)
    end_time = time()
    return end_time - start_time, func_res


class Graph:
    def __init__(self, vertices_number):
        self.graph_dict = {}
        self.vertices_number = vertices_number
        self.edges_number = random.randint(1, self.vertices_number * (self.vertices_number - 1) // 2)
        self.greedy_result = 0
        self.k = 0
        self.times = {}
        self.generate_random()
        self.greedy_vertex_cover_number()

    def get_degree(self, vertex):
        return len(self.graph_dict[vertex])

    def get_max_degree_vertice(self):
        return max(self.graph_dict, key=lambda vertex: len(self.graph_dict[vertex]))

    def vertex_cover_smt(self,  k):
        graph_dict_copy = copy.deepcopy(self.graph_dict)
        V, E = graph_dict_copy.keys(), [(u, v) for u in graph_dict_copy for v in graph_dict_copy[u]]
        solver = Solver()

        x = {v: Bool(f"x_{v}") for v in V}
        for (u, v) in E:
            solver.add(Or(x[u], x[v]))
        solver.add(Sum([If(x[v], 1, 0) for v in V]) <= k)

        if solver.check() == sat:
            model = solver.model()
            cover = [v for v in V if model.evaluate(x[v])]
            return cover
        else:
            return None

    def count_degrees(self):
        all_degrees = [self.get_degree(i) for i in self.graph_dict.keys()]
        return dict(Counter(all_degrees))

    def generate_random(self):
        possible_vertices = [i for i in range(self.vertices_number)]
        for i in range(self.vertices_number):
            self.graph_dict[i] = set()
        for _ in range(self.edges_number):
            random_vertex = random.choice(possible_vertices)
            possible_edges = [i for i in range(self.vertices_number) if i not in self.graph_dict[random_vertex]
                              and i != random_vertex]
            if possible_edges:
                edge = random.choice(possible_edges)
                self.graph_dict[random_vertex].add(edge)
                self.graph_dict[edge].add(random_vertex)

    def delete_edges_from_vertice(self, vertice):
        for v in self.graph_dict[vertice]:
            self.graph_dict[v].remove(vertice)
            if not self.graph_dict[v]:
                del self.graph_dict[v]

        del self.graph_dict[vertice]

    def bruteforce_vertex_cover_number(self, k):
        vertices = list(self.graph_dict.keys())
        all_subsets = get_subsets_of_size(vertices, k)

        for subset in all_subsets:
            graph_copy = copy.deepcopy(self.graph_dict)
            to_delete = []
            for vertice in self.graph_dict:
                if not graph_copy[vertice]:
                    to_delete.append(vertice)
            for vertice in to_delete:
                del self.graph_dict[vertice]
            for vertice in subset:
                if vertice not in self.graph_dict:
                    pass
                else:
                    self.delete_edges_from_vertice(vertice)

            if not self.graph_dict:
                self.graph_dict = graph_copy
                return subset
            else:
                self.graph_dict = graph_copy
        return None

    def greedy_vertex_cover_number(self):
        result = 0
        subset_result = []

        graph_copy = copy.deepcopy(self.graph_dict)
        while self.graph_dict:
            max_degree_vertice = self.get_max_degree_vertice()
            subset_result.append(max_degree_vertice)
            self.delete_edges_from_vertice(max_degree_vertice)
            result += 1
        self.graph_dict = graph_copy
        self.greedy_result = result
        if random.choice([True, False]):
            self.k = result
        else:
            self.k = result - 1

    def run_brute_with_time(self):
        execution_time, func_res = count_time(self.bruteforce_vertex_cover_number, self.k)
        self.times["brute"] = execution_time
        return func_res

    def run_smt_with_time(self):
        execution_time, func_res = count_time(self.vertex_cover_smt, self.k)
        self.times["smt"] = execution_time
        return func_res


def generate_random_graphs(number_of_graphs=1000, epochs=100):
    list_of_graphs = []
    step = number_of_graphs // epochs
    number_of_vertexes = 1
    for i in range(epochs):
        print("Epoch: ", i)
        number_of_vertexes += 1
        for j in range(step):
            g_graph = Graph(vertices_number=number_of_vertexes)
            list_of_graphs.append(g_graph)

    return list_of_graphs


def plot_statistics(list_of_graphs):
    k_list = [graph_.k for graph_ in list_of_graphs]
    counter = Counter(k_list)
    plt.xlabel("K")
    plt.ylabel("number of graphs")
    plt.bar(list(counter.keys()), list(counter.values()))
    plt.savefig("plots/k_histogram.png")
    plt.close()

    plt.show()


def save_mean_time_data(graph_list, method: str, output_file: str):
    k_time_dict = {}
    vertices_time_dict = {}
    iterator = 0
    start_time = time()

    for _graph in graph_list:
        print("Iteration: ", iterator)
        print("Global time", time() - start_time)
        getattr(_graph, f"run_{method}_with_time")()
        k_time_dict.setdefault(_graph.k, []).append(_graph.times[method])
        vertices_time_dict.setdefault(_graph.vertices_number, []).append(_graph.times[method])
        iterator += 1

        if time() - start_time > 600:
            break

    output_data = {
        "k_time_dict": k_time_dict,
        "vertices_time_dict": vertices_time_dict
    }
    with open(output_file, 'w') as json_file:
        json.dump(output_data, json_file, indent=4)

    print(f"Dane zostały zapisane do pliku: {output_file}")


def ensure_folder_exists(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)


def compute_statistics(data):
    statistics = {}
    for key, values in data.items():
        statistics[int(key)] = {
            "mean": np.mean(values),
            "std": np.std(values),
            "min": np.min(values),
            "max": np.max(values)
        }
    return statistics


def plot_comparative_statistics(smt_stats, brute_stats, stat_key, x_label, output_path):
    smt_values = {k: v[stat_key] for k, v in smt_stats.items()}
    brute_values = {k: v[stat_key] for k, v in brute_stats.items()}

    plt.plot(smt_values.keys(), smt_values.values(), label=f"SMT {stat_key}", marker='o')
    plt.plot(brute_values.keys(), brute_values.values(), label=f"Brute {stat_key}", marker='x')

    plt.xlabel(x_label)
    plt.ylabel(stat_key.capitalize())
    plt.title(f"Comparison of {stat_key.capitalize()} ({x_label})")
    plt.legend()

    plt.savefig(output_path)
    plt.close()


def generate_comparative_plots(smt_file, brute_file):
    with open(smt_file, 'r') as f:
        smt_data = json.load(f)
    with open(brute_file, 'r') as f:
        brute_data = json.load(f)

    smt_k_stats = compute_statistics(smt_data["k_time_dict"])
    smt_v_stats = compute_statistics(smt_data["vertices_time_dict"])
    brute_k_stats = compute_statistics(brute_data["k_time_dict"])
    brute_v_stats = compute_statistics(brute_data["vertices_time_dict"])

    ensure_folder_exists("plots")

    for stat_key in ["mean", "std", "min", "max"]:
        plot_comparative_statistics(
            smt_k_stats, brute_k_stats, stat_key, "k", f"plots/comparison_{stat_key}_k.png"
        )
        plot_comparative_statistics(
            smt_v_stats, brute_v_stats, stat_key, "Number of vertices", f"plots/comparison_{stat_key}_vertices.png"
        )


def experiment_brute():
    graphs_list = generate_random_graphs(100, 100)
    graphs_list.sort(key=lambda x: x.vertices_number)
    graphs_list = graphs_list[19:]
    max_brute = 0

    for i, graph in enumerate(graphs_list):
        print("Brute: ", i)
        start_time = time()
        graph.run_brute_with_time()
        elapsed_time = time() - start_time
        graph.times["brute"] = elapsed_time
        if elapsed_time > 120:
            print(f"Brute: Stopping at graph with {graph.vertices_number} vertices")
            return max_brute
        max_brute = graph.vertices_number

    return max_brute


def experiment_smt():
    graphs_list = generate_random_graphs(130, 130)
    graphs_list.sort(key=lambda x: x.vertices_number)
    graphs_list = graphs_list[90:]
    max_smt = 0

    for i, graph in enumerate(graphs_list):
        print("SMT: ", i)
        start_time = time()
        graph.run_smt_with_time()
        elapsed_time = time() - start_time
        graph.times["smt"] = elapsed_time
        if elapsed_time > 120:
            print(f"SMT: Stopping at graph with {graph.vertices_number} vertices")
            return max_smt
        max_smt = graph.vertices_number

    return max_smt

# Uncomment the code below to run the experiments
"""
store_smt = []
store_brute = []
for i in range(10):
    print(f"Experiment {i}")
    store_smt.append(experiment_smt())
    store_brute.append(experiment_brute())
graphs = generate_random_graphs(5000, 100)
save_mean_time_data(graphs, "smt", "smt2.json")
save_mean_time_data(graphs, "brute", "brute2.json")
generate_comparative_plots("smt2.json", "brute2.json")
plot_statistics(graphs)
"""

