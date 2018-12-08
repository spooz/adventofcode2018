from collections import defaultdict
import re

data = open('input3.txt')
claims = map(lambda s: map(int, re.findall(r'-?\d+', s)), data)
m = defaultdict(list)

overlaps = defaultdict(list)

for (claim_number, start_x, start_y, width, height) in claims:
    for i in range(start_x, start_x + width):
        for j in range(start_y, start_y + height):
            if m[(i, j)]:
                for number in m[(i, j)]:
                    overlaps[number].append(claim_number)
                    overlaps[claim_number].append(number)
            m[(i, j)].append(claim_number)

print(len([k for k in m if len(m[k]) > 1]))
print([len(overlaps[k]) for k in overlaps])
print([k for k in overlaps if len(overlaps[k]) == 0])

