a, c, m = input().split(" ")
a, c, m = int(a), int(c), int(m)
r = 0

grid = []
for i in range(10):
    row = []
    for j in range(10):
        row.append("O")
    grid.append(row)

def CheckAdjecent(Xstart, Xend, Ystart, Yend, matrix):
    for i in range(Ystart, Yend + 1):
        for j in range(Xstart, Xend + 1):
            if j > 9 or i > 9:
                continue
            if matrix[i][j] == "X":
                return False
    return True

for ship_length in range(4, 0, -1):
    for repeats in range(5 - ship_length):
        placed = False
        while placed == False:
            r = str((a * int(r) + c) % m)

            x = int(r[len(r) - 1])
            if len(r) == 1:
                y = 0
            else:
                y = int(r[len(r) - 2])
            r = (a * int(r) + c) % m

            if r % 2 == 0:
                orientation = "H"

                if (x + ship_length - 1) < 10 and (CheckAdjecent(x - 1, x + ship_length + 1, y - 1, y + 1, grid) == True):
                    for i in range(ship_length):
                        grid[y][x + i] = "X"
                        placed = True
            else:
                orientation = "V"
            
                if (y + ship_length - 1) < 10 and (CheckAdjecent(x - 1, x + 1, y - 1, y + ship_length + 1, grid) == True):
                    for i in range(ship_length):
                        grid[y + i][x] = "X"
                        placed = True

            
            if placed == True:
                print(x, y, orientation)
                