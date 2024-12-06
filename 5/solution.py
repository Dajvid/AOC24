from math import ceil

def get_invalid_index(update, rules):
    update_reversed = update[::-1]
    for i in range(len(update_reversed)):
        relevant_rules = set(rules.get(update_reversed[i], []))

        if set(update_reversed[i+1:]).intersection(relevant_rules):
            return len(update) - i - 1

    return -1

def sum_middle_page_numers(updates):
    sum = 0
    for update in updates:
        sum += update[len(update) // 2]
    return sum

rules = {}

with open('input.txt') as f:
    while True:
        line = f.readline().strip()
        if not line:
            break
        a, b = [int(a) for a in line.split('|')]
        rules.setdefault(a, []).append(b)

    updates = [[int(rec) for rec in line.strip().split(",")] for line in f.readlines()]

valid_updates = []
invalid_updates = []
for update in updates:
    invalid = get_invalid_index(update, rules)
    if invalid == -1:
        valid_updates.append(update)
    else:
        invalid_updates.append(update)



print(sum_middle_page_numers(valid_updates))

for update in invalid_updates:
    while get_invalid_index(update, rules) != -1:
        inv_idx = get_invalid_index(update, rules)
        for i in range(len(update), 0, -1):
            inv_idx = get_invalid_index(update[:i], rules)
            if inv_idx == -1:
                break
            update[inv_idx], update[inv_idx - 1] = update[inv_idx - 1], update[inv_idx]

print(sum_middle_page_numers(invalid_updates))
