import pandas as pd
import numpy as np
import random
import pyprind

from Search import Search


class Fitness:
    def __init__(self, search):
        self._search = search

    def get_fitness(self):
        return 1 / self._search.get_path_cost()


class GeneticAlgorithm:
    def __init__(self, graph, population_size, elite_ratio, mutation_rate, epochs):
        self._graph = graph
        self._population_size = population_size
        self._population = []
        self._elite_ratio = elite_ratio
        self._mutation_rate = mutation_rate
        self._epochs = epochs

    def run(self):
        best_chromossomes = []
        bar = pyprind.ProgBar(self._epochs, bar_char='█')

        print("[RUN] Creating initial population..")
        self.create_initial_population()

        print("[RUN] Starting epochs now.")

        for i in range(self._epochs):
            self.breed_chromossomes()
            self.mutate_chromossomes()

            sorted_chromossomes = self._sorted_chromossomes()
            best_chromossomes.append(sorted_chromossomes[0])

            print(f"Best route on epoch {i + 1} has a path cost of {sorted_chromossomes[0].get_path_cost()}")
            bar.update()

        print(bar)

        self.save_path(self._sorted_chromossomes()[0].get_path(), "best_path.path")

    def _create_chromossome_single(self):
        chromossome = Search()
        chromossome.add_city(self._graph[0])
        return chromossome

    def _create_chromossome_random(self):
        chromossome = Search()
        for city in random.sample(self._graph.get_cities(), len(self._graph)):
            chromossome.add_city(city)
        chromossome.add_city(self._graph[0])
        return chromossome

    def create_initial_population(self):
        for _ in range(self._population_size):
            self._population.append(self._create_chromossome_random())

    def _sorted_chromossomes(self):
        return sorted(self._population, key=lambda chromossome: 1 / chromossome.get_path_cost(), reverse=True)

    def select_breeding_pool(self):
        breeding_pool = []
        sorted_chromossomes = self._sorted_chromossomes()

        df = pd.DataFrame(np.array([1 / chromossome.get_path_cost() for chromossome in sorted_chromossomes]), columns=["Fitness"])
        df['cum_sum'] = df.Fitness.cumsum()
        df['cum_perc'] = 100 * df.cum_sum / df.Fitness.sum()

        for i in range(int(self._population_size * self._elite_ratio)):
            breeding_pool.append(sorted_chromossomes[i])

        for _ in range(0, self._population_size - int(self._population_size * self._elite_ratio)):
            random_threshold = 100 * random.random()
            for j in range(0, self._population_size):
                if random_threshold <= df.iat[j, 2]:
                    breeding_pool.append(sorted_chromossomes[j])
                    break

        return breeding_pool

    def crossover(self, chromossome1, chromossome2):
        child = self._create_chromossome_single()
        child_c1_path = []

        gene_a = int(random.random() * len(chromossome1))
        gene_b = int(random.random() * len(chromossome2))

        start_gene = min(1, gene_a, gene_b)
        end_gene = max(len(self._graph) - 2, gene_a, gene_b)

        for i in range(start_gene, end_gene):
            child_c1_path.append(chromossome1.get_path()[i])

        child_c1_path.extend(chromossome2.get_path())

        child_path = set(child_c1_path)

        child.add_city(self._graph[0])

        for city in child_path:
            child.add_city(city)

        child.add_city(self._graph[0])
        return child

    def breed_chromossomes(self):
        breeding_pool = self.select_breeding_pool()

        children = []
        length = len(breeding_pool) - int(self._population_size * self._elite_ratio)
        pool = random.sample(breeding_pool, len(breeding_pool))

        for i in range(0, int(self._population_size * self._elite_ratio)):
            children.append(breeding_pool[i])

        for i in range(0, length):
            child = self.crossover(pool[i], pool[len(breeding_pool) - i - 1])
            children.append(child)

        self._population = children

    def mutate(self, chromossome):
        for swapped in range(1, len(chromossome.get_path()) - 1):
            if random.random() < self._mutation_rate:
                swapWith = int(random.random() * len(chromossome.get_path()))

                city_1 = chromossome.get_path()[swapped]
                city_2 = chromossome.get_path()[swapWith]

                chromossome[swapped] = city_2
                chromossome[swapWith] = city_1

        return chromossome

    def mutate_chromossomes(self):
        for chromossome in self._population:
            self.mutate(chromossome)

    def save_path(self, path, fname):
        with open(fname, "w") as fw:
            for city in path:
                fw.write(f"{city.get_city_id()}\n")
