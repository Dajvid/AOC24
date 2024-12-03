import re

with open('input.txt') as f:
    content = f.read()


groups = re.findall(r'mul\(([0-9]{1,3}),([0-9]{1,3})\)', content)

sum = 0
for (x, y) in groups:
    sum += int(x) * int(y)

print(f"Sum of valid mul instructions is: {sum}.")


instructions = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)|don't\(\)|do\(\)", content)

sum = 0
interpretation_enabled = True

for instruction in instructions:
    do = re.match(r"do\(\)", instruction)
    dont = re.match(r"don't\(\)", instruction)
    mul = re.match(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)", instruction)


    if do:
        interpretation_enabled = True
    elif dont:
        interpretation_enabled = False
    elif mul:
        if interpretation_enabled:
            x, y = mul.groups()
            sum += int(x) * int(y)

print(f"Sum of valid mul instructions considering also do and don't instructions is: {sum}.")
