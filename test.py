import sys

lines = []
for l in sys.stdin:
    if("\n" in l):
        lines.append(l[:-1])
    else:
        lines.append(l)

ans = [0, 0, 0, 0, 0]
lines.remove(lines[0])
changes = [(0, 0), (1, 0), (0, 1), (1, 1)]
for row in range(0, len(lines) - 1):
    for col in range(0, len(lines[0]) - 1):
        correct = True
        index = 0
        for change in changes:
            char = lines[row + change[0]][col + change[1]]
            if (char == '#'):
                correct = False;
            elif (char == 'X' or char == 'x'):
                index += 1
        if correct:
            ans[index] += 1

for num in ans:
    print(num)
