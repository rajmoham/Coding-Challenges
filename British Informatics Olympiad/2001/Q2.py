from ntpath import join
from operator import truediv


grid = []
for i in range(11):
    row = []
    for j in range(11):
        row.append(".")
    grid.append(row)

def PrintGrid():
    for i in range(len(grid)-1, -1, -1):
        print(" ",join(grid[i]))

x1, y1, dir1 = input().split(" ")
x2, y2, dir2 = input().split(" ")
x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

def ChangeGridColour(posx, posy):
    if grid[posy-1][posx-1] == ".":
        grid[posy - 1][posx - 1] = "*"
    elif grid[posy - 1][posx - 1] == "*":
        grid[posy - 1][posx - 1] = "."

def ChangeDirection(d, squarecolour):
    if squarecolour == ".":
        if d == "T":
            d = "R"
        elif d == "R":
            d = "B"
        elif d == "B":
            d = "L"
        elif d == "L":
            d = "T"
    elif squarecolour == "*":
        if d == "T":
            d = "L"
        elif d == "R":
            d = "T"
        elif d == "B":
            d = "R"
        elif d == "L":
            d = "B"

    return d
    
def MoveAnt(xpos, ypos, direction):
    ongrid = True

    if direction == "T":
        if ypos == 11:
            ongrid = False
        else:
            ypos += 1
    elif direction == "R":
        if xpos == 11:
            ongrid = False
        else:
            ypos -= 1
    elif direction == "B":
        if ypos == 1:
            ongrid = False
        else:
            ypos -= 1
    elif direction == "L":
        if xpos == 1:
            ongrid = False
        else:
            xpos -= 1
    
    if ongrid == True:
        direction = ChangeDirection(direction, grid[ypos - 1][xpos - 1])
        ChangeDirection(xpos, ypos)

    return xpos, ypos, direction, ongrid

ant1 = True
ant2 = True

while True:
    moves = input()
    if moves == "-1":
        break
        
    for simulations in range(int(moves)):
        if ant1 == True:
            x1, y1, dir1, ant1 = MoveAnt(x1, y1, dir1)

        if ant2 == True:
            x2, y2, dir2, ant2 = MoveAnt(x2, y2, dir2)

    PrintGrid()
    if ant1 == True:
        print(x1, y1, dir1)
    else:
        print("Removed")
    if ant2 == True:
        print(x2, y2, dir2)
    else:
        print("Removed")
    