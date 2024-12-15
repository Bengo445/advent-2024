
f = open("input.txt", "r")
input_ = f.read().split("\n\n")

# get board info
board = []
walls = []
boxes = []
robot = [0,0]
for y, line in enumerate(input_[0].split("\n")):
    board.append(line.strip())
    for x in range(len(line)):
        if line[x] == "#":
            walls.append([y,x*2])
        if line[x] == "O":
            boxes.append([y,x*2])
        if line[x] == "@":
            robot = [y,x*2]

def VisualizeMap():
    for y in range(robot[0]-15, robot[0]+16):
        line = ""
        for x in range(robot[1]-15, robot[1]+16):
            pos = [y,x]
            if pos in walls:
                line += "#"
            elif [pos[0], pos[1]-1] in walls:
                line += "#"
            elif pos in boxes:
                line += "["
            elif [pos[0], pos[1]-1] in boxes:
                line += "]"
            elif pos == robot:
                line += "@"
            else:
                line += "."
        print(line)

# get instructions
instructions = input_[1].replace("\n", "")

# do da thang
DIRS = {  #y,x
    "^": [-1, 0],
    ">": [0, 1],
    "v": [1, 0],
    "<": [0, -1],
}
BOX_PUSH_CHECK = {
    "[-1, 0]": [[-1,-1],[-1,0], [-1,1]], 
    "[0, 1]": [[0,2]],
    "[1, 0]": [[1,-1],[1,0], [1,1]], 
    "[0, -1]": [[0,-2]]
}

def try_move_box(pos, dir, boxesmoved:list):
    box_i = boxes.index(pos)

    # check walls
    for check_dir in BOX_PUSH_CHECK[str(dir)]:
        check_pos = [pos[0]+check_dir[0], pos[1]+check_dir[1]]
        if check_pos in walls:
            return False

    moving = True
    # check boxes
    for check_dir in BOX_PUSH_CHECK[str(dir)]:
        check_pos = [pos[0]+check_dir[0], pos[1]+check_dir[1]]
        if check_pos in boxes:
            if try_move_box(check_pos, dir, boxesmoved) == False:
                moving = False

    if moving:
        new_pos = [pos[0]+dir[0], pos[1]+dir[1]]
        boxesmoved.append([box_i, new_pos])
    return moving

for inst in instructions:
    dir = DIRS[inst]
    new_pos = [robot[0]+dir[0], robot[1]+dir[1]]
    alt_new_pos = [robot[0]+dir[0], robot[1]+dir[1]-1]
    if new_pos in walls or [new_pos[0], new_pos[1]-1] in walls:
        continue
    if (new_pos in boxes):
        boxesmoved = []
        if try_move_box(new_pos, dir, boxesmoved):
            robot = [new_pos[0], new_pos[1]]
            for box_info in boxesmoved:
                boxes[box_info[0]] = [box_info[1][0], box_info[1][1]]
    elif (inst != ">" and alt_new_pos in boxes):
        boxesmoved = []
        if try_move_box(alt_new_pos, dir, boxesmoved):
            robot = [new_pos[0], new_pos[1]]
            for box_info in boxesmoved:
                boxes[box_info[0]] = [box_info[1][0], box_info[1][1]]
    else:
        robot = [new_pos[0], new_pos[1]]
    
    #print(inst)
    #VisualizeMap()
    #input()


result = 0
for box in boxes:
    print(box)
    result += box[0]*100 + box[1]

print(result)