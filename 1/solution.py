import numpy as np

data = np.loadtxt('input.txt', dtype=int)

l0 = np.sort(data[:, 0])
l1 = np.sort(data[:, 1])


distance = np.abs(l0 - l1).sum()
print(f"The distance is: {distance}")

values, counts = np.unique(l0, return_counts=True)
l0_map = {v: c for v, c in zip(values, counts)}
values, counts = np.unique(l1, return_counts=True)
l1_map = {v: c for v, c in zip(values, counts)}

sim_score = 0
for val, count in l0_map.items():
    sim_score += val * count * l1_map.get(val, 0)

print(f"The similarity score is: {sim_score}")