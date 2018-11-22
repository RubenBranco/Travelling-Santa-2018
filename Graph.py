import math


class Graph:
    def __init__(self):
        self._cities = []

    def __getitem__(self, idx):
        return self._cities[idx]

    def __setitem__(self, idx, value):
        self._cities[idx] = value

    def append(self, city):
        self._cities.append(city)

    @staticmethod
    def euclidean_distance(coord1, coord2):
        return math.sqrt((coord2[0] - coord1[0]) ** 2 + (coord2[1] - coord1[1]) ** 2)


class City:
    def __init__(self, city_id, x, y):
        self._city_id = city_id
        self._x = x
        self._y = y

    def getX(self):
        return self._x

    def getY(self):
        return self._y

    def get_city_id(self):
        return self._city_id
