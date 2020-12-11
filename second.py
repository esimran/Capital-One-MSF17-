import sys

lines = []
for l in sys.stdin:
    if("\n" in l):
        lines.append(l[:-1])
    else:
        lines.append(l)

queens = 0
badSquares = set()
done = False
for row in range(0, len(lines)):
    for col in range(0, len(lines[0])):
        if lines[row][col] == "*":
            square = (row, col)
            queens += 1
            if square in badSquares:
                done = True
                print("Invalid")
                break
            else:
                badSquares.add(square)
                tR = row
                while(tR >= 0):
                    badSquares.add((tR, col))
                    tR += -1
                tR = row
                while(tR < 8):
                    badSquares.add((tR, col))
                    tR += 1
                tC = col
                while(tC >= 0):
                    badSquares.add((row, tC))
                    tC += -1
                tC = col
                while(tC < 8):
                    badSquares.add((row, tC))
                    tC += 1
                tC = col
                tR = row
                while(tC < 8 and tR < 8):
                    badSquares.add((tR, tC))
                    tR += 1
                    tC +=1
                tC = col
                tR = row
                while(tC >= 0 and tR >= 0):
                    badSquares.add((tR, tC))
                    tR += -1
                    tC += -1
                tC = col
                tR = row
                while(tC < 8 and tR >= 0):
                    badSquares.add((tR, tC))
                    tR += -1
                    tC += 1
                tC = col
                tR = row
                while(tC >= 0 and tR < 8):
                    badSquares.add((tR, tC))
                    tR += 1
                    tC += -1

if queens is 8 and not done:
    print("valid")