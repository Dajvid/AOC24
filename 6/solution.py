import numpy as np

class LoopedException(Exception):
    pass

class Map:
    def __init__(self, filename="input.txt"):
        with open(filename) as f:
            lines = f.readlines()

        self.simulation_ended = False
        self.looped = False
        self.array = np.array([[c for c in line.strip()] for line in lines])
        location = np.where(self.array == "^")
        self.origin_x = int(location[0][0])
        self.origin_y = int(location[1][0])
        self.x = self.origin_x
        self.y = self.origin_y
        self.direction = "up"
        self.array[self.x, self.y] = "X"
        self.visited = {(x, y): [] for x in range(len(self.array)) for y in range(len(self.array[0]))}
        self.visited[(self.x, self.y)].append(self.direction)

    def is_looped(self):
        return self.direction in self.visited[(self.x, self.y)]

    def add_obstacle(self, x, y):
        self.array[x, y] = "#"

    def move(self):
        x = self.x
        y = self.y
        if self.direction == "up":
            x -= 1
        elif self.direction == "down":
            x += 1
        elif self.direction == "left":
            y -= 1
        elif self.direction == "right":
            y += 1

        if not self.is_in_bounds(x, y):
            raise IndexError

        if self.array[x, y] != "#":
            self.x = x
            self.y = y
            self.array[self.x, self.y] = "X"
            if self.is_looped():
                raise LoopedException
            self.visited[self.x, self.y].append(self.direction)
        else:
            self.direction = self.change_direction()

    def change_direction(self):
        if self.direction == "up":
            return "right"
        elif self.direction == "right":
            return "down"
        elif self.direction == "down":
            return "left"
        elif self.direction == "left":
            return "up"

    def is_in_bounds(self, x, y):
        return 0 <= x < len(self.array) and 0 <= y < len(self.array[0])

    def simulate(self):
        while True:
            try:
                self.move()
            except IndexError:
                self.simulation_ended = True
                break
            except LoopedException:
                self.looped = True
                break


map = Map("input.txt")
map.simulate()
print(np.sum(map.array == "X"))

looped = 0
for x in range(map.array.shape[0]):
    for y in range(map.array.shape[1]):
        print("Trying", x, y)
        map = Map("input.txt")
        if not x == map.origin_x or not y == map.origin_y:
            map.add_obstacle(x, y)
            map.simulate()
            if map.looped:
                looped += 1

print(looped)