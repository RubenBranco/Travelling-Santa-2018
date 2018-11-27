from Graph import Graph

import math


def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))


class Search:
    def __init__(self):
        self._path = []
        self._path_cost = 0

    def _calculate_latest_path_cost(self):
        if len(self._path) > 1:
            coord1 = (self._path[-1].getX(), self._path[-1].getY())
            coord2 = (self._path[-2].getX(), self._path[-2].getY())
            path_cost = Graph.euclidean_distance(coord1, coord2)
            if len(self._path) % 10 == 0 and not is_prime(self._path[-2].get_city_id()):
                path_cost += path_cost * 0.10
            self._path_cost += path_cost

    def add_city(self, city):
        self._path.append(city)
        city.visit()
        self._calculate_latest_path_cost()

    def get_path(self):
        return self._path

    def __setitem__(self, idx, value):
        self._path[idx] = value

    def __len__(self):
        return len(self._path)

    def calculate_path_cost(self):
        self._path_cost = 0
        for i, city in enumerate(self._path[1:], start=1):
            coord1 = (city.getX(), city.getY())
            coord2 = (self._path[i - 1].getX(), self._path[i - 1].getY())
            path_cost = Graph.euclidean_distance(coord1, coord2)
            if i % 10 == 0 and not is_prime(self._path[i - 1].get_city_id()):
                path_cost += path_cost * 0.10
            self._path_cost += path_cost

    def get_path_cost(self):
        return self._path_cost
