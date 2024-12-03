from itertools import pairwise

def is_report_safe(report):
    increasing = all(x <= y for x, y in pairwise(report))
    decreasing = all(x >= y for x, y in pairwise(report))
    adjacent = all(1 <= abs(x - y) <= 3 for x, y in pairwise(report))
    return adjacent and (increasing or decreasing)


with open('input.txt') as f:
    lines = f.readlines()

reports = [list(map(int, line.strip().split(' '))) for line in lines]

safe = 0
for report in reports:
    if is_report_safe(report):
        safe += 1

print(f"Safe reports: {safe}")


safe = 0
for report in reports:
    if is_report_safe(report):
        safe += 1
    else:
        for i in range(len(report)):
            dampened_report = report[:i] + report[i+1:]
            if is_report_safe(dampened_report):
                safe += 1
                break

print(f"Safe reports considering The Problem Dampener: {safe}")
