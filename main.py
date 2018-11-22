import os

from input_output import load_graph


if __name__ == "__main__":
    graph = load_graph(os.path.join("data", "cities.csv"))
