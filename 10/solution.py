import numpy as np

class TopologicalMap:
    def __init__(self, filename="input.txt"):
        with open(filename) as f:
            lines = f.readlines()
        self.arr = np.array([list(line.strip()) for line in lines]).astype(int)
        self.top_value = 9

    def is_in_bounds(self, position):
        return 0 <= position[0] < self.arr.shape[0] and 0 <= position[1] < self.arr.shape[1]

    def search_position(self, position, value, trailhead_tops, calculate_rating=False):
        directions = np.array([[0, 1], [1, 0], [0, -1], [-1, 0]])
        for direction in directions:
            new_position = tuple(position + direction)
            if self.is_in_bounds(new_position) and self.arr[new_position] == value:
                if self.arr[new_position] == self.top_value:
                    trailhead_tops[new_position] = trailhead_tops[new_position] + 1 if calculate_rating else 1
                else:
                    self.search_position(new_position, value + 1, trailhead_tops, calculate_rating)

    def search_trailhead(self, trailhead_indices, calculate_rating=False):
        if self.arr[trailhead_indices] != 0:
            raise ValueError("Non-trailhead indices passed to search_trailhead")

        trailhead_tops = np.zeros_like(self.arr)
        self.search_position(trailhead_indices, 1, trailhead_tops, calculate_rating)
        return np.sum(trailhead_tops)


topological_map = TopologicalMap("input.txt")
trailheads = np.where(topological_map.arr == 0)

trails = 0
for trailhead in zip(trailheads[0], trailheads[1]):
    trails += topological_map.search_trailhead(trailhead)
print("Number of trails:", trails)

total_trail_ratings = 0
for trailhead in zip(trailheads[0], trailheads[1]):
    total_trail_ratings += topological_map.search_trailhead(trailhead, calculate_rating=True)
print("Total trail raitings:", total_trail_ratings)
