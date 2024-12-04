
def scan_adjecent(matrix, x, y, remaining_match, direction):
    """
    directions: h: |, v: -, d: \\, a: /
    """
    if not remaining_match:
        return 1
    found = 0
    if not direction or direction == 'h':
        if y + 1 < len(matrix[0]) and matrix[x][y + 1] == remaining_match[0]:
            found += scan_adjecent(matrix, x, y + 1, remaining_match[1:], 'h')
        if y - 1 >= 0 and matrix[x][y - 1] == remaining_match[0]:
            found += scan_adjecent(matrix, x, y - 1, remaining_match[1:], 'h')
    if not direction or direction == 'v':
        if x + 1 < len(matrix) and matrix[x + 1][y] == remaining_match[0]:
            found += scan_adjecent(matrix, x + 1, y, remaining_match[1:], 'v')
        if x - 1 >= 0 and matrix[x - 1][y] == remaining_match[0]:
            found += scan_adjecent(matrix, x - 1, y, remaining_match[1:], 'v')
    if not direction or direction == 'd':
        if x + 1 < len(matrix) and y + 1 < len(matrix[0]) and matrix[x + 1][y + 1] == remaining_match[0]:
            found += scan_adjecent(matrix, x + 1, y + 1, remaining_match[1:], 'd')
        if x - 1 >= 0 and y - 1 >= 0 and matrix[x - 1][y - 1] == remaining_match[0]:
            found += scan_adjecent(matrix, x - 1, y - 1, remaining_match[1:], 'd')
    if not direction or direction == 'a':
        if x + 1 < len(matrix) and y - 1 >= 0 and matrix[x + 1][y - 1] == remaining_match[0]:
            found += scan_adjecent(matrix, x + 1, y - 1, remaining_match[1:], 'a')
        if x - 1 >= 0 and  y + 1 < len(matrix[0]) and matrix[x - 1][y + 1] == remaining_match[0]:
            found += scan_adjecent(matrix, x - 1, y + 1, remaining_match[1:], 'a')
    return found


def print_matrix(matrix):
    for x in matrix:
        print("".join(x))


def cmp_pattern(matrix, x_b, y_b, pattern):
    for x in range(len(pattern)):
        for y in range(len(pattern[x])):
            try:
                if pattern[x][y] != matrix[x_b + x][y_b + y] and pattern[x][y] != '*':
                    return False
            except IndexError:
                return False
    return True

def count_pattern_occurrences(matrix, pattern):
    occurrences = 0
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if cmp_pattern(matrix, x, y, pattern):
                occurrences += 1
    return occurrences



with open('input.txt') as f:
    lines = f.readlines()

matrix = [list(line.strip()) for line in lines]

# found = 0
# for x in range(len(matrix)):
#     for y in range(len(matrix[x])):
#         if matrix[x][y] == 'X':
#             l = scan_adjecent(matrix, x, y, 'MAS', None)
#             found += l
# print("Found XMAS in the matrix: ", found)
patterns = \
    [
        [["M", "*", "S"],
        ["*", "A", "*"],
        ["M", "*", "S"]],

        [["S", "*", "S"],
        ["*", "A", "*"],
        ["M", "*", "M"]],

        [["S", "*", "M"],
         ["*", "A", "*"],
         ["S", "*", "M"]],

        [["M", "*", "M"],
         ["*", "A", "*"],
         ["S", "*", "S"]],
    ]
pattern = [[]]
o = 0
for pattern in patterns:
    o += count_pattern_occurrences(matrix, pattern)
print(o)
