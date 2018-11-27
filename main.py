import os

from input_output import load_graph
from GeneticStrategy import GeneticAlgorithm

if __name__ == "__main__":
    graph = load_graph(os.path.join("data", "cities.csv"))
    genetic = GeneticAlgorithm(graph, 100, 0.2, 0.01, 100, "chromossomes.pkl")
    genetic.run()
