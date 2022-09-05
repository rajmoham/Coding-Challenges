trail_len, command, moves = input().split(" ")
trail_len, moves = int(trail_len), int(moves)
instructions = command * (moves // len(command)) + command[:moves%len(command)]
direction = 1 #1 = UP, 2 = RIGHT, 3 = DOWN, 4 = LEFT

x, y = 0, 0
trails = []

def CheckDirectionOverflow(dir):
    if dir < 1:
        dir = 4
    elif dir > 4:
        dir = 1
    
    return dir

def CheckTrail(x, y):
    for t in trails:
        if t[0] == x and t[1] == y:
            return True

    return False

def MoveExplorer(dir, xpos, ypos):
    lst = []
    lst.append(xpos)
    lst.append(ypos)
    trails.append(lst)
    if dir == 1:
        ypos += 1
    elif dir == 2:
        xpos += 1
    elif dir == 3:
        ypos -= 1
    elif dir == 4:
        xpos -= 1

    return xpos, ypos

for z in instructions:
    if z == "L":
        direction -= 1
    elif z == "R":
        direction += 1

    direction = CheckDirectionOverflow(direction)

    for i in range(4):
        if direction == 1:
            if CheckTrail(x, y + 1) == True:
                direction += 1
            else:
                x, y = MoveExplorer(direction, x, y)
                break
        elif direction == 2:
            if CheckTrail(x + 1, y) == True:
                direction += 1
            else:
                x, y = MoveExplorer(direction, x, y)
                break
        elif direction == 3:
            if CheckTrail(x, y - 1) == True:
                direction += 1
            else:
                x, y  = MoveExplorer(direction, x, y)
                break
        elif direction == 4:
            if CheckTrail(x - 1, y) == True:
                direction = 1
            else:
                x, y = MoveExplorer(direction, x, y)
                break

    if len(trails) > trail_len:
        del trails[0]

print("(" + str(x) + ", " + str(y), ")")