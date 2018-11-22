import pandas as pd

from Graph import Graph, City


def load_graph(filename):
    graph = Graph()
    csv = pd.read_csv(filename)
    for i in range(0, len(csv)):
        graph.append(City(csv['CityId'][i], csv['X'][i], csv['Y'][i]))
    return graph
