import os

from input_output import load_graph
from GeneticStrategy import GeneticAlgorithm
from Search import Search


if __name__ == "__main__":
    graph = load_graph(os.path.join("data", "cities.csv"))
    population_size = 10
    genetic = GeneticAlgorithm(graph, population_size, 0.2, 0.01, 100, "chromossomes.pkl")
    genetic.set_chromossome_population([Search.from_submission_file(graph, os.path.join("data", "greedy_submission.csv"))] * population_size)
    genetic.run()

