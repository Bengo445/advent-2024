
f = open("input.txt", "r")
input = f.read().split("\n\n")

# get board info
board = []
walls = []
boxes = []
robot = [0,0]
for y, line in enumerate(input[0].split("\n")):
    board.append(line.strip())
    for x in range(len(line)):
        if line[x] == "#":
            walls.append([y,x])
        if line[x] == "O":
            boxes.append([y,x])
        if line[x] == "@":
            robot = [y,x]
# get instructions
instructions = input[1].replace("\n", "")

# do da thang
DIRS = {  #y,x
    "^": [-1,0],
    ">": [0,1],
    "v": [1,0],
    "<": [0,-1],
}

def try_move_box(pos, dir):
    box_i = boxes.index(pos)
    facing_pos = [pos[0]+dir[0], pos[1]+dir[1]]
    moving = False
    if facing_pos in walls:
        moving = False
    elif facing_pos in boxes:
        moving = try_move_box(facing_pos, dir)
    else:
        moving = True

    if moving:
        boxes[box_i] = [facing_pos[0], facing_pos[1]]
    return moving

for inst in instructions:
    dir = DIRS[inst]
    facing_pos = [robot[0]+dir[0], robot[1]+dir[1]]
    if facing_pos in walls:
        continue
    elif facing_pos in boxes:
        if try_move_box(facing_pos, dir):
            robot = [facing_pos[0], facing_pos[1]]
    else:
        robot = [facing_pos[0], facing_pos[1]]


result = 0
for box in boxes:
    print(box)
    result += box[0]*100 + box[1]

print(result)