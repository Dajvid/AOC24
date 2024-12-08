import math
import numpy as np


class Map:
    def __init__(self, filename="input.txt"):
        with open(filename) as f:
            lines = f.readlines()

        self.array = np.array([[c for c in line.strip()] for line in lines])
        antena_types = np.unique(self.array)
        self.antenas = {str(antena): [] for antena in antena_types if antena != "."}
        for antena_type in self.antenas:
            locations = np.where(self.array == antena_type)
            for x, y in zip(locations[0], locations[1]):
                self.antenas[antena_type].append((int(x), int(y)))

    def calculate_antinode(self, closer_antena, other_antena):
        antena_diff = np.array(closer_antena) - np.array(other_antena)
        antinode = closer_antena + antena_diff
        if self.is_in_bounds(antinode):
            self.array[tuple(antinode)] = "#"

    def calculate_antinode_with_resonant_harmonics(self, closer_antena, other_antena):
        antena_diff = np.array(closer_antena) - np.array(other_antena)
        gcd = math.gcd(antena_diff[0], antena_diff[1])
        antena_diff = antena_diff // gcd

        i = 0
        while self.is_in_bounds(closer_antena + antena_diff * i):
            self.array[tuple(closer_antena + antena_diff * i)] = "#"
            i += 1

    def is_in_bounds(self, vector):
        return 0 <= vector[0] < len(self.array) and 0 <= vector[1] < len(self.array[0])

    def calculate_antinodes(self, with_resonant_harmonics=False):
        for antena_type in self.antenas:
            for closer_antena in self.antenas[antena_type]:
                for other_antena in self.antenas[antena_type]:
                    if closer_antena != other_antena:
                        if with_resonant_harmonics:
                            self.calculate_antinode_with_resonant_harmonics(closer_antena, other_antena)
                        else:
                            self.calculate_antinode(closer_antena, other_antena)

    def antinodes_count(self):
        return np.sum(self.array == "#")


map = Map(filename="input.txt")
map.calculate_antinodes()
print(f"Number of antinodes: {map.antinodes_count()}")

map = Map(filename="input.txt")
map.calculate_antinodes(with_resonant_harmonics=True)
print(f"Number of antinodes with resonant harmonics: {map.antinodes_count()}")
