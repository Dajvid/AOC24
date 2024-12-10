import re

with open("input.txt") as f:
    line = f.readline()

disk_map =  [int(x) for x in line.strip()]

filesystem = []
datablock_id = 0
for i, num in enumerate(disk_map):
    if i % 2 == 1:
        filesystem.extend("." * num)
    else:
        filesystem.extend([datablock_id] * num)
        datablock_id += 1


# fs = filesystem.copy()
# for i in range(len(fs) - 1, 0, -1):
#     if fs[i] != ".":
#         leftmost_empty_index = fs.index(".")
#         if leftmost_empty_index > i:
#             break
#         else:
#             fs[leftmost_empty_index], fs[i] = fs[i], fs[leftmost_empty_index]
#
# checksum = sum([value * i for i, value in enumerate(fs) if value != "."])
# print(f"Checksum: {checksum}")

fs = [str(a) for a in filesystem]
i = len(fs) - 1
while i >= 0:
    if fs[i] != ".":
        match = list(re.finditer(f"(?:{fs[i]})+", "".join(fs)))[-1]
        free_block_fit = re.search(f"\\.{{{len(match.group())}}}", "".join(fs))
        i -= len(match.group())
        if free_block_fit and free_block_fit.start() < match.start():
            fs[free_block_fit.start():free_block_fit.end()], fs[match.start():match.end()] = fs[match.start():match.end()], fs[free_block_fit.start():free_block_fit.end()]
    else:
        i -= 1
print(fs)
checksum = sum([int(value) * i for i, value in enumerate(fs) if value != "."])
print(f"Checksum: {checksum}")